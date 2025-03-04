import os
import json
import asyncio
import aiohttp
import aiofiles
import nest_asyncio
from tqdm.asyncio import tqdm

### Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

API_KEY = ""
BASE_URL = ""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--agent', type=str)
parser.add_argument('--save', type=str)
parser.add_argument('--prompt', type=str)
args = parser.parse_args()

MODEL = args.agent
SAVE_FOLD = args.save
prompts_file = args.prompt

print(f"Using model: {MODEL}")
print(f"Saving files: {SAVE_FOLD}")
print(f"Reading file: {prompts_file}")
# x = input(">>> Ready to start?")
# if x != "y":    exit()

CONCURRENT_REQUESTS = 10  # Set the number of concurrent requests
RETRY_LIMIT = 3  # Maximum number of retry attempts
if not os.path.exists(SAVE_FOLD):
    os.makedirs(SAVE_FOLD)


async def save_response(index, response):
    """Save the response to a file asynchronously."""
    filename = f"./{SAVE_FOLD}/{index}.txt"
    assert not os.path.exists(filename), f"File {filename} already exists"
    async with aiofiles.open(filename, 'w') as f:
        await f.write(response)


async def fetch(session, prompt, index, semaphore):
    for attempt in range(RETRY_LIMIT):
        async with semaphore:  # Use semaphore to limit concurrency
            url = f"{BASE_URL}/chat/completions"
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0
            }

            try:
                async with session.post(url, json=payload, headers=headers) as response:
                    if response.status == 200:
                        result = await response.json()
                        content = result['choices'][0]['message']['content']
                    else:
                        raise aiohttp.ClientError(f"Request failed with status {response.status}")
                    
                    await save_response(index, content)
                    return index, content

            except (aiohttp.ClientError, aiohttp.ServerTimeoutError) as e:
                print(f"Attempt {attempt + 1} failed for prompt {index}. Error: {e}")
                if attempt < RETRY_LIMIT - 1:
                    await asyncio.sleep(2 ** attempt)  # Exponential backoff

    return index, f"Request failed after {RETRY_LIMIT} attempts"

async def main(prompts):
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)  # Create a semaphore
    async with aiohttp.ClientSession() as session:
        ### prompt: index, prompt
        tasks = [fetch(session, prompt[1], prompt[0], semaphore) for idx, prompt in enumerate(prompts)]
        results = []
        for f in tqdm.as_completed(tasks):
            result = await f
            results.append(result)
        ### Sort results by index
        results.sort(key=lambda x: x[0])
        return [result[1] for result in results]



### Define the prompts
if __name__ == "__main__":
    prompts = []
    with open(prompts_file) as fp:
        for data in fp.readlines():
            item = json.loads(data.strip())
            prompts.append(item['input'])
    
    start_index = 0
    end_index = len(prompts)
  
    ### exclude existing files
    file_list = os.listdir(SAVE_FOLD)
    prompts_now = [(i, prompts[i])  for i in range(start_index, end_index) if f"{i}.txt" not in file_list]

    ### Get the current event loop and run the main function
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(main(prompts_now))
    error_num = 0
    for i, response in enumerate(responses):
        if "Request failed" in response:
            error_num += 1
    print(f"Failed request: {error_num}")
