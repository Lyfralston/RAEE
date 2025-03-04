import os
import sys
import json

def delete_files(file_list):
    """
    删除列表中的所有文件。

    参数：
    file_list (list): 包含要删除的文件路径的列表。
    """
    for file_path in file_list:
        try:
            os.remove(file_path)
            print(f"已删除文件: {file_path}")
        except FileNotFoundError:
            print(f"文件未找到: {file_path}")
        except Exception as e:
            print(f"删除文件时出错: {file_path} - 错误信息: {e}")

# 示例用法
if not os.path.exists('wrong_files.json'):
    with open('wrong_files.json', 'w') as fp:
        fp.write(str(list()))

with open('wrong_files.json') as fp:
    file_list = json.load(fp)
    if len(file_list) == 0:
        sys.exit(0)
    delete_files(file_list)
    
with open('wrong_files.json', 'w') as fp:
    fp.write(str(list()))
sys.exit(1)