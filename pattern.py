patterns = {
    "ace05": {
        "Business:Declare-Bankruptcy": {
            "event subtype": "declare bankruptcy",
            "event type": "Business:Declare-Bankruptcy",
            "keywords": [
                "bankruptcy",
                "bankrupt",
                "Bankruptcy"
            ],
            "event description": "The event is related to some organization declaring bankruptcy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} declared bankruptcy.",
            "valid roles": [
                "Org"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u7ec4\u7ec7\u5ba3\u5e03\u7834\u4ea7\u6709\u5173\u3002"
        },
        "Business:End-Org": {
            "event subtype": "end organization",
            "event type": "Business:End-Org",
            "keywords": [
                "dissolve",
                "disbanded",
                "close"
            ],
            "event description": "The event is related to some organization ceasing to exist.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} dissolved at {ROLE_Place}.",
            "valid roles": [
                "Org",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4e2a\u7ec4\u7ec7\u4e0d\u590d\u5b58\u5728\u6709\u5173\u3002"
        },
        "Business:Merge-Org": {
            "event subtype": "merge organization",
            "event type": "Business:Merge-Org",
            "keywords": [
                "merge",
                "merging",
                "merger"
            ],
            "event description": "The event is related to two or more organization coming together to form a new organization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} was merged.",
            "valid roles": [
                "Org"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e24\u4e2a\u6216\u4e24\u4e2a\u4ee5\u4e0a\u7684\u7ec4\u7ec7\u805a\u96c6\u5728\u4e00\u8d77\u5f62\u6210\u4e00\u4e2a\u65b0\u7684\u7ec4\u7ec7\u6709\u5173\u3002"
        },
        "Business:Start-Org": {
            "event subtype": "start organization",
            "event type": "Business:Start-Org",
            "keywords": [
                "founded",
                "create",
                "launch"
            ],
            "event description": "The event is related to a new organization being created.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} launched {ROLE_Org} in {ROLE_Place}.",
            "valid roles": [
                "Agent",
                "Org",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6b63\u5728\u521b\u5efa\u7684\u65b0\u7ec4\u7ec7\u6709\u5173\u3002"
        },
        "Conflict:Attack": {
            "event subtype": "attack",
            "event type": "Conflict:Attack",
            "keywords": [
                "war",
                "attack",
                "terrorism"
            ],
            "event description": "The event is related to conflict and some violent physical act.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} attacked {ROLE_Target} by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Attacker",
                "Target",
                "Instrument",
                "Place",
                "Agent"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u548c\u4e00\u4e9b\u66b4\u529b\u7684\u8eab\u4f53\u884c\u4e3a\u6709\u5173\u3002"
        },
        "Conflict:Demonstrate": {
            "event subtype": "demonstrate",
            "event type": "Conflict:Demonstrate",
            "keywords": [
                "rally",
                "protest",
                "demonstrate"
            ],
            "event description": "The event is related to a large number of people coming together to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} protested at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u8bb8\u591a\u4eba\u805a\u96c6\u5728\u4e00\u8d77\u6297\u8bae\u6709\u5173\u3002"
        },
        "Contact:Meet": {
            "event subtype": "meet",
            "event type": "Contact:Meet",
            "keywords": [
                "meeting",
                "met",
                "summit"
            ],
            "event description": "The event is related to a group of people meeting and interacting with one another face-to-face.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} met at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u6d3b\u52a8\u4e0e\u4e00\u7fa4\u4eba\u89c1\u9762\u5e76\u9762\u5bf9\u9762\u4e92\u52a8\u6709\u5173\u3002"
        },
        "Contact:Phone-Write": {
            "event subtype": "phone write",
            "event type": "Contact:Phone-Write",
            "keywords": [
                "call",
                "communicate",
                "e-mail"
            ],
            "event description": "The event is related to people phone calling or messaging one another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} called or texted messages at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4eba\u4eec\u76f8\u4e92\u6253\u7535\u8bdd\u6216\u53d1\u77ed\u4fe1\u6709\u5173\u3002"
        },
        "Justice:Acquit": {
            "event subtype": "acquit",
            "event type": "Justice:Acquit",
            "keywords": [
                "acquitted",
                "acquittal",
                "acquit"
            ],
            "event description": "The event is related to someone being acquitted.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was acquitted of the charges by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u88ab\u65e0\u7f6a\u91ca\u653e\u6709\u5173\u3002"
        },
        "Justice:Appeal": {
            "event subtype": "appeal",
            "event type": "Justice:Appeal",
            "keywords": [
                "appeal",
                "appealing",
                "appeals"
            ],
            "event description": "The event is related to someone appealing the decision of a court.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Plaintiff} in {ROLE_Place} appealed the adjudication from {ROLE_Adjudicator}.",
            "valid roles": [
                "Plaintiff",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u5bf9\u6cd5\u9662\u5224\u51b3\u63d0\u51fa\u4e0a\u8bc9\u6709\u5173\u3002"
        },
        "Justice:Arrest-Jail": {
            "event subtype": "arrest jail",
            "event type": "Justice:Arrest-Jail",
            "keywords": [
                "arrest",
                "jail",
                "detained"
            ],
            "event description": "The event is related to a person getting arrested or a person being sent to jail.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was sent to jailed or arrested by {ROLE_Agent} in {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u4e00\u4e2a\u4eba\u88ab\u902e\u6355\u6216\u88ab\u9001\u8fdb\u76d1\u72f1\u6709\u5173\u3002"
        },
        "Justice:Charge-Indict": {
            "event subtype": "charge indict",
            "event type": "Justice:Charge-Indict",
            "keywords": [
                "indict",
                "charged",
                "accused"
            ],
            "event description": "The event is related to someone or some organization being accused of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was charged by {ROLE_Prosecutor} in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Prosecutor",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u6216\u67d0\u4e2a\u7ec4\u7ec7\u88ab\u6307\u63a7\u72af\u7f6a\u6709\u5173\u3002"
        },
        "Justice:Convict": {
            "event subtype": "convict",
            "event type": "Justice:Convict",
            "keywords": [
                "convicted",
                "guilty",
                "verdict"
            ],
            "event description": "The event is related to someone being found guilty of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was convicted of a crime in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u88ab\u5224\u6709\u7f6a\u6709\u5173\u3002"
        },
        "Justice:Execute": {
            "event subtype": "execute",
            "event type": "Justice:Execute",
            "keywords": [
                "execution",
                "executed",
                "execute"
            ],
            "event description": "The event is related to someone being executed to death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was executed by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u88ab\u6267\u884c\u6b7b\u5211\u6709\u5173\u3002"
        },
        "Justice:Extradite": {
            "event subtype": "extradite",
            "event type": "Justice:Extradite",
            "keywords": [
                "extradition",
                "extradited",
                "extraditing"
            ],
            "event description": "The event is related to justice. The event occurs when a person was extradited from one place to another place.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was extradicted to {ROLE_Destination} from {ROLE_Origin}, and {ROLE_Agent} was responsible for the extradition.",
            "valid roles": [
                "Person",
                "Destination",
                "Origin",
                "Agent"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6b63\u4e49\u6709\u5173\u3002\u5f53\u4e00\u4e2a\u4eba\u88ab\u4ece\u4e00\u4e2a\u5730\u65b9\u5f15\u6e21\u5230\u53e6\u4e00\u4e2a\u5730\u65b9\u65f6\uff0c\u5c31\u4f1a\u53d1\u751f\u8fd9\u79cd\u60c5\u51b5\u3002"
        },
        "Justice:Fine": {
            "event subtype": "fine",
            "event type": "Justice:Fine",
            "keywords": [
                "fine",
                "fined",
                "payouts"
            ],
            "event description": "The event is related to someone being issued a financial punishment.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} in {ROLE_Place} was ordered by {ROLE_Adjudicator} to pay a fine.",
            "valid roles": [
                "Entity",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u53d7\u5230\u7ecf\u6d4e\u5904\u7f5a\u6709\u5173\u3002"
        },
        "Justice:Pardon": {
            "event subtype": "pardon",
            "event type": "Justice:Pardon",
            "keywords": [
                "pardon",
                "pardoned",
                "remission"
            ],
            "event description": "The event is related to someone being pardoned.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} received a pardon from {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Adjudicator"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u88ab\u8d66\u514d\u6709\u5173\u3002"
        },
        "Justice:Release-Parole": {
            "event subtype": "release parole",
            "event type": "Justice:Release-Parole",
            "keywords": [
                "parole",
                "release",
                "free"
            ],
            "event description": "The event is related to an end to someone's custody in prison.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was released by {ROLE_Entity} from {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u5728\u76d1\u72f1\u7684\u76d1\u7981\u7ed3\u675f\u6709\u5173\u3002"
        },
        "Justice:Sentence": {
            "event subtype": "sentence",
            "event type": "Justice:Sentence",
            "keywords": [
                "sentenced",
                "sentencing",
                "sentence"
            ],
            "event description": "The event is related to someone being sentenced to punishment because of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was sentenced to punishment in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u56e0\u72af\u7f6a\u800c\u88ab\u5224\u5211\u6709\u5173\u3002"
        },
        "Justice:Sue": {
            "event subtype": "sue",
            "event type": "Justice:Sue",
            "keywords": [
                "sue",
                "lawsuit",
                "suit"
            ],
            "event description": "The event is related to a court proceeding that has been initiated and someone sue the other.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was sued by {ROLE_Plaintiff} in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Plaintiff",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5df2\u7ecf\u542f\u52a8\u7684\u6cd5\u5ead\u7a0b\u5e8f\u6709\u5173\uff0c\u6709\u4eba\u8d77\u8bc9\u53e6\u4e00\u4e2a\u4eba\u3002"
        },
        "Justice:Trial-Hearing": {
            "event subtype": "trial hearing",
            "event type": "Justice:Trial-Hearing",
            "keywords": [
                "trial",
                "hearing",
                "proceeding"
            ],
            "event description": "The event is related to a trial or hearing for someone.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant}, prosecuted by {ROLE_Prosecutor}, faced a trial in {ROLE_Place}, and the hearing was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Prosecutor",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u7684\u5ba1\u5224\u6216\u542c\u8bc1\u4f1a\u6709\u5173\u3002"
        },
        "Life:Be-Born": {
            "event subtype": "born",
            "event type": "Life:Be-Born",
            "keywords": [
                "born",
                "birth",
                "bore"
            ],
            "event description": "The event is related to life and someone is given birth to.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was born in {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u547d\u6709\u5173\uff0c\u6709\u4eba\u51fa\u751f\u4e86\u3002"
        },
        "Life:Die": {
            "event subtype": "die",
            "event type": "Life:Die",
            "keywords": [
                "kill",
                "death",
                "assassination"
            ],
            "event description": "The event is related to life and someone died.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} died by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Agent",
                "Victim",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u547d\u548c\u67d0\u4eba\u53bb\u4e16\u6709\u5173\u3002"
        },
        "Life:Divorce": {
            "event subtype": "divorce",
            "event type": "Life:Divorce",
            "keywords": [
                "divorce",
                "divorced",
                "Divorce"
            ],
            "event description": "The event is related to life and someone was divorced.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} divorced in {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u6d3b\u6709\u5173\uff0c\u6709\u4eba\u79bb\u5a5a\u4e86\u3002"
        },
        "Life:Injure": {
            "event subtype": "injure",
            "event type": "Life:Injure",
            "keywords": [
                "injure",
                "wounded",
                "hurt"
            ],
            "event description": "The event is related to life and someone is injured.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} injured by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Agent",
                "Victim",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u547d\u6709\u5173\uff0c\u6709\u4eba\u53d7\u4f24\u4e86\u3002"
        },
        "Life:Marry": {
            "event subtype": "marry",
            "event type": "Life:Marry",
            "keywords": [
                "marry",
                "marriage",
                "married"
            ],
            "event description": "The event is related to life and someone is married.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} got married in {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u751f\u6d3b\u6709\u5173\uff0c\u6709\u4eba\u7ed3\u5a5a\u4e86\u3002"
        },
        "Movement:Transport": {
            "event subtype": "transport",
            "event type": "Movement:Transport",
            "keywords": [
                "travel",
                "go",
                "move"
            ],
            "event description": "The event is related to movement. The event occurs when a weapon or vehicle is moved from one place to another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Artifact} was sent to {ROLE_Destination} from {ROLE_Origin} by {ROLE_Vehicle}, and {ROLE_Agent} was responsible for the transport.",
            "valid roles": [
                "Artifact",
                "Destination",
                "Origin",
                "Vehicle",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\u3002\u5f53\u6b66\u5668\u6216\u8f66\u8f86\u4ece\u4e00\u4e2a\u5730\u65b9\u79fb\u52a8\u5230\u53e6\u4e00\u4e2a\u5730\u65b9\u65f6\uff0c\u4e8b\u4ef6\u5c31\u53d1\u751f\u4e86\u3002"
        },
        "Personnel:Elect": {
            "event subtype": "elect",
            "event type": "Personnel:Elect",
            "keywords": [
                "election",
                "elect",
                "elected"
            ],
            "event description": "The event is related to a candidate wins an election.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was elected a position, and the election was voted by {ROLE_Entity} in {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5019\u9009\u4eba\u8d62\u5f97\u9009\u4e3e\u6709\u5173\u3002"
        },
        "Personnel:End-Position": {
            "event subtype": "end position",
            "event type": "Personnel:End-Position",
            "keywords": [
                "former",
                "laid off",
                "fired"
            ],
            "event description": "The event is related to a person stops working for an organization or a hiring manager.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} stopped working for {ROLE_Entity} at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u505c\u6b62\u4e3a\u7ec4\u7ec7\u6216\u62db\u8058\u7ecf\u7406\u5de5\u4f5c\u6709\u5173\u3002"
        },
        "Personnel:Nominate": {
            "event subtype": "nominate",
            "event type": "Personnel:Nominate",
            "keywords": [
                "named",
                "nomination",
                "nominate"
            ],
            "event description": "The event is related to a person being nominated for a position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was nominated by {ROLE_Agent} to do a job.",
            "valid roles": [
                "Person",
                "Agent"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u4e00\u4e2a\u4eba\u88ab\u63d0\u540d\u4e00\u4e2a\u804c\u4f4d\u6709\u5173\u3002"
        },
        "Personnel:Start-Position": {
            "event subtype": "start position",
            "event type": "Personnel:Start-Position",
            "keywords": [
                "hire",
                "appoint",
                "join"
            ],
            "event description": "The event is related to a person begins working for an organization or a hiring manager.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} got new job and was hired by {ROLE_Entity} in {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u4e00\u4e2a\u4eba\u5f00\u59cb\u4e3a\u4e00\u4e2a\u7ec4\u7ec7\u6216\u62db\u8058\u7ecf\u7406\u5de5\u4f5c\u6709\u5173\u3002"
        },
        "Transaction:Transfer-Money": {
            "event subtype": "transfer money",
            "event type": "Transaction:Transfer-Money",
            "keywords": [
                "pay",
                "donation",
                "loan"
            ],
            "event description": "The event is related to transaction. The event occurs when someone is giving, receiving, borrowing, or lending money.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} paid {ROLE_Recipient} in {ROLE_Place}.",
            "valid roles": [
                "Giver",
                "Recipient",
                "Place",
                "Beneficiary"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u76f8\u5173\u3002\u8fd9\u4e00\u4e8b\u4ef6\u53d1\u751f\u5728\u67d0\u4eba\u7ed9\u4e88\u3001\u63a5\u53d7\u3001\u501f\u6b3e\u6216\u653e\u8d37\u65f6\u3002"
        },
        "Transaction:Transfer-Ownership": {
            "event subtype": "transfer ownership",
            "event type": "Transaction:Transfer-Ownership",
            "keywords": [
                "sell",
                "buy",
                "acquire"
            ],
            "event description": "The event is related to transaction. The event occurs when an item or an organization is sold or gave to some other.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Buyer} got {ROLE_Artifact} from {ROLE_Place} in {ROLE_Place}.",
            "valid roles": [
                "Buyer",
                "Artifact",
                "Seller",
                "Place",
                "Beneficiary"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u76f8\u5173\u3002\u5f53\u4e00\u4ef6\u7269\u54c1\u6216\u4e00\u4e2a\u7ec4\u7ec7\u88ab\u51fa\u552e\u6216\u8d60\u4e0e\u4ed6\u4eba\u65f6\uff0c\u5c31\u4f1a\u53d1\u751f\u8fd9\u4e00\u4e8b\u4ef6\u3002"
        }
    },
    "richere-en": {
        "Business:Declare-Bankruptcy": {
            "event subtype": "declare bankruptcy",
            "event type": "Business:Declare-Bankruptcy",
            "keywords": [
                "bankruptcy",
                "bankrupt",
                "Bankruptcy"
            ],
            "event description": "The event is related to some organization declaring bankruptcy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} declared bankruptcy.",
            "valid roles": [
                "Org"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u7ec4\u7ec7\u5ba3\u5e03\u7834\u4ea7\u6709\u5173\u3002"
        },
        "Business:End-Org": {
            "event subtype": "end organization",
            "event type": "Business:End-Org",
            "keywords": [
                "dissolve",
                "disbanded",
                "close"
            ],
            "event description": "The event is related to some organization ceasing to exist.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} dissolved in {ROLE_Place}.",
            "valid roles": [
                "Org",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4e2a\u7ec4\u7ec7\u4e0d\u590d\u5b58\u5728\u6709\u5173\u3002"
        },
        "Business:Merge-Org": {
            "event subtype": "merge organization",
            "event type": "Business:Merge-Org",
            "keywords": [
                "merge",
                "merging",
                "merger"
            ],
            "event description": "The event is related to two or more organization coming together to form a new organization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} was merged.",
            "valid roles": [
                "Org"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e24\u4e2a\u6216\u4e24\u4e2a\u4ee5\u4e0a\u7684\u7ec4\u7ec7\u805a\u96c6\u5728\u4e00\u8d77\u5f62\u6210\u4e00\u4e2a\u65b0\u7684\u7ec4\u7ec7\u6709\u5173\u3002"
        },
        "Business:Start-Org": {
            "event subtype": "start organization",
            "event type": "Business:Start-Org",
            "keywords": [
                "founded",
                "create",
                "launch"
            ],
            "event description": "The event is related to a new organization being created.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} launched {ROLE_Org} at {ROLE_Place}.",
            "valid roles": [
                "Agent",
                "Org",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6b63\u5728\u521b\u5efa\u7684\u65b0\u7ec4\u7ec7\u6709\u5173\u3002"
        },
        "Conflict:Attack": {
            "event subtype": "attack",
            "event type": "Conflict:Attack",
            "keywords": [
                "war",
                "attack",
                "terrorism"
            ],
            "event description": "The event is related to conflict and some violent physical act.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} attacked {ROLE_Target} by {ROLE_Instrument} at {ROLE_Place}.",
            "valid roles": [
                "Attacker",
                "Target",
                "Instrument",
                "Place",
                "Agent"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u548c\u4e00\u4e9b\u66b4\u529b\u7684\u8eab\u4f53\u884c\u4e3a\u6709\u5173\u3002"
        },
        "Conflict:Demonstrate": {
            "event subtype": "demonstrate",
            "event type": "Conflict:Demonstrate",
            "keywords": [
                "rally",
                "protest",
                "demonstrate"
            ],
            "event description": "The event is related to a large number of people coming together to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} protested at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u8bb8\u591a\u4eba\u805a\u96c6\u5728\u4e00\u8d77\u6297\u8bae\u6709\u5173\u3002"
        },
        "Contact:Meet": {
            "event subtype": "meet",
            "event type": "Contact:Meet",
            "keywords": [
                "meeting",
                "met",
                "summit"
            ],
            "event description": "The event is related to a group of people meeting and interacting with one another face-to-face.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} met at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u6d3b\u52a8\u4e0e\u4e00\u7fa4\u4eba\u89c1\u9762\u5e76\u9762\u5bf9\u9762\u4e92\u52a8\u6709\u5173\u3002"
        },
        "Contact:Correspondence": {
            "event subtype": "contact correspondence",
            "event type": "Contact:Correspondence",
            "keywords": [
                "call",
                "teleconference",
                "e-mail"
            ],
            "event description": "The event happens when a face\u2010to\u2010face meeting between sender and receiver is not explicitly stated. This includes written, phone, or electronic communication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} contacted each other at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u5f53\u53d1\u9001\u65b9\u548c\u63a5\u6536\u65b9\u4e4b\u95f4\u7684\u9762\u5bf9\u9762\u4f1a\u8bae\u6ca1\u6709\u660e\u786e\u8bf4\u660e\u65f6\uff0c\u5c31\u4f1a\u53d1\u751f\u8be5\u4e8b\u4ef6\u3002\u8fd9\u5305\u62ec\u4e66\u9762\u3001\u7535\u8bdd\u6216\u7535\u5b50\u901a\u4fe1\u3002"
        },
        "Contact:Broadcast": {
            "event subtype": "broadcast",
            "event type": "Contact:Broadcast",
            "keywords": [
                "statement",
                "announce",
                "say"
            ],
            "event description": "The event happens when a person or an organization contact with the media and other publicity or announcement conference.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} made announcement to {ROLE_Audience} at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Audience",
                "Place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u53d1\u751f\u65f6\uff0c\u4e00\u4e2a\u4eba\u6216\u4e00\u4e2a\u7ec4\u7ec7\u63a5\u89e6\u5a92\u4f53\u548c\u5176\u4ed6\u5ba3\u4f20\u6216\u516c\u544a\u4f1a\u8bae\u3002"
        },
        "Contact:Contact": {
            "event subtype": "contact",
            "event type": "Contact:Contact",
            "keywords": [
                "said",
                "talk",
                "tell"
            ],
            "event description": "The event happens when there is no explicit mention of contact ways of communication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} talked to each other at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u5f53\u6ca1\u6709\u660e\u786e\u63d0\u5230\u6c9f\u901a\u7684\u8054\u7cfb\u65b9\u5f0f\u65f6\uff0c\u4e8b\u4ef6\u5c31\u53d1\u751f\u4e86\u3002"
        },
        "Justice:Acquit": {
            "event subtype": "acquit",
            "event type": "Justice:Acquit",
            "keywords": [
                "acquitted",
                "acquittal",
                "acquit"
            ],
            "event description": "The event is related to someone being acquitted.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was acquitted of the charges by {ROLE_Adjudicator} at {ROLE_Place}.",
            "valid roles": [
                "Defendant",
                "Adjudicator",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u88ab\u65e0\u7f6a\u91ca\u653e\u6709\u5173\u3002"
        },
        "Justice:Appeal": {
            "event subtype": "appeal",
            "event type": "Justice:Appeal",
            "keywords": [
                "appeal",
                "appealing",
                "appeals"
            ],
            "event description": "The event is related to someone appealing the decision of a court.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} in {ROLE_Place} appealed the adjudication by {ROLE_Prosecutor} from {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Place",
                "Adjudicator",
                "Prosecutor"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u5bf9\u6cd5\u9662\u5224\u51b3\u63d0\u51fa\u4e0a\u8bc9\u6709\u5173\u3002"
        },
        "Justice:Arrest-Jail": {
            "event subtype": "arrest jail",
            "event type": "Justice:Arrest-Jail",
            "keywords": [
                "arrest",
                "jail",
                "detained"
            ],
            "event description": "The event is related to a person getting arrested or a person being sent to jail.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was sent to jailed or arrested by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u4e00\u4e2a\u4eba\u88ab\u902e\u6355\u6216\u88ab\u9001\u8fdb\u76d1\u72f1\u6709\u5173\u3002"
        },
        "Justice:Charge-Indict": {
            "event subtype": "charge indict",
            "event type": "Justice:Charge-Indict",
            "keywords": [
                "indict",
                "charged",
                "accused"
            ],
            "event description": "The event is related to someone or some organization being accused of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was charged by {ROLE_Prosecutor} at {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Prosecutor",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u6216\u67d0\u4e2a\u7ec4\u7ec7\u88ab\u6307\u63a7\u72af\u7f6a\u6709\u5173\u3002"
        },
        "Justice:Convict": {
            "event subtype": "convict",
            "event type": "Justice:Convict",
            "keywords": [
                "convicted",
                "guilty",
                "verdict"
            ],
            "event description": "The event is related to someone being found guilty of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was convicted of a crime in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u88ab\u5224\u6709\u7f6a\u6709\u5173\u3002"
        },
        "Justice:Execute": {
            "event subtype": "execute",
            "event type": "Justice:Execute",
            "keywords": [
                "execution",
                "executed",
                "execute"
            ],
            "event description": "The event is related to someone being executed to death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was executed by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u88ab\u6267\u884c\u6b7b\u5211\u6709\u5173\u3002"
        },
        "Justice:Extradite": {
            "event subtype": "extradite",
            "event type": "Justice:Extradite",
            "keywords": [
                "extradition",
                "extradited",
                "extraditing"
            ],
            "event description": "The event is related to justice. The event occurs when a person was extradited from one place to another place.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was extradicted to {ROLE_Destination} from {ROLE_Origin}, and {ROLE_Agent} was responsible for the extradition.",
            "valid roles": [
                "Person",
                "Destination",
                "Origin",
                "Agent"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6b63\u4e49\u6709\u5173\u3002\u5f53\u4e00\u4e2a\u4eba\u88ab\u4ece\u4e00\u4e2a\u5730\u65b9\u5f15\u6e21\u5230\u53e6\u4e00\u4e2a\u5730\u65b9\u65f6\uff0c\u5c31\u4f1a\u53d1\u751f\u8fd9\u79cd\u60c5\u51b5\u3002"
        },
        "Justice:Fine": {
            "event subtype": "fine",
            "event type": "Justice:Fine",
            "keywords": [
                "fine",
                "fined",
                "payouts"
            ],
            "event description": "The event is related to someone being issued a financial punishment.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} in {ROLE_Place} was ordered by {ROLE_Adjudicator} to pay a fine.",
            "valid roles": [
                "Entity",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u53d7\u5230\u7ecf\u6d4e\u5904\u7f5a\u6709\u5173\u3002"
        },
        "Justice:Pardon": {
            "event subtype": "pardon",
            "event type": "Justice:Pardon",
            "keywords": [
                "pardon",
                "pardoned",
                "remission"
            ],
            "event description": "The event is related to someone being pardoned.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} received a pardon from {ROLE_Adjudicator} at {ROLE_Place}.",
            "valid roles": [
                "Defendant",
                "Adjudicator",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u88ab\u8d66\u514d\u6709\u5173\u3002"
        },
        "Justice:Release-Parole": {
            "event subtype": "release parole",
            "event type": "Justice:Release-Parole",
            "keywords": [
                "parole",
                "release",
                "free"
            ],
            "event description": "The event is related to an end to someone's custody in prison.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was released by {ROLE_Agent} from {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u5728\u76d1\u72f1\u7684\u76d1\u7981\u7ed3\u675f\u6709\u5173\u3002"
        },
        "Justice:Sentence": {
            "event subtype": "sentence",
            "event type": "Justice:Sentence",
            "keywords": [
                "sentenced",
                "sentencing",
                "sentence"
            ],
            "event description": "The event is related to someone being sentenced to punishment because of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was sentenced to punishment in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u56e0\u72af\u7f6a\u800c\u88ab\u5224\u5211\u6709\u5173\u3002"
        },
        "Justice:Sue": {
            "event subtype": "sue",
            "event type": "Justice:Sue",
            "keywords": [
                "sue",
                "lawsuit",
                "suit"
            ],
            "event description": "The event is related to a court proceeding that has been initiated and someone sue the other.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was sued by {ROLE_Plaintiff} in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Plaintiff",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5df2\u7ecf\u542f\u52a8\u7684\u6cd5\u5ead\u7a0b\u5e8f\u6709\u5173\uff0c\u6709\u4eba\u8d77\u8bc9\u53e6\u4e00\u4e2a\u4eba\u3002"
        },
        "Justice:Trial-Hearing": {
            "event subtype": "trial hearing",
            "event type": "Justice:Trial-Hearing",
            "keywords": [
                "trial",
                "hearing",
                "proceeding"
            ],
            "event description": "The event is related to a trial or hearing for someone.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant}, prosecuted by {ROLE_Prosecutor}, faced a trial in {ROLE_Place}. The hearing was judged by {ROLE_Adjudicator}.",
            "valid roles": [
                "Defendant",
                "Prosecutor",
                "Place",
                "Adjudicator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u7684\u5ba1\u5224\u6216\u542c\u8bc1\u4f1a\u6709\u5173\u3002"
        },
        "Life:Be-Born": {
            "event subtype": "born",
            "event type": "Life:Be-Born",
            "keywords": [
                "born",
                "birth",
                "bore"
            ],
            "event description": "The event is related to life and someone is given birth to.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was born at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u547d\u6709\u5173\uff0c\u6709\u4eba\u51fa\u751f\u4e86\u3002"
        },
        "Life:Die": {
            "event subtype": "die",
            "event type": "Life:Die",
            "keywords": [
                "kill",
                "death",
                "assassination"
            ],
            "event description": "The event is related to life and someone died.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} died by {ROLE_Instrument} at {ROLE_Place}.",
            "valid roles": [
                "Agent",
                "Victim",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u547d\u548c\u67d0\u4eba\u53bb\u4e16\u6709\u5173\u3002"
        },
        "Life:Divorce": {
            "event subtype": "divorce",
            "event type": "Life:Divorce",
            "keywords": [
                "divorce",
                "divorced",
                "Divorce"
            ],
            "event description": "The event is related to life and someone was divorced.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} divorced at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u6d3b\u6709\u5173\uff0c\u6709\u4eba\u79bb\u5a5a\u4e86\u3002"
        },
        "Life:Injure": {
            "event subtype": "injure",
            "event type": "Life:Injure",
            "keywords": [
                "injure",
                "wounded",
                "hurt"
            ],
            "event description": "The event is related to life and someone is injured.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} injured by {ROLE_Instrument} at {ROLE_Place}.",
            "valid roles": [
                "Agent",
                "Victim",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u547d\u6709\u5173\uff0c\u6709\u4eba\u53d7\u4f24\u4e86\u3002"
        },
        "Life:Marry": {
            "event subtype": "marry",
            "event type": "Life:Marry",
            "keywords": [
                "marry",
                "marriage",
                "married"
            ],
            "event description": "The event is related to life and someone is married.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} got married at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u751f\u6d3b\u6709\u5173\uff0c\u6709\u4eba\u7ed3\u5a5a\u4e86\u3002"
        },
        "Movement:Transport-Person": {
            "event subtype": "transport person",
            "event type": "Movement:Transport-Person",
            "keywords": [
                "travel",
                "go",
                "move"
            ],
            "event description": "The event is related to movement. The event occurs when a person moves or is moved from one place to another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was moved to {ROLE_Destination} from {ROLE_Origin} by {ROLE_Instrument}, and {ROLE_Agent} was responsible for the movement.",
            "valid roles": [
                "Person",
                "Destination",
                "Origin",
                "Instrument",
                "Agent"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\u3002\u5f53\u4e00\u4e2a\u4eba\u4ece\u4e00\u4e2a\u5730\u65b9\u79fb\u52a8\u5230\u53e6\u4e00\u4e2a\u5730\u65b9\u65f6\uff0c\u5c31\u4f1a\u53d1\u751f\u8fd9\u79cd\u60c5\u51b5\u3002"
        },
        "Movement:Transport-Artifact": {
            "event subtype": "transport artifact",
            "event type": "Movement:Transport-Artifact",
            "keywords": [
                "export",
                "deliver",
                "send"
            ],
            "event description": "The event is related to movement. The event occurs when an artifact, like items or weapon, is moved from one place to another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Artifact} was sent to {ROLE_Destination} from {ROLE_Origin}, and {ROLE_Agent} was responsible for the transport.",
            "valid roles": [
                "Artifact",
                "Destination",
                "Origin",
                "Agent"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\u3002\u5f53\u7269\u54c1\u6216\u6b66\u5668\u7b49\u795e\u5668\u4ece\u4e00\u4e2a\u5730\u65b9\u79fb\u52a8\u5230\u53e6\u4e00\u4e2a\u5730\u65b9\u65f6\uff0c\u5c31\u4f1a\u53d1\u751f\u8be5\u4e8b\u4ef6\u3002"
        },
        "Personnel:Elect": {
            "event subtype": "elect",
            "event type": "Personnel:Elect",
            "keywords": [
                "election",
                "elect",
                "elected"
            ],
            "event description": "The event is related to a candidate wins an election.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was elected a position, and the election was voted by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5019\u9009\u4eba\u8d62\u5f97\u9009\u4e3e\u6709\u5173\u3002"
        },
        "Personnel:End-Position": {
            "event subtype": "end position",
            "event type": "Personnel:End-Position",
            "keywords": [
                "former",
                "laid off",
                "fired"
            ],
            "event description": "The event is related to a person stops working for an organization or a hiring manager.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} stopped working for {ROLE_Entity} at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u67d0\u4eba\u505c\u6b62\u4e3a\u7ec4\u7ec7\u6216\u62db\u8058\u7ecf\u7406\u5de5\u4f5c\u6709\u5173\u3002"
        },
        "Personnel:Nominate": {
            "event subtype": "nominate",
            "event type": "Personnel:Nominate",
            "keywords": [
                "named",
                "nomination",
                "nominate"
            ],
            "event description": "The event is related to a person being nominated for a position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was nominated by {ROLE_Entity} to do a job at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u4e00\u4e2a\u4eba\u88ab\u63d0\u540d\u4e00\u4e2a\u804c\u4f4d\u6709\u5173\u3002"
        },
        "Personnel:Start-Position": {
            "event subtype": "start position",
            "event type": "Personnel:Start-Position",
            "keywords": [
                "hire",
                "appoint",
                "join"
            ],
            "event description": "The event is related to a person begins working for an organization or a hiring manager.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} got new job and was hired by {ROLE_Entity} at {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u4e00\u4e2a\u4eba\u5f00\u59cb\u4e3a\u4e00\u4e2a\u7ec4\u7ec7\u6216\u62db\u8058\u7ecf\u7406\u5de5\u4f5c\u6709\u5173\u3002"
        },
        "Transaction:Transfer-Money": {
            "event subtype": "transfer money",
            "event type": "Transaction:Transfer-Money",
            "keywords": [
                "pay",
                "donation",
                "loan"
            ],
            "event description": "The event is related to transaction. The event occurs when someone is giving, receiving, borrowing, or lending money.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} paid {ROLE_Recipient} at {ROLE_Place}.",
            "valid roles": [
                "Giver",
                "Recipient",
                "Place",
                "Beneficiary"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u76f8\u5173\u3002\u8fd9\u4e00\u4e8b\u4ef6\u53d1\u751f\u5728\u67d0\u4eba\u7ed9\u4e88\u3001\u63a5\u53d7\u3001\u501f\u6b3e\u6216\u653e\u8d37\u65f6\u3002"
        },
        "Transaction:Transfer-Ownership": {
            "event subtype": "transfer ownership",
            "event type": "Transaction:Transfer-Ownership",
            "keywords": [
                "sell",
                "buy",
                "acquire"
            ],
            "event description": "The event is events refer to the buying, selling, loaning, borrowing, giving, receiving, bartering, stealing, or renting of physical items, assets,or organizations.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "The ownership of {ROLE_Thing} from {ROLE_Giver} was transferred to {ROLE_Recipient} at {ROLE_Place}.",
            "valid roles": [
                "Thing",
                "Giver",
                "Recipient",
                "Place",
                "Beneficiary"
            ],
            "chinese event description": "\u4e8b\u4ef6\u662f\u6307\u5b9e\u7269\u3001\u8d44\u4ea7\u6216\u7ec4\u7ec7\u7684\u8d2d\u4e70\u3001\u51fa\u552e\u3001\u501f\u51fa\u3001\u501f\u7528\u3001\u7ed9\u4e88\u3001\u63a5\u6536\u3001\u6613\u8d27\u3001\u7a83\u53d6\u6216\u79df\u7528\u3002"
        },
        "Transaction:Transaction": {
            "event subtype": "transaction",
            "event type": "Transaction:Transaction",
            "keywords": [
                "receive",
                "give",
                "get"
            ],
            "event description": "The event is related to transaction. The event occurs when someone is giving, receiving, borrowing, or lending something when you cannot tell whether it is money or an asset in the context.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} give some things to {ROLE_Recipient} at {ROLE_Place}.",
            "valid roles": [
                "Giver",
                "Recipient",
                "Place",
                "Beneficiary"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u76f8\u5173\u3002\u5f53\u67d0\u4eba\u7ed9\u4e88\u3001\u63a5\u53d7\u3001\u501f\u6b3e\u6216\u51fa\u501f\u67d0\u7269\u65f6\uff0c\u5f53\u4f60\u5728\u4e0a\u4e0b\u6587\u4e2d\u65e0\u6cd5\u5206\u8fa8\u5b83\u662f\u94b1\u8fd8\u662f\u8d44\u4ea7\u65f6\uff0c\u5c31\u4f1a\u53d1\u751f\u8be5\u4e8b\u4ef6\u3002"
        },
        "Manufacture:Artifact": {
            "event subtype": "artifact",
            "event type": "Manufacture:Artifact",
            "keywords": [
                "develop",
                "produce",
                "construct"
            ],
            "event description": "The event occurs whenever a person or an organization builds or manufactures a facility or a weapon, etc",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Artifact} was built by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": [
                "Artifact",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u6bcf\u5f53\u4e00\u4e2a\u4eba\u6216\u4e00\u4e2a\u7ec4\u7ec7\u5efa\u9020\u6216\u5236\u9020\u8bbe\u65bd\u6216\u6b66\u5668\u7b49\u65f6\uff0c\u5c31\u4f1a\u53d1\u751f\u8be5\u4e8b\u4ef6"
        }
    },
    "m2e2": {
        "Conflict:Attack": {
            "event subtype": "attack",
            "event type": "Conflict:Attack",
            "keywords": [
                "war",
                "attack",
                "terrorism"
            ],
            "event description": "The event is related to conflict and some violent physical act.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} attacked {ROLE_Target} by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Attacker",
                "Target",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u548c\u4e00\u4e9b\u66b4\u529b\u7684\u8eab\u4f53\u884c\u4e3a\u6709\u5173\u3002"
        },
        "Conflict:Demonstrate": {
            "event subtype": "demonstrate",
            "event type": "Conflict:Demonstrate",
            "keywords": [
                "rally",
                "protest",
                "demonstrate"
            ],
            "event description": "The event is related to a large number of people coming together to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} protested at {ROLE_Place} with {ROLE_Police}.",
            "valid roles": [
                "Entity",
                "Place",
                "Police"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u8bb8\u591a\u4eba\u805a\u96c6\u5728\u4e00\u8d77\u6297\u8bae\u6709\u5173\u3002"
        },
        "Contact:Meet": {
            "event subtype": "meet",
            "event type": "Contact:Meet",
            "keywords": [
                "meeting",
                "met",
                "summit"
            ],
            "event description": "The event is related to a group of people meeting and interacting with one another face-to-face.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} met at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u6d3b\u52a8\u4e0e\u4e00\u7fa4\u4eba\u89c1\u9762\u5e76\u9762\u5bf9\u9762\u4e92\u52a8\u6709\u5173\u3002"
        },
        "Contact:Phone-Write": {
            "event subtype": "phone write",
            "event type": "Contact:Phone-Write",
            "keywords": [
                "call",
                "communicate",
                "e-mail"
            ],
            "event description": "The event is related to people phone calling or messaging one another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} called or texted messages at {ROLE_Place}.",
            "valid roles": [
                "Entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4eba\u4eec\u76f8\u4e92\u6253\u7535\u8bdd\u6216\u53d1\u77ed\u4fe1\u6709\u5173\u3002"
        },
        "Justice:Arrest-Jail": {
            "event subtype": "arrest jail",
            "event type": "Justice:Arrest-Jail",
            "keywords": [
                "arrest",
                "jail",
                "detained"
            ],
            "event description": "The event is related to a person getting arrested or a person being sent to jail.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was sent to jailed or arrested by {ROLE_Agent} in {ROLE_Place}.",
            "valid roles": [
                "Person",
                "Agent",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u4e00\u4e2a\u4eba\u88ab\u902e\u6355\u6216\u88ab\u9001\u8fdb\u76d1\u72f1\u6709\u5173\u3002"
        },
        "Life:Die": {
            "event subtype": "die",
            "event type": "Life:Die",
            "keywords": [
                "kill",
                "death",
                "assassination"
            ],
            "event description": "The event is related to life and someone died.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} died by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Agent",
                "Victim",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u751f\u547d\u548c\u67d0\u4eba\u53bb\u4e16\u6709\u5173\u3002"
        },
        "Movement:Transport": {
            "event subtype": "transport",
            "event type": "Movement:Transport",
            "keywords": [
                "travel",
                "go",
                "move"
            ],
            "event description": "The event is related to movement. The event occurs when a weapon or vehicle is moved from one place to another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Artifact} was sent to {ROLE_Destination} from {ROLE_Origin} by {ROLE_Vehicle}, and {ROLE_Agent} was responsible for the transport.",
            "valid roles": [
                "Artifact",
                "Destination",
                "Origin",
                "Vehicle",
                "Agent"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\u3002\u5f53\u6b66\u5668\u6216\u8f66\u8f86\u4ece\u4e00\u4e2a\u5730\u65b9\u79fb\u52a8\u5230\u53e6\u4e00\u4e2a\u5730\u65b9\u65f6\uff0c\u4e8b\u4ef6\u5c31\u53d1\u751f\u4e86\u3002"
        },
        "Transaction:Transfer-Money": {
            "event subtype": "transfer money",
            "event type": "Transaction:Transfer-Money",
            "keywords": [
                "pay",
                "donation",
                "loan"
            ],
            "event description": "The event is related to transaction. The event occurs when someone is giving, receiving, borrowing, or lending money.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} paid {ROLE_Recipient}.",
            "valid roles": [
                "Giver",
                "Recipient"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u76f8\u5173\u3002\u8fd9\u4e00\u4e8b\u4ef6\u53d1\u751f\u5728\u67d0\u4eba\u7ed9\u4e88\u3001\u63a5\u53d7\u3001\u501f\u6b3e\u6216\u653e\u8d37\u65f6\u3002"
        }
    },
    "maven": {
        "Achieve": {
            "event description": "The event is related to achieve.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5b9e\u73b0\u6709\u5173\u3002"
        },
        "Action": {
            "event description": "The event is related to action.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u884c\u52a8\u6709\u5173\u3002"
        },
        "Adducing": {
            "event description": "The event is related to adducing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5f15\u8bc1\u6709\u5173\u3002"
        },
        "Agree_or_refuse_to_act": {
            "event description": "The event is related to agree or refuse to act.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u540c\u610f\u6216\u62d2\u7edd\u884c\u52a8\u6709\u5173\u3002"
        },
        "Aiming": {
            "event description": "The event is related to aiming.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u7784\u51c6\u6709\u5173\u3002"
        },
        "Arranging": {
            "event description": "The event is related to arranging.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u5b89\u6392\u6709\u5173\u3002"
        },
        "Arrest": {
            "event description": "The event is related to arrest.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u902e\u6355\u6709\u5173\u3002"
        },
        "Arriving": {
            "event description": "The event is related to arriving.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5230\u8fbe\u6709\u5173\u3002"
        },
        "Assistance": {
            "event description": "The event is related to assistance.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63f4\u52a9\u6709\u5173\u3002"
        },
        "Attack": {
            "event description": "The event is related to attack.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653b\u51fb\u6709\u5173\u3002"
        },
        "Award": {
            "event description": "The event is related to award.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u5956\u52b1\u6709\u5173\u3002"
        },
        "Bearing_arms": {
            "event description": "The event is related to bearing arms.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8f74\u627f\u6b66\u5668\u6709\u5173\u3002"
        },
        "Becoming": {
            "event description": "The event is related to becoming.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6210\u4e3a\u6709\u5173\u3002"
        },
        "Becoming_a_member": {
            "event description": "The event is related to becoming a member.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u6210\u4e3a\u4f1a\u5458\u6709\u5173\u3002"
        },
        "Being_in_operation": {
            "event description": "The event is related to being in operation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6b63\u5728\u8fd0\u884c\u6709\u5173\u3002"
        },
        "Besieging": {
            "event description": "The event is related to besieging.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u56f4\u653b\u6709\u5173\u3002"
        },
        "Bodily_harm": {
            "event description": "The event is related to bodily harm.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8eab\u4f53\u4f24\u5bb3\u6709\u5173\u3002"
        },
        "Body_movement": {
            "event description": "The event is related to body movement.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u8eab\u4f53\u8fd0\u52a8\u6709\u5173\u3002"
        },
        "Breathing": {
            "event description": "The event is related to breathing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u547c\u5438\u6709\u5173\u3002"
        },
        "Bringing": {
            "event description": "The event is related to bringing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5e26\u6765\u6709\u5173\u3002"
        },
        "Building": {
            "event description": "The event is related to building.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5efa\u7b51\u6709\u5173\u3002"
        },
        "Carry_goods": {
            "event description": "The event is related to carry goods.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u642c\u8fd0\u8d27\u7269\u6709\u5173\u3002"
        },
        "Catastrophe": {
            "event description": "The event is related to catastrophe.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u707e\u96be\u6709\u5173\u3002"
        },
        "Causation": {
            "event description": "The event is related to causation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u56e0\u679c\u5173\u7cfb\u6709\u5173\u3002"
        },
        "Cause_change_of_position_on_a_scale": {
            "event description": "The event is related to cause change of position on a scale.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5f15\u8d77\u6807\u5ea6\u4e0a\u4f4d\u7f6e\u7684\u53d8\u5316\u6709\u5173\u3002"
        },
        "Cause_change_of_strength": {
            "event description": "The event is related to cause change of strength.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5f15\u8d77\u5f3a\u5ea6\u53d8\u5316\u6709\u5173\u3002"
        },
        "Cause_to_amalgamate": {
            "event description": "The event is related to cause to amalgamate.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5408\u5e76\u7684\u539f\u56e0\u6709\u5173\u3002"
        },
        "Cause_to_be_included": {
            "event description": "The event is related to cause to be included.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8981\u5305\u542b\u7684\u539f\u56e0\u76f8\u5173\u3002"
        },
        "Cause_to_make_progress": {
            "event description": "The event is related to cause to make progress.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u53d6\u5f97\u8fdb\u5c55\u7684\u539f\u56e0\u6709\u5173\u3002"
        },
        "Change": {
            "event description": "The event is related to change.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u53d8\u5316\u6709\u5173\u3002"
        },
        "Change_event_time": {
            "event description": "The event is related to change event time.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53d8\u66f4\u4e8b\u4ef6\u65f6\u95f4\u76f8\u5173\u3002"
        },
        "Change_of_leadership": {
            "event description": "The event is related to change of leadership.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u9886\u5bfc\u5c42\u7684\u66f4\u8fed\u6709\u5173\u3002"
        },
        "Change_sentiment": {
            "event description": "The event is related to change sentiment.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53d8\u5316\u7684\u60c5\u7eea\u6709\u5173\u3002"
        },
        "Change_tool": {
            "event description": "The event is related to change tool.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53d8\u66f4\u5de5\u5177\u76f8\u5173\u3002"
        },
        "Check": {
            "event description": "The event is related to check.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u68c0\u67e5\u76f8\u5173\u3002"
        },
        "Choosing": {
            "event description": "The event is related to choosing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u9009\u62e9\u6709\u5173\u3002"
        },
        "Collaboration": {
            "event description": "The event is related to collaboration.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u534f\u4f5c\u6709\u5173\u3002"
        },
        "Come_together": {
            "event description": "The event is related to come together.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u662f\u6709\u5173\u8d70\u5230\u4e00\u8d77\u3002"
        },
        "Coming_to_be": {
            "event description": "The event is related to coming to be.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5373\u5c06\u5230\u6765\u6709\u5173\u3002"
        },
        "Coming_to_believe": {
            "event description": "The event is related to coming to believe.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5f00\u59cb\u76f8\u4fe1\u6709\u5173\u3002"
        },
        "Commerce_buy": {
            "event description": "The event is related to commerce buy.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5546\u4e1a\u8d2d\u4e70\u6709\u5173\u3002"
        },
        "Commerce_pay": {
            "event description": "The event is related to commerce pay.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5546\u4e1a\u652f\u4ed8\u6709\u5173\u3002"
        },
        "Commerce_sell": {
            "event description": "The event is related to commerce sell.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5546\u4e1a\u9500\u552e\u6709\u5173\u3002"
        },
        "Commitment": {
            "event description": "The event is related to commitment.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u627f\u8bfa\u6709\u5173\u3002"
        },
        "Committing_crime": {
            "event description": "The event is related to committing crime.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u72af\u7f6a\u6709\u5173\u3002"
        },
        "Communication": {
            "event description": "The event is related to communication.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6c9f\u901a\u6709\u5173\u3002"
        },
        "Competition": {
            "event description": "The event is related to competition.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u7ade\u4e89\u6709\u5173\u3002"
        },
        "Confronting_problem": {
            "event description": "The event is related to confronting problem.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u9762\u5bf9\u95ee\u9898\u6709\u5173\u3002"
        },
        "Connect": {
            "event description": "The event is related to connect.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fde\u63a5\u76f8\u5173\u3002"
        },
        "Conquering": {
            "event description": "The event is related to conquering.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5f81\u670d\u6709\u5173\u3002"
        },
        "Containing": {
            "event description": "The event is related to containing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5305\u542b\u6709\u5173\u3002"
        },
        "Control": {
            "event description": "The event is related to control.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a7\u5236\u6709\u5173\u3002"
        },
        "Convincing": {
            "event description": "The event is related to convincing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8bf4\u670d\u6709\u5173\u3002"
        },
        "Cost": {
            "event description": "The event is related to cost.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6210\u672c\u6709\u5173\u3002"
        },
        "Create_artwork": {
            "event description": "The event is related to create artwork.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u521b\u4f5c\u827a\u672f\u54c1\u6709\u5173\u3002"
        },
        "Creating": {
            "event description": "The event is related to creating.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u521b\u5efa\u76f8\u5173\u3002"
        },
        "Criminal_investigation": {
            "event description": "The event is related to criminal investigation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5211\u4e8b\u8c03\u67e5\u6709\u5173\u3002"
        },
        "Cure": {
            "event description": "The event is related to cure.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6cbb\u7597\u6709\u5173\u3002"
        },
        "Damaging": {
            "event description": "The event is related to damaging.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7834\u574f\u6709\u5173\u3002"
        },
        "Death": {
            "event description": "The event is related to death.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6b7b\u4ea1\u6709\u5173\u3002"
        },
        "Deciding": {
            "event description": "The event is related to deciding.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u51b3\u5b9a\u6709\u5173\u3002"
        },
        "Defending": {
            "event description": "The event is related to defending.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u9632\u5fa1\u6709\u5173\u3002"
        },
        "Departing": {
            "event description": "The event is related to departing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u79bb\u522b\u6709\u5173\u3002"
        },
        "Destroying": {
            "event description": "The event is related to destroying.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6bc1\u706d\u6709\u5173\u3002"
        },
        "Dispersal": {
            "event description": "The event is related to dispersal.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6269\u6563\u6709\u5173\u3002"
        },
        "Earnings_and_losses": {
            "event description": "The event is related to earnings and losses.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6536\u76ca\u548c\u635f\u5931\u6709\u5173\u3002"
        },
        "Education_teaching": {
            "event description": "The event is related to education teaching.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6559\u80b2\u6559\u5b66\u6709\u5173\u3002"
        },
        "Emergency": {
            "event description": "The event is related to emergency.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u5c5e\u4e8e\u7d27\u6025\u4e8b\u4ef6\u3002"
        },
        "Employment": {
            "event description": "The event is related to employment.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u6b21\u6d3b\u52a8\u4e0e\u5c31\u4e1a\u6709\u5173\u3002"
        },
        "Emptying": {
            "event description": "The event is related to emptying.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6392\u7a7a\u6709\u5173\u3002"
        },
        "Escaping": {
            "event description": "The event is related to escaping.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8f6c\u4e49\u6709\u5173\u3002"
        },
        "Exchange": {
            "event description": "The event is related to exchange.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6362\u6709\u5173\u3002"
        },
        "Expansion": {
            "event description": "The event is related to expansion.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6269\u5bb9\u6709\u5173\u3002"
        },
        "Expend_resource": {
            "event description": "The event is related to expend resource.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6d88\u8017\u8d44\u6e90\u6709\u5173\u3002"
        },
        "Expressing_publicly": {
            "event description": "The event is related to expressing publicly.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u516c\u5f00\u8868\u8fbe\u6709\u5173\u3002"
        },
        "Extradition": {
            "event description": "The event is related to extradition.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5f15\u6e21\u6709\u5173\u3002"
        },
        "Filling": {
            "event description": "The event is related to filling.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u586b\u5145\u6709\u5173\u3002"
        },
        "Forming_relationships": {
            "event description": "The event is related to forming relationships.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5f62\u6210\u5173\u7cfb\u6709\u5173\u3002"
        },
        "GetReady": {
            "event description": "The event is related to getready.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u51c6\u5907\u6709\u5173\u3002"
        },
        "Getting": {
            "event description": "The event is related to getting.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5f97\u5230\u6709\u5173\u3002"
        },
        "GiveUp": {
            "event description": "The event is related to giveup.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u653e\u5f03\u6709\u5173\u3002"
        },
        "Giving": {
            "event description": "The event is related to giving.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u7ed9\u4e88\u6709\u5173\u3002"
        },
        "Having_or_lacking_access": {
            "event description": "The event is related to having or lacking access.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u62e5\u6709\u6216\u7f3a\u4e4f\u8bbf\u95ee\u6743\u9650\u6709\u5173\u3002"
        },
        "Hiding_objects": {
            "event description": "The event is related to hiding objects.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u9690\u85cf\u5bf9\u8c61\u6709\u5173\u3002"
        },
        "Hindering": {
            "event description": "The event is related to hindering.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u963b\u788d\u6709\u5173\u3002"
        },
        "Hold": {
            "event description": "The event is related to hold.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e3e\u884c\u6709\u5173\u3002"
        },
        "Hostile_encounter": {
            "event description": "The event is related to hostile encounter.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u654c\u5bf9\u906d\u9047\u6709\u5173\u3002"
        },
        "Imposing_obligation": {
            "event description": "The event is related to imposing obligation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5f3a\u52a0\u4e49\u52a1\u6709\u5173\u3002"
        },
        "Incident": {
            "event description": "The event is related to incident.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e8b\u4ef6\u76f8\u5173\u3002"
        },
        "Influence": {
            "event description": "The event is related to influence.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5f71\u54cd\u529b\u6709\u5173\u3002"
        },
        "Ingestion": {
            "event description": "The event is related to ingestion.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6444\u5165\u6709\u5173\u3002"
        },
        "Institutionalization": {
            "event description": "The event is related to institutionalization.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5236\u5ea6\u5316\u6709\u5173\u3002"
        },
        "Judgment_communication": {
            "event description": "The event is related to judgment communication.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5224\u65ad\u6c9f\u901a\u6709\u5173\u3002"
        },
        "Justifying": {
            "event description": "The event is related to justifying.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u8fa9\u62a4\u6709\u5173\u3002"
        },
        "Kidnapping": {
            "event description": "The event is related to kidnapping.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u7ed1\u67b6\u6709\u5173\u3002"
        },
        "Killing": {
            "event description": "The event is related to killing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u6740\u622e\u6709\u5173\u3002"
        },
        "Know": {
            "event description": "The event is related to know.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e86\u89e3\u6709\u5173\u3002"
        },
        "Labeling": {
            "event description": "The event is related to labeling.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6807\u7b7e\u6709\u5173\u3002"
        },
        "Legal_rulings": {
            "event description": "The event is related to legal rulings.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6cd5\u5f8b\u88c1\u51b3\u6709\u5173\u3002"
        },
        "Legality": {
            "event description": "The event is related to legality.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5408\u6cd5\u6027\u6709\u5173\u3002"
        },
        "Lighting": {
            "event description": "The event is related to lighting.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u7167\u660e\u6709\u5173\u3002"
        },
        "Limiting": {
            "event description": "The event is related to limiting.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u9650\u5236\u6709\u5173\u3002"
        },
        "Manufacturing": {
            "event description": "The event is related to manufacturing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5236\u9020\u4e1a\u6709\u5173\u3002"
        },
        "Military_operation": {
            "event description": "The event is related to military operation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u519b\u4e8b\u884c\u52a8\u6709\u5173\u3002"
        },
        "Motion": {
            "event description": "The event is related to motion.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\u3002"
        },
        "Motion_directional": {
            "event description": "The event is related to motion directional.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u65b9\u5411\u6709\u5173\u3002"
        },
        "Name_conferral": {
            "event description": "The event is related to name conferral.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u540d\u79f0\u6388\u4e88\u6709\u5173\u3002"
        },
        "Openness": {
            "event description": "The event is related to openness.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5f00\u653e\u6027\u6709\u5173\u3002"
        },
        "Participation": {
            "event description": "The event is related to participation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u53c2\u4e0e\u6709\u5173\u3002"
        },
        "Patrolling": {
            "event description": "The event is related to patrolling.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5de1\u903b\u6709\u5173\u3002"
        },
        "Perception_active": {
            "event description": "The event is related to perception active.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u77e5\u89c9\u6d3b\u52a8\u6709\u5173\u3002"
        },
        "Placing": {
            "event description": "The event is related to placing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "Practice": {
            "event description": "The event is related to practice.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5b9e\u8df5\u6709\u5173\u3002"
        },
        "Presence": {
            "event description": "The event is related to presence.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5728\u573a\u6709\u5173\u3002"
        },
        "Preserving": {
            "event description": "The event is related to preserving.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u4fdd\u5b58\u6709\u5173\u3002"
        },
        "Preventing_or_letting": {
            "event description": "The event is related to preventing or letting.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u9884\u9632\u6216\u51fa\u79df\u6709\u5173\u3002"
        },
        "Prison": {
            "event description": "The event is related to prison.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u76d1\u72f1\u6709\u5173\u3002"
        },
        "Process_end": {
            "event description": "The event is related to process end.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fdb\u7a0b\u7ed3\u675f\u76f8\u5173\u3002"
        },
        "Process_start": {
            "event description": "The event is related to process start.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fdb\u7a0b\u542f\u52a8\u76f8\u5173\u3002"
        },
        "Protest": {
            "event description": "The event is related to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6297\u8bae\u6709\u5173\u3002"
        },
        "Publishing": {
            "event description": "The event is related to publishing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u51fa\u7248\u6709\u5173\u3002"
        },
        "Quarreling": {
            "event description": "The event is related to quarreling.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4e89\u5435\u6709\u5173\u3002"
        },
        "Ratification": {
            "event description": "The event is related to ratification.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6279\u51c6\u6709\u5173\u3002"
        },
        "Receiving": {
            "event description": "The event is related to receiving.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u63a5\u6536\u76f8\u5173\u3002"
        },
        "Recording": {
            "event description": "The event is related to recording.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5f55\u97f3\u6709\u5173\u3002"
        },
        "Recovering": {
            "event description": "The event is related to recovering.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6062\u590d\u76f8\u5173\u3002"
        },
        "Reforming_a_system": {
            "event description": "The event is related to reforming a system.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4f53\u5236\u6539\u9769\u6709\u5173\u3002"
        },
        "Releasing": {
            "event description": "The event is related to releasing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u91ca\u653e\u76f8\u5173\u3002"
        },
        "Removing": {
            "event description": "The event is related to removing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u9664\u76f8\u5173\u3002"
        },
        "Renting": {
            "event description": "The event is related to renting.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u6b21\u6d3b\u52a8\u4e0e\u79df\u623f\u6709\u5173\u3002"
        },
        "Reporting": {
            "event description": "The event is related to reporting.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u62a5\u544a\u6709\u5173\u3002"
        },
        "Request": {
            "event description": "The event is related to request.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8bf7\u6c42\u76f8\u5173\u3002"
        },
        "Rescuing": {
            "event description": "The event is related to rescuing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6551\u63f4\u6709\u5173\u3002"
        },
        "Research": {
            "event description": "The event is related to research.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u7814\u7a76\u6709\u5173\u3002"
        },
        "Resolve_problem": {
            "event description": "The event is related to resolve problem.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u89e3\u51b3\u95ee\u9898\u6709\u5173\u3002"
        },
        "Response": {
            "event description": "The event is related to response.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u54cd\u5e94\u6709\u5173\u3002"
        },
        "Reveal_secret": {
            "event description": "The event is related to reveal secret.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6cc4\u9732\u79d8\u5bc6\u6709\u5173\u3002"
        },
        "Revenge": {
            "event description": "The event is related to revenge.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u590d\u4ec7\u6709\u5173\u3002"
        },
        "Rewards_and_punishments": {
            "event description": "The event is related to rewards and punishments.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u5956\u52b1\u548c\u60e9\u7f5a\u6709\u5173\u3002"
        },
        "Risk": {
            "event description": "The event is related to risk.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u98ce\u9669\u6709\u5173\u3002"
        },
        "Rite": {
            "event description": "The event is related to rite.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u4eea\u5f0f\u6709\u5173\u3002"
        },
        "Robbery": {
            "event description": "The event is related to robbery.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u62a2\u52ab\u6709\u5173\u3002"
        },
        "Scouring": {
            "event description": "The event is related to scouring.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u51b2\u5237\u6709\u5173\u3002"
        },
        "Scrutiny": {
            "event description": "The event is related to scrutiny.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5ba1\u67e5\u6709\u5173\u3002"
        },
        "Self_motion": {
            "event description": "The event is related to self motion.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u81ea\u6211\u8fd0\u52a8\u6709\u5173\u3002"
        },
        "Sending": {
            "event description": "The event is related to sending.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53d1\u9001\u76f8\u5173\u3002"
        },
        "Sign_agreement": {
            "event description": "The event is related to sign agreement.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u7b7e\u7f72\u534f\u8bae\u6709\u5173\u3002"
        },
        "Social_event": {
            "event description": "The event is related to social event.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u793e\u4f1a\u4e8b\u4ef6\u6709\u5173\u3002"
        },
        "Statement": {
            "event description": "The event is related to statement.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8bed\u53e5\u76f8\u5173\u3002"
        },
        "Submitting_documents": {
            "event description": "The event is related to submitting documents.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63d0\u4ea4\u6587\u4ef6\u6709\u5173\u3002"
        },
        "Supply": {
            "event description": "The event is related to supply.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4f9b\u5e94\u6709\u5173\u3002"
        },
        "Supporting": {
            "event description": "The event is related to supporting.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u652f\u6301\u6709\u5173\u3002"
        },
        "Surrendering": {
            "event description": "The event is related to surrendering.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6295\u964d\u6709\u5173\u3002"
        },
        "Surrounding": {
            "event description": "The event is related to surrounding.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5468\u56f4\u73af\u5883\u6709\u5173\u3002"
        },
        "Suspicion": {
            "event description": "The event is related to suspicion.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6000\u7591\u6709\u5173\u3002"
        },
        "Telling": {
            "event description": "The event is related to telling.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u8bb2\u8ff0\u6709\u5173\u3002"
        },
        "Temporary_stay": {
            "event description": "The event is related to temporary stay.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e34\u65f6\u505c\u7559\u6709\u5173\u3002"
        },
        "Terrorism": {
            "event description": "The event is related to terrorism.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6050\u6016\u4e3b\u4e49\u6709\u5173\u3002"
        },
        "Testing": {
            "event description": "The event is related to testing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6d4b\u8bd5\u6709\u5173\u3002"
        },
        "Theft": {
            "event description": "The event is related to theft.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u76d7\u7a83\u6709\u5173\u3002"
        },
        "Traveling": {
            "event description": "The event is related to traveling.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u65c5\u884c\u6709\u5173\u3002"
        },
        "Use_firearm": {
            "event description": "The event is related to use firearm.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4f7f\u7528\u67aa\u652f\u6709\u5173\u3002"
        },
        "Using": {
            "event description": "The event is related to using.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4f7f\u7528\u6709\u5173\u3002"
        },
        "Violence": {
            "event description": "The event is related to violence.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u66b4\u529b\u6709\u5173\u3002"
        },
        "Vocalizations": {
            "event description": "The event is related to vocalizations.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53d1\u58f0\u6709\u5173\u3002"
        },
        "Warning": {
            "event description": "The event is related to warning.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8b66\u544a\u76f8\u5173\u3002"
        },
        "Wearing": {
            "event description": "The event is related to wearing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u7a7f\u7740\u6709\u5173\u3002"
        },
        "Writing": {
            "event description": "The event is related to writing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5199\u4f5c\u6709\u5173\u3002"
        }
    },
    "geneva": {
        "Achieve": {
            "event type": "Achieve",
            "keywords": [],
            "event description": "The event is related to achieve.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Goal {ROLE_Goal} Means {ROLE_Means}.",
            "valid roles": [
                "Agent",
                "Goal",
                "Means"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5b9e\u73b0\u6709\u5173\u3002"
        },
        "Action": {
            "event type": "Action",
            "keywords": [],
            "event description": "The event is related to action.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Act {ROLE_Act} Agent {ROLE_Agent} Domain {ROLE_Domain} Manner {ROLE_Manner}.",
            "valid roles": [
                "Act",
                "Agent",
                "Domain",
                "Manner"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u884c\u52a8\u6709\u5173\u3002"
        },
        "Adducing": {
            "event type": "Adducing",
            "keywords": [],
            "event description": "The event is related to adducing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Medium {ROLE_Medium} Role {ROLE_Role} Speaker {ROLE_Speaker} Specified Entity {ROLE_Specified_entity}.",
            "valid roles": [
                "Medium",
                "Role",
                "Speaker",
                "Specified_entity"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5f15\u8bc1\u6709\u5173\u3002"
        },
        "Agree_or_refuse_to_act": {
            "event type": "Agree_or_refuse_to_act",
            "keywords": [],
            "event description": "The event is related to agree refuse act.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Proposed Action {ROLE_Proposed_action} Speaker {ROLE_Speaker}.",
            "valid roles": [
                "Proposed_action",
                "Speaker"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u540c\u610f\u62d2\u7edd\u884c\u4e3a\u6709\u5173\u3002"
        },
        "Arranging": {
            "event type": "Arranging",
            "keywords": [],
            "event description": "The event is related to arranging.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Configuration {ROLE_Configuration} Location {ROLE_Location} Theme {ROLE_Theme}.",
            "valid roles": [
                "Agent",
                "Configuration",
                "Location",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u5b89\u6392\u6709\u5173\u3002"
        },
        "Arrest": {
            "event type": "Arrest",
            "keywords": [],
            "event description": "The event is related to arrest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Authorities {ROLE_Authorities} Charges {ROLE_Charges} Offense {ROLE_Offense} Suspect {ROLE_Suspect}.",
            "valid roles": [
                "Authorities",
                "Charges",
                "Offense",
                "Suspect"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u902e\u6355\u6709\u5173\u3002"
        },
        "Arriving": {
            "event type": "Arriving",
            "keywords": [],
            "event description": "The event is related to arriving.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Goal {ROLE_Goal} Means {ROLE_Means} Path {ROLE_Path} Place {ROLE_Place} Purpose {ROLE_Purpose} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": [
                "Goal",
                "Means",
                "Path",
                "Place",
                "Purpose",
                "Source",
                "Theme"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5230\u8fbe\u6709\u5173\u3002"
        },
        "Assistance": {
            "event type": "Assistance",
            "keywords": [],
            "event description": "The event is related to assistance.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Benefited Party {ROLE_Benefited_party} Focal Entity {ROLE_Focal_entity} Goal {ROLE_Goal} Helper {ROLE_Helper} Means {ROLE_Means}.",
            "valid roles": [
                "Benefited_party",
                "Focal_entity",
                "Goal",
                "Helper",
                "Means"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63f4\u52a9\u6709\u5173\u3002"
        },
        "Attack": {
            "event type": "Attack",
            "keywords": [],
            "event description": "The event is related to attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Assailant {ROLE_Assailant} Means {ROLE_Means} Victim {ROLE_Victim} Weapon {ROLE_Weapon}.",
            "valid roles": [
                "Assailant",
                "Means",
                "Victim",
                "Weapon"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653b\u51fb\u6709\u5173\u3002"
        },
        "Bearing_arms": {
            "event type": "Bearing_arms",
            "keywords": [],
            "event description": "The event is related to bearing arms.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Protagonist {ROLE_Protagonist} Weapon {ROLE_Weapon}.",
            "valid roles": [
                "Protagonist",
                "Weapon"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8f74\u627f\u6b66\u5668\u6709\u5173\u3002"
        },
        "Becoming": {
            "event type": "Becoming",
            "keywords": [],
            "event description": "The event is related to becoming.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Entity {ROLE_Entity} Final Category {ROLE_Final_category} Final Quality {ROLE_Final_quality}.",
            "valid roles": [
                "Entity",
                "Final_category",
                "Final_quality"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6210\u4e3a\u6709\u5173\u3002"
        },
        "Becoming_a_member": {
            "event type": "Becoming_a_member",
            "keywords": [],
            "event description": "The event is related to becoming a member.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Group {ROLE_Group} New Member {ROLE_New_member}.",
            "valid roles": [
                "Group",
                "New_member"
            ],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u6210\u4e3a\u4f1a\u5458\u6709\u5173\u3002"
        },
        "Bodily_harm": {
            "event type": "Bodily_harm",
            "keywords": [],
            "event description": "The event is related to bodily harm.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Body Part {ROLE_Body_part} Cause {ROLE_Cause} Instrument {ROLE_Instrument} Victim {ROLE_Victim}.",
            "valid roles": [
                "Agent",
                "Body_part",
                "Cause",
                "Instrument",
                "Victim"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8eab\u4f53\u4f24\u5bb3\u6709\u5173\u3002"
        },
        "Bringing": {
            "event type": "Bringing",
            "keywords": [],
            "event description": "The event is related to bringing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Area {ROLE_Area} Carrier {ROLE_Carrier} Goal {ROLE_Goal} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": [
                "Agent",
                "Area",
                "Carrier",
                "Goal",
                "Source",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5e26\u6765\u6709\u5173\u3002"
        },
        "Building": {
            "event type": "Building",
            "keywords": [],
            "event description": "The event is related to building.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Components {ROLE_Components} Created Entity {ROLE_Created_entity} Place {ROLE_Place}.",
            "valid roles": [
                "Agent",
                "Components",
                "Created_entity",
                "Place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5efa\u7b51\u6709\u5173\u3002"
        },
        "Catastrophe": {
            "event type": "Catastrophe",
            "keywords": [],
            "event description": "The event is related to catastrophe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Patient {ROLE_Patient} Place {ROLE_Place} Undesirable Event {ROLE_Undesirable_event}.",
            "valid roles": [
                "Cause",
                "Patient",
                "Place",
                "Undesirable_event"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u707e\u96be\u6709\u5173\u3002"
        },
        "Causation": {
            "event type": "Causation",
            "keywords": [],
            "event description": "The event is related to causation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Actor {ROLE_Actor} Affected {ROLE_Affected} Cause {ROLE_Cause} Effect {ROLE_Effect} Means {ROLE_Means}.",
            "valid roles": [
                "Actor",
                "Affected",
                "Cause",
                "Effect",
                "Means"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u56e0\u679c\u5173\u7cfb\u6709\u5173\u3002"
        },
        "Cause_change_of_position_on_a_scale": {
            "event type": "Cause_change_of_position_on_a_scale",
            "keywords": [],
            "event description": "The event is related to cause change position on acale.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Attribute {ROLE_Attribute} Cause {ROLE_Cause} Difference {ROLE_Difference} Item {ROLE_Item} Value 1 {ROLE_Value_1} Value 2 {ROLE_Value_2}.",
            "valid roles": [
                "Agent",
                "Attribute",
                "Cause",
                "Difference",
                "Item",
                "Value_1",
                "Value_2"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5bfc\u81f4\u4f4d\u7f6e\u53d8\u5316\u6709\u5173\u3002"
        },
        "Cause_to_amalgamate": {
            "event type": "Cause_to_amalgamate",
            "keywords": [],
            "event description": "The event is related to cause amalgamate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Part 1 {ROLE_Part_1} Part 2 {ROLE_Part_2} Parts {ROLE_Parts} Whole {ROLE_Whole}.",
            "valid roles": [
                "Agent",
                "Part_1",
                "Part_2",
                "Parts",
                "Whole"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5f15\u8d77\u5408\u5e76\u6709\u5173\u3002"
        },
        "Cause_to_make_progress": {
            "event type": "Cause_to_make_progress",
            "keywords": [],
            "event description": "The event is related to cause make_ progress.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Project {ROLE_Project}.",
            "valid roles": [
                "Agent",
                "Project"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4e8b\u4e1a\u7684\u8fdb\u6b65\u6709\u5173\u3002"
        },
        "Change": {
            "event type": "Change",
            "keywords": [],
            "event description": "The event is related to change.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Attribute {ROLE_Attribute} Cause {ROLE_Cause} Entity {ROLE_Entity} Final Category {ROLE_Final_category} Final Value {ROLE_Final_value} Initial Category {ROLE_Initial_category}.",
            "valid roles": [
                "Agent",
                "Attribute",
                "Cause",
                "Entity",
                "Final_category",
                "Final_value",
                "Initial_category"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u53d8\u5316\u6709\u5173\u3002"
        },
        "Change_of_leadership": {
            "event type": "Change_of_leadership",
            "keywords": [],
            "event description": "The event is related to change leadership.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Body {ROLE_Body} New Leader {ROLE_New_leader} Old Leader {ROLE_Old_leader} Old Order {ROLE_Old_order} Role {ROLE_Role} Selector {ROLE_Selector}.",
            "valid roles": [
                "Body",
                "New_leader",
                "Old_leader",
                "Old_order",
                "Role",
                "Selector"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53d8\u9769\u9886\u5bfc\u6709\u5173\u3002"
        },
        "Check": {
            "event type": "Check",
            "keywords": [],
            "event description": "The event is related to check.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Inspector {ROLE_Inspector} Means {ROLE_Means} Unconfirmed Content {ROLE_Unconfirmed_content}.",
            "valid roles": [
                "Inspector",
                "Means",
                "Unconfirmed_content"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u68c0\u67e5\u76f8\u5173\u3002"
        },
        "Choosing": {
            "event type": "Choosing",
            "keywords": [],
            "event description": "The event is related to choosing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Chosen {ROLE_Chosen} Cognizer {ROLE_Cognizer} Possibilities {ROLE_Possibilities}.",
            "valid roles": [
                "Chosen",
                "Cognizer",
                "Possibilities"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u9009\u62e9\u6709\u5173\u3002"
        },
        "Collaboration": {
            "event type": "Collaboration",
            "keywords": [],
            "event description": "The event is related to collaboration.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Partners {ROLE_Partners} Undertaking {ROLE_Undertaking}.",
            "valid roles": [
                "Partners",
                "Undertaking"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u534f\u4f5c\u6709\u5173\u3002"
        },
        "Come_together": {
            "event type": "Come_together",
            "keywords": [],
            "event description": "The event is related to come together.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Configuration {ROLE_Configuration} Individuals {ROLE_Individuals} Place {ROLE_Place}.",
            "valid roles": [
                "Configuration",
                "Individuals",
                "Place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u662f\u6709\u5173\u8d70\u5230\u4e00\u8d77\u3002"
        },
        "Coming_to_be": {
            "event type": "Coming_to_be",
            "keywords": [],
            "event description": "The event is related to coming.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Components {ROLE_Components} Entity {ROLE_Entity} Place {ROLE_Place} Time {ROLE_Time}.",
            "valid roles": [
                "Components",
                "Entity",
                "Place",
                "Time"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5230\u6765\u6709\u5173\u3002"
        },
        "Coming_to_believe": {
            "event type": "Coming_to_believe",
            "keywords": [],
            "event description": "The event is related to coming believe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cognizer {ROLE_Cognizer} Content {ROLE_Content} Means {ROLE_Means}.",
            "valid roles": [
                "Cognizer",
                "Content",
                "Means"
            ],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u4fe1\u4ef0\u6709\u5173\u3002"
        },
        "Commerce_buy": {
            "event type": "Commerce_buy",
            "keywords": [],
            "event description": "The event is related to commerce buy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Buyer {ROLE_Buyer} Goods {ROLE_Goods} Seller {ROLE_Seller}.",
            "valid roles": [
                "Buyer",
                "Goods",
                "Seller"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5546\u4e1a\u8d2d\u4e70\u6709\u5173\u3002"
        },
        "Commerce_pay": {
            "event type": "Commerce_pay",
            "keywords": [],
            "event description": "The event is related to commerce pay.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Buyer {ROLE_Buyer} Goods {ROLE_Goods} Money {ROLE_Money} Seller {ROLE_Seller}.",
            "valid roles": [
                "Buyer",
                "Goods",
                "Money",
                "Seller"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5546\u4e1a\u652f\u4ed8\u6709\u5173\u3002"
        },
        "Commerce_sell": {
            "event type": "Commerce_sell",
            "keywords": [],
            "event description": "The event is related to commerce sell.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Buyer {ROLE_Buyer} Goods {ROLE_Goods} Money {ROLE_Money} Seller {ROLE_Seller}.",
            "valid roles": [
                "Buyer",
                "Goods",
                "Money",
                "Seller"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5546\u4e1a\u9500\u552e\u6709\u5173\u3002"
        },
        "Commitment": {
            "event type": "Commitment",
            "keywords": [],
            "event description": "The event is related to commitment.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Message {ROLE_Message} Speaker {ROLE_Speaker}.",
            "valid roles": [
                "Addressee",
                "Message",
                "Speaker"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u627f\u8bfa\u6709\u5173\u3002"
        },
        "Committing_crime": {
            "event type": "Committing_crime",
            "keywords": [],
            "event description": "The event is related to committing crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Crime {ROLE_Crime} Instrument {ROLE_Instrument} Perpetrator {ROLE_Perpetrator}.",
            "valid roles": [
                "Crime",
                "Instrument",
                "Perpetrator"
            ],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u72af\u7f6a\u6709\u5173\u3002"
        },
        "Communication": {
            "event type": "Communication",
            "keywords": [],
            "event description": "The event is related to communication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Interlocutors {ROLE_Interlocutors} Message {ROLE_Message} Speaker {ROLE_Speaker} Topic {ROLE_Topic} Trigger {ROLE_Trigger}.",
            "valid roles": [
                "Addressee",
                "Interlocutors",
                "Message",
                "Speaker",
                "Topic",
                "Trigger"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6c9f\u901a\u6709\u5173\u3002"
        },
        "Competition": {
            "event type": "Competition",
            "keywords": [],
            "event description": "The event is related to competition.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Competition {ROLE_Competition} Participants {ROLE_Participants} Venue {ROLE_Venue}.",
            "valid roles": [
                "Competition",
                "Participants",
                "Venue"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u7ade\u4e89\u6709\u5173\u3002"
        },
        "Confronting_problem": {
            "event type": "Confronting_problem",
            "keywords": [],
            "event description": "The event is related to confronting problem.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Activity {ROLE_Activity} Experiencer {ROLE_Experiencer}.",
            "valid roles": [
                "Activity",
                "Experiencer"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u9762\u5bf9\u95ee\u9898\u6709\u5173\u3002"
        },
        "Connect": {
            "event type": "Connect",
            "keywords": [],
            "event description": "The event is related to connect.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Figures {ROLE_Figures} Ground {ROLE_Ground}.",
            "valid roles": [
                "Figures",
                "Ground"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fde\u63a5\u76f8\u5173\u3002"
        },
        "Conquering": {
            "event type": "Conquering",
            "keywords": [],
            "event description": "The event is related to conquering.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Conqueror {ROLE_Conqueror} Means {ROLE_Means} Theme {ROLE_Theme}.",
            "valid roles": [
                "Conqueror",
                "Means",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5f81\u670d\u6709\u5173\u3002"
        },
        "Containing": {
            "event type": "Containing",
            "keywords": [],
            "event description": "The event is related to containing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Container {ROLE_Container} Contents {ROLE_Contents}.",
            "valid roles": [
                "Container",
                "Contents"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5305\u542b\u6709\u5173\u3002"
        },
        "Control": {
            "event type": "Control",
            "keywords": [],
            "event description": "The event is related to control.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Controlling Variable {ROLE_Controlling_variable} Dependent Variable {ROLE_Dependent_variable}.",
            "valid roles": [
                "Controlling_variable",
                "Dependent_variable"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a7\u5236\u6709\u5173\u3002"
        },
        "Convincing": {
            "event type": "Convincing",
            "keywords": [],
            "event description": "The event is related to convincing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Content {ROLE_Content} Speaker {ROLE_Speaker} Topic {ROLE_Topic}.",
            "valid roles": [
                "Addressee",
                "Content",
                "Speaker",
                "Topic"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8bf4\u670d\u6709\u5173\u3002"
        },
        "Cost": {
            "event type": "Cost",
            "keywords": [],
            "event description": "The event is related to cost.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Asset {ROLE_Asset} Goods {ROLE_Goods} Intended Event {ROLE_Intended_event} Payer {ROLE_Payer} Rate {ROLE_Rate}.",
            "valid roles": [
                "Asset",
                "Goods",
                "Intended_event",
                "Payer",
                "Rate"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6210\u672c\u6709\u5173\u3002"
        },
        "Create_artwork": {
            "event type": "Create_artwork",
            "keywords": [],
            "event description": "The event is related to create artwork.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Activity {ROLE_Activity} Culture {ROLE_Culture}.",
            "valid roles": [
                "Activity",
                "Culture"
            ],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u521b\u4f5c\u827a\u672f\u54c1\u6709\u5173\u3002"
        },
        "Creating": {
            "event type": "Creating",
            "keywords": [],
            "event description": "The event is related to creating.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Created Entity {ROLE_Created_entity} Creator {ROLE_Creator}.",
            "valid roles": [
                "Cause",
                "Created_entity",
                "Creator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u521b\u5efa\u76f8\u5173\u3002"
        },
        "Criminal_investigation": {
            "event type": "Criminal_investigation",
            "keywords": [],
            "event description": "The event is related to criminal investigation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Incident {ROLE_Incident} Investigator {ROLE_Investigator} Suspect {ROLE_Suspect}.",
            "valid roles": [
                "Incident",
                "Investigator",
                "Suspect"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5211\u4e8b\u8c03\u67e5\u6709\u5173\u3002"
        },
        "Cure": {
            "event type": "Cure",
            "keywords": [],
            "event description": "The event is related to cure.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Affliction {ROLE_Affliction} Medication {ROLE_Medication} Patient {ROLE_Patient} Treatment {ROLE_Treatment}.",
            "valid roles": [
                "Affliction",
                "Medication",
                "Patient",
                "Treatment"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6cbb\u7597\u6709\u5173\u3002"
        },
        "Damaging": {
            "event type": "Damaging",
            "keywords": [],
            "event description": "The event is related to damaging.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Patient {ROLE_Patient}.",
            "valid roles": [
                "Agent",
                "Cause",
                "Patient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7834\u574f\u6709\u5173\u3002"
        },
        "Death": {
            "event type": "Death",
            "keywords": [],
            "event description": "The event is related to death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Deceased {ROLE_Deceased}.",
            "valid roles": [
                "Deceased"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6b7b\u4ea1\u6709\u5173\u3002"
        },
        "Deciding": {
            "event type": "Deciding",
            "keywords": [],
            "event description": "The event is related to deciding.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cognizer {ROLE_Cognizer} Decision {ROLE_Decision}.",
            "valid roles": [
                "Cognizer",
                "Decision"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u51b3\u5b9a\u6709\u5173\u3002"
        },
        "Defending": {
            "event type": "Defending",
            "keywords": [],
            "event description": "The event is related to defending.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Assailant {ROLE_Assailant} Defender {ROLE_Defender} Instrument {ROLE_Instrument} Victim {ROLE_Victim}.",
            "valid roles": [
                "Assailant",
                "Defender",
                "Instrument",
                "Victim"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u9632\u5fa1\u6709\u5173\u3002"
        },
        "Departing": {
            "event type": "Departing",
            "keywords": [],
            "event description": "The event is related to departing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Goal {ROLE_Goal} Path {ROLE_Path} Source {ROLE_Source} Traveller {ROLE_Traveller}.",
            "valid roles": [
                "Goal",
                "Path",
                "Source",
                "Traveller"
            ],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u79bb\u522b\u6709\u5173\u3002"
        },
        "Destroying": {
            "event type": "Destroying",
            "keywords": [],
            "event description": "The event is related to destroying.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Destroyer {ROLE_Destroyer} Means {ROLE_Means} Patient {ROLE_Patient}.",
            "valid roles": [
                "Cause",
                "Destroyer",
                "Means",
                "Patient"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6bc1\u706d\u6709\u5173\u3002"
        },
        "Dispersal": {
            "event type": "Dispersal",
            "keywords": [],
            "event description": "The event is related to dispersal.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Goal Area {ROLE_Goal_area} Individuals {ROLE_Individuals}.",
            "valid roles": [
                "Agent",
                "Cause",
                "Goal_area",
                "Individuals"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6269\u6563\u6709\u5173\u3002"
        },
        "Earnings_and_losses": {
            "event type": "Earnings_and_losses",
            "keywords": [],
            "event description": "The event is related to earnings losses.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Earner {ROLE_Earner} Earnings {ROLE_Earnings} Goods {ROLE_Goods}.",
            "valid roles": [
                "Earner",
                "Earnings",
                "Goods"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6536\u5165\u635f\u5931\u6709\u5173\u3002"
        },
        "Education_teaching": {
            "event type": "Education_teaching",
            "keywords": [],
            "event description": "The event is related to education teaching.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Course {ROLE_Course} Fact {ROLE_Fact} Role {ROLE_Role} Skill {ROLE_Skill} Student {ROLE_Student} Subject {ROLE_Subject} Teacher {ROLE_Teacher}.",
            "valid roles": [
                "Course",
                "Fact",
                "Role",
                "Skill",
                "Student",
                "Subject",
                "Teacher"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6559\u80b2\u6559\u5b66\u6709\u5173\u3002"
        },
        "Emergency": {
            "event type": "Emergency",
            "keywords": [],
            "event description": "The event is related to emergency.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Place {ROLE_Place} Undesirable Event {ROLE_Undesirable_event}.",
            "valid roles": [
                "Place",
                "Undesirable_event"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u5c5e\u4e8e\u7d27\u6025\u4e8b\u4ef6\u3002"
        },
        "Employment": {
            "event type": "Employment",
            "keywords": [],
            "event description": "The event is related to employment.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Employee {ROLE_Employee} Employer {ROLE_Employer} Field {ROLE_Field} Place Of Employment {ROLE_Place_of_employment} Position {ROLE_Position} Task {ROLE_Task} Type {ROLE_Type}.",
            "valid roles": [
                "Employee",
                "Employer",
                "Field",
                "Place_of_employment",
                "Position",
                "Task",
                "Type"
            ],
            "chinese event description": "\u8fd9\u6b21\u6d3b\u52a8\u4e0e\u5c31\u4e1a\u6709\u5173\u3002"
        },
        "Emptying": {
            "event type": "Emptying",
            "keywords": [],
            "event description": "The event is related to emptying.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": [
                "Agent",
                "Cause",
                "Source",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6392\u7a7a\u6709\u5173\u3002"
        },
        "Exchange": {
            "event type": "Exchange",
            "keywords": [],
            "event description": "The event is related to exchange.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Exchanger 1 {ROLE_Exchanger_1} Exchanger 2 {ROLE_Exchanger_2} Exchangers {ROLE_Exchangers} Theme 1 {ROLE_Theme_1} Theme 2 {ROLE_Theme_2} Themes {ROLE_Themes}.",
            "valid roles": [
                "Exchanger_1",
                "Exchanger_2",
                "Exchangers",
                "Theme_1",
                "Theme_2",
                "Themes"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6362\u6709\u5173\u3002"
        },
        "Expansion": {
            "event type": "Expansion",
            "keywords": [],
            "event description": "The event is related to expansion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Dimension {ROLE_Dimension} Initial Size {ROLE_Initial_size} Item {ROLE_Item} Result Size {ROLE_Result_size}.",
            "valid roles": [
                "Agent",
                "Dimension",
                "Initial_size",
                "Item",
                "Result_size"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6269\u5bb9\u6709\u5173\u3002"
        },
        "Filling": {
            "event type": "Filling",
            "keywords": [],
            "event description": "The event is related to filling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Goal {ROLE_Goal} Theme {ROLE_Theme}.",
            "valid roles": [
                "Agent",
                "Cause",
                "Goal",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u586b\u5145\u6709\u5173\u3002"
        },
        "GetReady": {
            "event type": "GetReady",
            "keywords": [],
            "event description": "The event is related to getready.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Activity {ROLE_Activity} Protagonist {ROLE_Protagonist}.",
            "valid roles": [
                "Activity",
                "Protagonist"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u51c6\u5907\u6709\u5173\u3002"
        },
        "Getting": {
            "event type": "Getting",
            "keywords": [],
            "event description": "The event is related to getting.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Means {ROLE_Means} Recipient {ROLE_Recipient} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": [
                "Means",
                "Recipient",
                "Source",
                "Theme"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5f97\u5230\u6709\u5173\u3002"
        },
        "Giving": {
            "event type": "Giving",
            "keywords": [],
            "event description": "The event is related to giving.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Offerer {ROLE_Offerer} Recipient {ROLE_Recipient} Theme {ROLE_Theme}.",
            "valid roles": [
                "Offerer",
                "Recipient",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u7ed9\u4e88\u6709\u5173\u3002"
        },
        "Hindering": {
            "event type": "Hindering",
            "keywords": [],
            "event description": "The event is related to hindering.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Action {ROLE_Action} Hindrance {ROLE_Hindrance} Protagonist {ROLE_Protagonist}.",
            "valid roles": [
                "Action",
                "Hindrance",
                "Protagonist"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u963b\u788d\u6709\u5173\u3002"
        },
        "Hold": {
            "event type": "Hold",
            "keywords": [],
            "event description": "The event is related to hold.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Entity {ROLE_Entity} Manipulator {ROLE_Manipulator}.",
            "valid roles": [
                "Entity",
                "Manipulator"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e3e\u884c\u6709\u5173\u3002"
        },
        "Hostile_encounter": {
            "event type": "Hostile_encounter",
            "keywords": [],
            "event description": "The event is related to hostile encounter.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Instrument {ROLE_Instrument} Issue {ROLE_Issue} Purpose {ROLE_Purpose} Side 1 {ROLE_Side_1} Side 2 {ROLE_Side_2} Sides {ROLE_Sides}.",
            "valid roles": [
                "Instrument",
                "Issue",
                "Purpose",
                "Side_1",
                "Side_2",
                "Sides"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u654c\u5bf9\u906d\u9047\u6709\u5173\u3002"
        },
        "Influence": {
            "event type": "Influence",
            "keywords": [],
            "event description": "The event is related to influence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Action {ROLE_Action} Agent {ROLE_Agent} Behavior {ROLE_Behavior} Cognizer {ROLE_Cognizer} Product {ROLE_Product} Situation {ROLE_Situation}.",
            "valid roles": [
                "Action",
                "Agent",
                "Behavior",
                "Cognizer",
                "Product",
                "Situation"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5f71\u54cd\u529b\u6709\u5173\u3002"
        },
        "Ingestion": {
            "event type": "Ingestion",
            "keywords": [],
            "event description": "The event is related to ingestion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Ingestibles {ROLE_Ingestibles} Ingestor {ROLE_Ingestor}.",
            "valid roles": [
                "Ingestibles",
                "Ingestor"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6444\u5165\u6709\u5173\u3002"
        },
        "Judgment_communication": {
            "event type": "Judgment_communication",
            "keywords": [],
            "event description": "The event is related to judgment communication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Communicator {ROLE_Communicator} Evaluee {ROLE_Evaluee} Medium {ROLE_Medium} Reason {ROLE_Reason} Topic {ROLE_Topic}.",
            "valid roles": [
                "Addressee",
                "Communicator",
                "Evaluee",
                "Medium",
                "Reason",
                "Topic"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5224\u65ad\u6c9f\u901a\u6709\u5173\u3002"
        },
        "Killing": {
            "event type": "Killing",
            "keywords": [],
            "event description": "The event is related to killing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Instrument {ROLE_Instrument} Killer {ROLE_Killer} Means {ROLE_Means} Victim {ROLE_Victim}.",
            "valid roles": [
                "Cause",
                "Instrument",
                "Killer",
                "Means",
                "Victim"
            ],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u6740\u622e\u6709\u5173\u3002"
        },
        "Know": {
            "event type": "Know",
            "keywords": [],
            "event description": "The event is related to know.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cognizer {ROLE_Cognizer} Evidence {ROLE_Evidence} Instrument {ROLE_Instrument} Means {ROLE_Means} Phenomenon {ROLE_Phenomenon} Topic {ROLE_Topic}.",
            "valid roles": [
                "Cognizer",
                "Evidence",
                "Instrument",
                "Means",
                "Phenomenon",
                "Topic"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e86\u89e3\u6709\u5173\u3002"
        },
        "Labeling": {
            "event type": "Labeling",
            "keywords": [],
            "event description": "The event is related to labeling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Entity {ROLE_Entity} Label {ROLE_Label} Speaker {ROLE_Speaker}.",
            "valid roles": [
                "Entity",
                "Label",
                "Speaker"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6807\u7b7e\u6709\u5173\u3002"
        },
        "Legality": {
            "event type": "Legality",
            "keywords": [],
            "event description": "The event is related to legality.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Action {ROLE_Action} Object {ROLE_Object}.",
            "valid roles": [
                "Action",
                "Object"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5408\u6cd5\u6027\u6709\u5173\u3002"
        },
        "Manufacturing": {
            "event type": "Manufacturing",
            "keywords": [],
            "event description": "The event is related to manufacturing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Factory {ROLE_Factory} Instrument {ROLE_Instrument} Producer {ROLE_Producer} Product {ROLE_Product} Resource {ROLE_Resource}.",
            "valid roles": [
                "Factory",
                "Instrument",
                "Producer",
                "Product",
                "Resource"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5236\u9020\u4e1a\u6709\u5173\u3002"
        },
        "Motion": {
            "event type": "Motion",
            "keywords": [],
            "event description": "The event is related to motion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Area {ROLE_Area} Cause {ROLE_Cause} Distance {ROLE_Distance} Goal {ROLE_Goal} Means {ROLE_Means} Path {ROLE_Path} Source {ROLE_Source} Speed {ROLE_Speed} Theme {ROLE_Theme}.",
            "valid roles": [
                "Agent",
                "Area",
                "Cause",
                "Distance",
                "Goal",
                "Means",
                "Path",
                "Source",
                "Speed",
                "Theme"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\u3002"
        },
        "Motion_directional": {
            "event type": "Motion_directional",
            "keywords": [],
            "event description": "The event is related to motion directional.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Area {ROLE_Area} Direction {ROLE_Direction} Goal {ROLE_Goal} Path {ROLE_Path} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": [
                "Area",
                "Direction",
                "Goal",
                "Path",
                "Source",
                "Theme"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u65b9\u5411\u6709\u5173\u3002"
        },
        "Openness": {
            "event type": "Openness",
            "keywords": [],
            "event description": "The event is related to openness.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Barrier {ROLE_Barrier} Theme {ROLE_Theme} Useful Location {ROLE_Useful_location}.",
            "valid roles": [
                "Barrier",
                "Theme",
                "Useful_location"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5f00\u653e\u6027\u6709\u5173\u3002"
        },
        "Participation": {
            "event type": "Participation",
            "keywords": [],
            "event description": "The event is related to participation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Event {ROLE_Event} Participants {ROLE_Participants}.",
            "valid roles": [
                "Event",
                "Participants"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u53c2\u4e0e\u6709\u5173\u3002"
        },
        "Perception_active": {
            "event type": "Perception_active",
            "keywords": [],
            "event description": "The event is related to perception active.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Direction {ROLE_Direction} Perceiver Agentive {ROLE_Perceiver_agentive} Phenomenon {ROLE_Phenomenon}.",
            "valid roles": [
                "Direction",
                "Perceiver_agentive",
                "Phenomenon"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u77e5\u89c9\u6d3b\u52a8\u6709\u5173\u3002"
        },
        "Placing": {
            "event type": "Placing",
            "keywords": [],
            "event description": "The event is related to placing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Location {ROLE_Location} Theme {ROLE_Theme}.",
            "valid roles": [
                "Agent",
                "Cause",
                "Location",
                "Theme"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "Practice": {
            "event type": "Practice",
            "keywords": [],
            "event description": "The event is related to practice.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Action {ROLE_Action} Agent {ROLE_Agent} Occasion {ROLE_Occasion}.",
            "valid roles": [
                "Action",
                "Agent",
                "Occasion"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5b9e\u8df5\u6709\u5173\u3002"
        },
        "Presence": {
            "event type": "Presence",
            "keywords": [],
            "event description": "The event is related to presence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Circumstances {ROLE_Circumstances} Duration {ROLE_Duration} Entity {ROLE_Entity} Inherent Purpose {ROLE_Inherent_purpose} Place {ROLE_Place} Time {ROLE_Time}.",
            "valid roles": [
                "Circumstances",
                "Duration",
                "Entity",
                "Inherent_purpose",
                "Place",
                "Time"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u5728\u573a\u6709\u5173\u3002"
        },
        "Preventing_or_letting": {
            "event type": "Preventing_or_letting",
            "keywords": [],
            "event description": "The event is related to preventing letting.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Event {ROLE_Event} Means {ROLE_Means} Potential Hindrance {ROLE_Potential_hindrance}.",
            "valid roles": [
                "Agent",
                "Event",
                "Means",
                "Potential_hindrance"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u9632\u6b62\u51fa\u79df\u6709\u5173\u3002"
        },
        "Process_end": {
            "event type": "Process_end",
            "keywords": [],
            "event description": "The event is related to process end.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Final Subevent {ROLE_Final_subevent} Process {ROLE_Process} State {ROLE_State} Time {ROLE_Time}.",
            "valid roles": [
                "Agent",
                "Cause",
                "Final_subevent",
                "Process",
                "State",
                "Time"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fdb\u7a0b\u7ed3\u675f\u76f8\u5173\u3002"
        },
        "Process_start": {
            "event type": "Process_start",
            "keywords": [],
            "event description": "The event is related to process start.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Event {ROLE_Event} Initial Subevent {ROLE_Initial_subevent} Time {ROLE_Time}.",
            "valid roles": [
                "Agent",
                "Event",
                "Initial_subevent",
                "Time"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fdb\u7a0b\u542f\u52a8\u76f8\u5173\u3002"
        },
        "Protest": {
            "event type": "Protest",
            "keywords": [],
            "event description": "The event is related to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Arguer {ROLE_Arguer} Content {ROLE_Content}.",
            "valid roles": [
                "Addressee",
                "Arguer",
                "Content"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6297\u8bae\u6709\u5173\u3002"
        },
        "Quarreling": {
            "event type": "Quarreling",
            "keywords": [],
            "event description": "The event is related to quarreling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Arguer2 {ROLE_Arguer2} Arguers {ROLE_Arguers} Issue {ROLE_Issue}.",
            "valid roles": [
                "Arguer2",
                "Arguers",
                "Issue"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4e89\u5435\u6709\u5173\u3002"
        },
        "Ratification": {
            "event type": "Ratification",
            "keywords": [],
            "event description": "The event is related to ratification.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Proposal {ROLE_Proposal} Ratifier {ROLE_Ratifier}.",
            "valid roles": [
                "Proposal",
                "Ratifier"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6279\u51c6\u6709\u5173\u3002"
        },
        "Receiving": {
            "event type": "Receiving",
            "keywords": [],
            "event description": "The event is related to receiving.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Donor {ROLE_Donor} Recipient {ROLE_Recipient} Theme {ROLE_Theme}.",
            "valid roles": [
                "Donor",
                "Recipient",
                "Theme"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u63a5\u6536\u76f8\u5173\u3002"
        },
        "Recovering": {
            "event type": "Recovering",
            "keywords": [],
            "event description": "The event is related to recovering.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Entity {ROLE_Entity} Means {ROLE_Means}.",
            "valid roles": [
                "Agent",
                "Entity",
                "Means"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6062\u590d\u76f8\u5173\u3002"
        },
        "Removing": {
            "event type": "Removing",
            "keywords": [],
            "event description": "The event is related to removing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Goal {ROLE_Goal} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": [
                "Agent",
                "Cause",
                "Goal",
                "Source",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u9664\u76f8\u5173\u3002"
        },
        "Request": {
            "event type": "Request",
            "keywords": [],
            "event description": "The event is related to request.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Medium {ROLE_Medium} Message {ROLE_Message} Speaker {ROLE_Speaker}.",
            "valid roles": [
                "Addressee",
                "Medium",
                "Message",
                "Speaker"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8bf7\u6c42\u76f8\u5173\u3002"
        },
        "Research": {
            "event type": "Research",
            "keywords": [],
            "event description": "The event is related to research.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Field {ROLE_Field} Researcher {ROLE_Researcher} Topic {ROLE_Topic}.",
            "valid roles": [
                "Field",
                "Researcher",
                "Topic"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u7814\u7a76\u6709\u5173\u3002"
        },
        "Resolve_problem": {
            "event type": "Resolve_problem",
            "keywords": [],
            "event description": "The event is related to resolve problem.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Means {ROLE_Means} Problem {ROLE_Problem}.",
            "valid roles": [
                "Agent",
                "Cause",
                "Means",
                "Problem"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u89e3\u51b3\u95ee\u9898\u6709\u5173\u3002"
        },
        "Response": {
            "event type": "Response",
            "keywords": [],
            "event description": "The event is related to response.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Responding Entity {ROLE_Responding_entity} Response {ROLE_Response} Trigger {ROLE_Trigger}.",
            "valid roles": [
                "Agent",
                "Responding_entity",
                "Response",
                "Trigger"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u54cd\u5e94\u6709\u5173\u3002"
        },
        "Reveal_secret": {
            "event type": "Reveal_secret",
            "keywords": [],
            "event description": "The event is related to reveal secret.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Information {ROLE_Information} Speaker {ROLE_Speaker} Topic {ROLE_Topic}.",
            "valid roles": [
                "Addressee",
                "Information",
                "Speaker",
                "Topic"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6cc4\u9732\u79d8\u5bc6\u6709\u5173\u3002"
        },
        "Revenge": {
            "event type": "Revenge",
            "keywords": [],
            "event description": "The event is related to revenge.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Avenger {ROLE_Avenger} Injured Party {ROLE_Injured_party} Injury {ROLE_Injury} Offender {ROLE_Offender} Punishment {ROLE_Punishment}.",
            "valid roles": [
                "Avenger",
                "Injured_party",
                "Injury",
                "Offender",
                "Punishment"
            ],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u590d\u4ec7\u6709\u5173\u3002"
        },
        "Rite": {
            "event type": "Rite",
            "keywords": [],
            "event description": "The event is related to rite.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Member {ROLE_Member} Object {ROLE_Object} Type {ROLE_Type}.",
            "valid roles": [
                "Member",
                "Object",
                "Type"
            ],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u4eea\u5f0f\u6709\u5173\u3002"
        },
        "Scrutiny": {
            "event type": "Scrutiny",
            "keywords": [],
            "event description": "The event is related to scrutiny.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cognizer {ROLE_Cognizer} Ground {ROLE_Ground} Instrument {ROLE_Instrument} Phenomenon {ROLE_Phenomenon} Unwanted Entity {ROLE_Unwanted_entity}.",
            "valid roles": [
                "Cognizer",
                "Ground",
                "Instrument",
                "Phenomenon",
                "Unwanted_entity"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5ba1\u67e5\u6709\u5173\u3002"
        },
        "Self_motion": {
            "event type": "Self_motion",
            "keywords": [],
            "event description": "The event is related to self motion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Direction {ROLE_Direction} Distance {ROLE_Distance} Goal {ROLE_Goal} Path {ROLE_Path} Self Mover {ROLE_Self_mover} Source {ROLE_Source}.",
            "valid roles": [
                "Direction",
                "Distance",
                "Goal",
                "Path",
                "Self_mover",
                "Source"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u81ea\u6211\u8fd0\u52a8\u6709\u5173\u3002"
        },
        "Sending": {
            "event type": "Sending",
            "keywords": [],
            "event description": "The event is related to sending.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Goal {ROLE_Goal} Means {ROLE_Means} Recipient {ROLE_Recipient} Sender {ROLE_Sender} Source {ROLE_Source} Theme {ROLE_Theme} Transferors {ROLE_Transferors} Vehicle {ROLE_Vehicle}.",
            "valid roles": [
                "Goal",
                "Means",
                "Recipient",
                "Sender",
                "Source",
                "Theme",
                "Transferors",
                "Vehicle"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53d1\u9001\u76f8\u5173\u3002"
        },
        "Sign_agreement": {
            "event type": "Sign_agreement",
            "keywords": [],
            "event description": "The event is related to sign agreement.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agreement {ROLE_Agreement} Signatory {ROLE_Signatory}.",
            "valid roles": [
                "Agreement",
                "Signatory"
            ],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u7b7e\u7f72\u534f\u8bae\u6709\u5173\u3002"
        },
        "Social_event": {
            "event type": "Social_event",
            "keywords": [],
            "event description": "The event is related to social event.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Attendees {ROLE_Attendees} Beneficiary {ROLE_Beneficiary} Host {ROLE_Host} Occasion {ROLE_Occasion} Social Event {ROLE_Social_event}.",
            "valid roles": [
                "Attendees",
                "Beneficiary",
                "Host",
                "Occasion",
                "Social_event"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u793e\u4f1a\u4e8b\u4ef6\u6709\u5173\u3002"
        },
        "Statement": {
            "event type": "Statement",
            "keywords": [],
            "event description": "The event is related to statement.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Medium {ROLE_Medium} Message {ROLE_Message} Speaker {ROLE_Speaker}.",
            "valid roles": [
                "Addressee",
                "Medium",
                "Message",
                "Speaker"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8bed\u53e5\u76f8\u5173\u3002"
        },
        "Supply": {
            "event type": "Supply",
            "keywords": [],
            "event description": "The event is related to supply.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Imposed Purpose {ROLE_Imposed_purpose} Recipient {ROLE_Recipient} Supplier {ROLE_Supplier} Theme {ROLE_Theme}.",
            "valid roles": [
                "Imposed_purpose",
                "Recipient",
                "Supplier",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4f9b\u5e94\u6709\u5173\u3002"
        },
        "Supporting": {
            "event type": "Supporting",
            "keywords": [],
            "event description": "The event is related to supporting.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Supported {ROLE_Supported} Supporter {ROLE_Supporter}.",
            "valid roles": [
                "Supported",
                "Supporter"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u652f\u6301\u6709\u5173\u3002"
        },
        "Telling": {
            "event type": "Telling",
            "keywords": [],
            "event description": "The event is related to telling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Message {ROLE_Message} Speaker {ROLE_Speaker}.",
            "valid roles": [
                "Addressee",
                "Message",
                "Speaker"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u8bb2\u8ff0\u6709\u5173\u3002"
        },
        "Terrorism": {
            "event type": "Terrorism",
            "keywords": [],
            "event description": "The event is related to terrorism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Act {ROLE_Act} Instrument {ROLE_Instrument} Terrorist {ROLE_Terrorist} Victim {ROLE_Victim}.",
            "valid roles": [
                "Act",
                "Instrument",
                "Terrorist",
                "Victim"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6050\u6016\u4e3b\u4e49\u6709\u5173\u3002"
        },
        "Testing": {
            "event type": "Testing",
            "keywords": [],
            "event description": "The event is related to testing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Circumstances {ROLE_Circumstances} Means {ROLE_Means} Product {ROLE_Product} Result {ROLE_Result} Tested Property {ROLE_Tested_property} Tester {ROLE_Tester}.",
            "valid roles": [
                "Circumstances",
                "Means",
                "Product",
                "Result",
                "Tested_property",
                "Tester"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6d4b\u8bd5\u6709\u5173\u3002"
        },
        "Theft": {
            "event type": "Theft",
            "keywords": [],
            "event description": "The event is related to theft.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Goods {ROLE_Goods} Instrument {ROLE_Instrument} Means {ROLE_Means} Perpetrator {ROLE_Perpetrator} Source {ROLE_Source} Victim {ROLE_Victim}.",
            "valid roles": [
                "Goods",
                "Instrument",
                "Means",
                "Perpetrator",
                "Source",
                "Victim"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u76d7\u7a83\u6709\u5173\u3002"
        },
        "Traveling": {
            "event type": "Traveling",
            "keywords": [],
            "event description": "The event is related to traveling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Area {ROLE_Area} Distance {ROLE_Distance} Entity {ROLE_Entity} Goal {ROLE_Goal} Means {ROLE_Means} Path {ROLE_Path} Purpose {ROLE_Purpose} Traveler {ROLE_Traveler}.",
            "valid roles": [
                "Area",
                "Distance",
                "Entity",
                "Goal",
                "Means",
                "Path",
                "Purpose",
                "Traveler"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u65c5\u884c\u6709\u5173\u3002"
        },
        "Using": {
            "event type": "Using",
            "keywords": [],
            "event description": "The event is related to using.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Instrument {ROLE_Instrument} Means {ROLE_Means} Purpose {ROLE_Purpose}.",
            "valid roles": [
                "Agent",
                "Instrument",
                "Means",
                "Purpose"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4f7f\u7528\u6709\u5173\u3002"
        },
        "Wearing": {
            "event type": "Wearing",
            "keywords": [],
            "event description": "The event is related to wearing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Body Location {ROLE_Body_location} Clothing {ROLE_Clothing} Wearer {ROLE_Wearer}.",
            "valid roles": [
                "Body_location",
                "Clothing",
                "Wearer"
            ],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u7a7f\u7740\u6709\u5173\u3002"
        },
        "Writing": {
            "event type": "Writing",
            "keywords": [],
            "event description": "The event is related to writing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Author {ROLE_Author} Instrument {ROLE_Instrument} Text {ROLE_Text}.",
            "valid roles": [
                "Addressee",
                "Author",
                "Instrument",
                "Text"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u5199\u4f5c\u6709\u5173\u3002"
        }
    },
    "mee-en": {
        "Business_START-ORG": {
            "event description": "The event is related to business start organization.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u521b\u4e1a\u7ec4\u7ec7\u6709\u5173\u3002"
        },
        "Conflict_Attack": {
            "event description": "The event is related to conflict attack.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u6709\u5173\u3002"
        },
        "Conflict_Demonstrate": {
            "event description": "The event is related to conflict demonstrate.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u793a\u5a01\u6709\u5173\u3002"
        },
        "Contact_Meet": {
            "event description": "The event is related to contact meet.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u4f1a\u8bae\u6709\u5173\u3002"
        },
        "Contact_Phone-Write": {
            "event description": "The event is related to contact phone write.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u7535\u8bdd\u5199\u6709\u5173\u3002"
        },
        "Justice_Arrest-Jail": {
            "event description": "The event is related to justice arrest jail.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u902e\u6355\u76d1\u72f1\u6709\u5173\u3002"
        },
        "Life_Be-Born": {
            "event description": "The event is related to life born.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u751f\u547d\u7684\u8bde\u751f\u6709\u5173\u3002"
        },
        "Life_Die": {
            "event description": "The event is related to life die.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u751f\u547d\u6b7b\u4ea1\u6709\u5173\u3002"
        },
        "Life_Divorce": {
            "event description": "The event is related to life divorce.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u751f\u6d3b\u79bb\u5a5a\u6709\u5173\u3002"
        },
        "Life_Injure": {
            "event description": "The event is related to life injure.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u6d89\u53ca\u4eba\u8eab\u4f24\u5bb3\u3002"
        },
        "Life_Marry": {
            "event description": "The event is related to life marry.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u5173\u7cfb\u5230\u7ed3\u5a5a\u7684\u4e00\u751f\u3002"
        },
        "Movement_Transport": {
            "event description": "The event is related to movement transport.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u4f20\u8f93\u6709\u5173\u3002"
        },
        "Personnel_End-Position": {
            "event description": "The event is related to personnel end position.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u672b\u7aef\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "Personnel_Start-Position": {
            "event description": "The event is related to personnel start position.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u542f\u52a8\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "Transaction_Transfer-Money": {
            "event description": "The event is related to transaction transfer-money.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8f6c\u8d26\u4ea4\u6613\u6709\u5173\u3002"
        },
        "Transaction_Transfer-Ownership": {
            "event description": "The event is related to transaction transfer ownership.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u8f6c\u79fb\u6240\u6709\u6743\u6709\u5173\u3002"
        }
    },
    "rams": {
        "artifactexistence.damagedestroy.damage": {
            "event type": "artifactexistence.damagedestroy.damage",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy damage.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_damager} damaged {ROLE_artifact} using {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": [
                "damager",
                "artifact",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u795e\u5668\u5b58\u5728\u4f24\u5bb3\u7834\u574f\u4f24\u5bb3\u6709\u5173\u3002"
        },
        "artifactexistence.damagedestroy.destroy": {
            "event type": "artifactexistence.damagedestroy.destroy",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy destroy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_destroyer} destroyed {ROLE_artifact} using {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": [
                "destroyer",
                "artifact",
                "instrument",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u795e\u5668\u5b58\u5728\u6709\u5173\u4f24\u5bb3\u6467\u6bc1\u6467\u6bc1\u3002"
        },
        "artifactexistence.damagedestroy.n/a": {
            "event type": "artifactexistence.damagedestroy.n/a",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_damagerdestroyer} damaged or destroyed {ROLE_artifact} using {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": [
                "damagerdestroyer",
                "artifact",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u795e\u5668\u5b58\u5728\u3001\u4f24\u5bb3\u548c\u6bc1\u706d\u6709\u5173\u3002"
        },
        "conflict.attack.airstrikemissilestrike": {
            "event type": "conflict.attack.airstrikemissilestrike",
            "keywords": [],
            "event description": "The event is related to conflict attack airstrike missile strike.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u88ad\u51fb\u3001\u7a7a\u88ad\u3001\u5bfc\u5f39\u88ad\u51fb\u6709\u5173\u3002"
        },
        "conflict.attack.biologicalchemicalpoisonattack": {
            "event type": "conflict.attack.biologicalchemicalpoisonattack",
            "keywords": [],
            "event description": "The event is related to conflict attack biological chemical poison attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u751f\u7269\u5316\u5b66\u6bd2\u5242\u653b\u51fb\u6709\u5173\u3002"
        },
        "conflict.attack.bombing": {
            "event type": "conflict.attack.bombing",
            "keywords": [],
            "event description": "The event is related to conflict attack bombing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u88ad\u51fb\u7206\u70b8\u6709\u5173\u3002"
        },
        "conflict.attack.firearmattack": {
            "event type": "conflict.attack.firearmattack",
            "keywords": [],
            "event description": "The event is related to conflict attack firearm attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u88ad\u51fb\u548c\u67aa\u652f\u88ad\u51fb\u6709\u5173\u3002"
        },
        "conflict.attack.hanging": {
            "event type": "conflict.attack.hanging",
            "keywords": [],
            "event description": "The event is related to conflict attack hanging.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u60ac\u6302\u6709\u5173\u3002"
        },
        "conflict.attack.invade": {
            "event type": "conflict.attack.invade",
            "keywords": [],
            "event description": "The event is related to conflict attack invade.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u5165\u4fb5\u6709\u5173\u3002"
        },
        "conflict.attack.n/a": {
            "event type": "conflict.attack.n/a",
            "keywords": [],
            "event description": "The event is related to conflict attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u6709\u5173\u3002"
        },
        "conflict.attack.selfdirectedbattle": {
            "event type": "conflict.attack.selfdirectedbattle",
            "keywords": [],
            "event description": "The event is related to conflict attack self directed battle.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u662f\u4e0e\u51b2\u7a81\u653b\u51fb\u6709\u5173\u7684\u81ea\u4e3b\u6218\u6597\u3002"
        },
        "conflict.attack.setfire": {
            "event type": "conflict.attack.setfire",
            "keywords": [],
            "event description": "The event is related to conflict attack setfire.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u7eb5\u706b\u6709\u5173\u3002"
        },
        "conflict.attack.stabbing": {
            "event type": "conflict.attack.stabbing",
            "keywords": [],
            "event description": "The event is related to conflict attack stabbing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u88ad\u51fb\u523a\u6740\u6709\u5173\u3002"
        },
        "conflict.attack.stealrobhijack": {
            "event type": "conflict.attack.stealrobhijack",
            "keywords": [],
            "event description": "The event is related to conflict attack steal rob hijack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place} place, in order to take {ROLE_artifact}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place",
                "artifact"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u88ad\u51fb\u3001\u5077\u7a83\u3001\u62a2\u52ab\u3001\u52ab\u6301\u6709\u5173\u3002"
        },
        "conflict.attack.strangling": {
            "event type": "conflict.attack.strangling",
            "keywords": [],
            "event description": "The event is related to conflict attack strangling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "attacker",
                "target",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u7a92\u606f\u6709\u5173\u3002"
        },
        "conflict.demonstrate.marchprotestpoliticalgathering": {
            "event type": "conflict.demonstrate.marchprotestpoliticalgathering",
            "keywords": [],
            "event description": "The event is related to conflict demonstrate march protest political gathering.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_demonstrator} was in a demonstration or protest at {ROLE_place}.",
            "valid roles": [
                "demonstrator",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u793a\u5a01\u6e38\u884c\u6297\u8bae\u653f\u6cbb\u96c6\u4f1a\u6709\u5173\u3002"
        },
        "conflict.demonstrate.n/a": {
            "event type": "conflict.demonstrate.n/a",
            "keywords": [],
            "event description": "The event is related to conflict demonstrate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_demonstrator} was in a demonstration at {ROLE_place}.",
            "valid roles": [
                "demonstrator",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u793a\u5a01\u6709\u5173\u3002"
        },
        "conflict.yield.n/a": {
            "event type": "conflict.yield.n/a",
            "keywords": [],
            "event description": "The event is related to conflict yield.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_yielder} yielded to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "yielder",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u4ea7\u91cf\u6709\u5173\u3002"
        },
        "conflict.yield.retreat": {
            "event type": "conflict.yield.retreat",
            "keywords": [],
            "event description": "The event is related to conflict yield retreat.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_retreater} retreated from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "retreater",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u6536\u76ca\u64a4\u9000\u6709\u5173\u3002"
        },
        "conflict.yield.surrender": {
            "event type": "conflict.yield.surrender",
            "keywords": [],
            "event description": "The event is related to conflict yield surrender.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_surrenderer} surrendered to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "surrenderer",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u5c48\u670d\u6709\u5173\u3002"
        },
        "contact.collaborate.correspondence": {
            "event type": "contact.collaborate.correspondence",
            "keywords": [],
            "event description": "The event is related to contact collaborate correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated remotely with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u534f\u4f5c\u901a\u4fe1\u6709\u5173\u3002"
        },
        "contact.collaborate.meet": {
            "event type": "contact.collaborate.meet",
            "keywords": [],
            "event description": "The event is related to contact collaborate meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} met face-to-face with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u534f\u4f5c\u4f1a\u8bae\u6709\u5173\u3002"
        },
        "contact.collaborate.n/a": {
            "event type": "contact.collaborate.n/a",
            "keywords": [],
            "event description": "The event is related to contact collaborate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u534f\u4f5c\u6709\u5173\u3002"
        },
        "contact.commandorder.broadcast": {
            "event type": "contact.commandorder.broadcast",
            "keywords": [],
            "event description": "The event is related to contact command order broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u547d\u4ee4\u5e7f\u64ad\u76f8\u5173\u3002"
        },
        "contact.commandorder.correspondence": {
            "event type": "contact.commandorder.correspondence",
            "keywords": [],
            "event description": "The event is related to contact command order correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u547d\u4ee4\u547d\u4ee4\u901a\u4fe1\u6709\u5173\u3002"
        },
        "contact.commandorder.meet": {
            "event type": "contact.commandorder.meet",
            "keywords": [],
            "event description": "The event is related to contact command order meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u547d\u4ee4\u547d\u4ee4\u4f1a\u9762\u6709\u5173\u3002"
        },
        "contact.commandorder.n/a": {
            "event type": "contact.commandorder.n/a",
            "keywords": [],
            "event description": "The event is related to contact command order.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u547d\u4ee4\u6709\u5173\u3002"
        },
        "contact.commitmentpromiseexpressintent.broadcast": {
            "event type": "contact.commitmentpromiseexpressintent.broadcast",
            "keywords": [],
            "event description": "The event is related to contact commitment promise express intent broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8054\u7cfb\u76f8\u5173\u6d3b\u52a8\u627f\u8bfa\u627f\u8bfa\u660e\u793a\u610f\u5411\u5e7f\u64ad\u3002"
        },
        "contact.commitmentpromiseexpressintent.correspondence": {
            "event type": "contact.commitmentpromiseexpressintent.correspondence",
            "keywords": [],
            "event description": "The event is related to contact commitment promise express intent correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u4e0e\u4e8b\u4ef6\u76f8\u5173\u7684\u8054\u7cfb\u627f\u8bfa\u3001\u627f\u8bfa\u3001\u8868\u8fbe\u610f\u5411\u5bf9\u5e94\u3002"
        },
        "contact.commitmentpromiseexpressintent.meet": {
            "event type": "contact.commitmentpromiseexpressintent.meet",
            "keywords": [],
            "event description": "The event is related to contact commitment promise express intent meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u76f8\u5173\u6d3b\u52a8\u8054\u7cfb\u627f\u8bfa\u627f\u8bfa\u660e\u793a\u610f\u5411\u6ee1\u8db3\u3002"
        },
        "contact.commitmentpromiseexpressintent.n/a": {
            "event type": "contact.commitmentpromiseexpressintent.n/a",
            "keywords": [],
            "event description": "The event is related to contact commitment promise express intent.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8054\u7cfb\u76f8\u5173\u6d3b\u52a8\u627f\u8bfa\u627f\u8bfa\u8868\u8fbe\u610f\u5411\u3002"
        },
        "contact.discussion.correspondence": {
            "event type": "contact.discussion.correspondence",
            "keywords": [],
            "event description": "The event is related to contact discussion correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated remotely with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8ba8\u8bba\u901a\u4fe1\u6709\u5173\u3002"
        },
        "contact.discussion.meet": {
            "event type": "contact.discussion.meet",
            "keywords": [],
            "event description": "The event is related to contact discussion meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} met face-to-face with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u4eba\u8ba8\u8bba\u4f1a\u8bae\u6709\u5173\u3002"
        },
        "contact.discussion.n/a": {
            "event type": "contact.discussion.n/a",
            "keywords": [],
            "event description": "The event is related to contact discussion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u8ba8\u8bba\u6709\u5173\u3002"
        },
        "contact.funeralvigil.meet": {
            "event type": "contact.funeralvigil.meet",
            "keywords": [],
            "event description": "The event is related to contact funeral vigil meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} met face-to-face with {ROLE_participant} during a funeral or vigil for {ROLE_deceased} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "deceased",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u76f8\u5173\u8054\u7cfb\u4e27\u4e8b\u5b88\u591c\u4f1a\u3002"
        },
        "contact.funeralvigil.n/a": {
            "event type": "contact.funeralvigil.n/a",
            "keywords": [],
            "event description": "The event is related to contact funeral vigil.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated with {ROLE_participant} during a funeral or vigil for {ROLE_deceased} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "deceased",
                "place"
            ],
            "chinese event description": "\u4e0e\u4e8b\u4ef6\u6709\u5173\u7684\u8054\u7cfb\u4e27\u4e8b\u5b88\u591c\u3002"
        },
        "contact.mediastatement.broadcast": {
            "event type": "contact.mediastatement.broadcast",
            "keywords": [],
            "event description": "The event is related to contact media statement broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u5a92\u4f53\u58f0\u660e\u5e7f\u64ad\u6709\u5173\u3002"
        },
        "contact.mediastatement.n/a": {
            "event type": "contact.mediastatement.n/a",
            "keywords": [],
            "event description": "The event is related to contact media statement.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u76f8\u5173\u8054\u7cfb\u5a92\u4f53\u58f0\u660e\u3002"
        },
        "contact.negotiate.correspondence": {
            "event type": "contact.negotiate.correspondence",
            "keywords": [],
            "event description": "The event is related to contact negotiate correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated remotely with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u534f\u5546\u901a\u4fe1\u6709\u5173\u3002"
        },
        "contact.negotiate.meet": {
            "event type": "contact.negotiate.meet",
            "keywords": [],
            "event description": "The event is related to contact negotiate meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} met face-to-face with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u534f\u5546\u4f1a\u8bae\u6709\u5173\u3002"
        },
        "contact.negotiate.n/a": {
            "event type": "contact.negotiate.n/a",
            "keywords": [],
            "event description": "The event is related to contact negotiate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u534f\u5546\u6709\u5173\u3002"
        },
        "contact.prevarication.broadcast": {
            "event type": "contact.prevarication.broadcast",
            "keywords": [],
            "event description": "The event is related to contact prevarication broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u63a8\u8bff\u5e7f\u64ad\u6709\u5173\u3002"
        },
        "contact.prevarication.correspondence": {
            "event type": "contact.prevarication.correspondence",
            "keywords": [],
            "event description": "The event is related to contact prevarication correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u63a8\u8bff\u901a\u4fe1\u6709\u5173\u3002"
        },
        "contact.prevarication.meet": {
            "event type": "contact.prevarication.meet",
            "keywords": [],
            "event description": "The event is related to contact prevarication meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u63a8\u8bff\u89c1\u9762\u6709\u5173\u3002"
        },
        "contact.prevarication.n/a": {
            "event type": "contact.prevarication.n/a",
            "keywords": [],
            "event description": "The event is related to contact prevarication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u63a8\u8bff\u6709\u5173\u3002"
        },
        "contact.publicstatementinperson.broadcast": {
            "event type": "contact.publicstatementinperson.broadcast",
            "keywords": [],
            "event description": "The event is related to contact public statement in person broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u76f8\u5173\u8054\u7cfb\u516c\u5f00\u58f0\u660e\u4eb2\u81ea\u64ad\u51fa\u3002"
        },
        "contact.publicstatementinperson.n/a": {
            "event type": "contact.publicstatementinperson.n/a",
            "keywords": [],
            "event description": "The event is related to contact public statement in person.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u76f8\u5173\u7684\u8981\u4eb2\u81ea\u8054\u7cfb\u516c\u5f00\u58f0\u660e\u3002"
        },
        "contact.requestadvise.broadcast": {
            "event type": "contact.requestadvise.broadcast",
            "keywords": [],
            "event description": "The event is related to contact request advise broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8bf7\u6c42\u901a\u77e5\u5e7f\u64ad\u6709\u5173\u3002"
        },
        "contact.requestadvise.correspondence": {
            "event type": "contact.requestadvise.correspondence",
            "keywords": [],
            "event description": "The event is related to contact request advise correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8bf7\u6c42\u5efa\u8bae\u901a\u4fe1\u6709\u5173\u3002"
        },
        "contact.requestadvise.meet": {
            "event type": "contact.requestadvise.meet",
            "keywords": [],
            "event description": "The event is related to contact request advise meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8bf7\u6c42\u5efa\u8bae\u89c1\u9762\u6709\u5173\u3002"
        },
        "contact.requestadvise.n/a": {
            "event type": "contact.requestadvise.n/a",
            "keywords": [],
            "event description": "The event is related to contact request advise.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8bf7\u6c42\u5efa\u8bae\u6709\u5173\u3002"
        },
        "contact.threatencoerce.broadcast": {
            "event type": "contact.threatencoerce.broadcast",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u5a01\u80c1\u80c1\u8feb\u5e7f\u64ad\u6709\u5173\u3002"
        },
        "contact.threatencoerce.correspondence": {
            "event type": "contact.threatencoerce.correspondence",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u3001\u5a01\u80c1\u3001\u80c1\u8feb\u901a\u4fe1\u6709\u5173\u3002"
        },
        "contact.threatencoerce.meet": {
            "event type": "contact.threatencoerce.meet",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u5a01\u80c1\u80c1\u8feb\u4f1a\u9762\u6709\u5173\u3002"
        },
        "contact.threatencoerce.n/a": {
            "event type": "contact.threatencoerce.n/a",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "communicator",
                "recipient",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u3001\u5a01\u80c1\u3001\u80c1\u8feb\u6709\u5173\u3002"
        },
        "disaster.accidentcrash.accidentcrash": {
            "event type": "disaster.accidentcrash.accidentcrash",
            "keywords": [],
            "event description": "The event is related to disaster accidentcrash accidentcrash.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_driverpassenger} person in {ROLE_vehicle} vehicle crashed into {ROLE_crashobject} at {ROLE_place}.",
            "valid roles": [
                "driverpassenger",
                "vehicle",
                "crashobject",
                "place"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u707e\u96be\u4e8b\u6545\u6709\u5173\u3002"
        },
        "disaster.fireexplosion.fireexplosion": {
            "event type": "disaster.fireexplosion.fireexplosion",
            "keywords": [],
            "event description": "The event is related to disaster fireexplosion fireexplosion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_fireexplosionobject} caught fire or exploded from {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": [
                "fireexplosionobject",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u706b\u707e\u7206\u70b8\u6709\u5173\u3002"
        },
        "government.agreements.acceptagreementcontractceasefire": {
            "event type": "government.agreements.acceptagreementcontractceasefire",
            "keywords": [],
            "event description": "The event is related to government agreements accept agreement contract ceasefire.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} and {ROLE_participant} signed an agreement at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u534f\u8bae\u6709\u5173\uff0c\u63a5\u53d7\u534f\u8bae\uff0c\u5408\u540c\u505c\u706b\u3002"
        },
        "government.agreements.n/a": {
            "event type": "government.agreements.n/a",
            "keywords": [],
            "event description": "The event is related to government agreements.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} and {ROLE_participant} signed an agreement at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u534f\u8bae\u6709\u5173\u3002"
        },
        "government.agreements.rejectnullifyagreementcontractceasefire": {
            "event type": "government.agreements.rejectnullifyagreementcontractceasefire",
            "keywords": [],
            "event description": "The event is related to government agreements reject nullify agreement contract ceasefire.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_rejecternullifier} rejected or nullified an agreement with {ROLE_otherparticipant} at {ROLE_place}.",
            "valid roles": [
                "rejecternullifier",
                "otherparticipant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u534f\u8bae\u6709\u5173\uff0c\u62d2\u7edd\u534f\u8bae\uff0c\u65e0\u6548\u534f\u8bae\uff0c\u5408\u540c\u505c\u706b\u3002"
        },
        "government.agreements.violateagreement": {
            "event type": "government.agreements.violateagreement",
            "keywords": [],
            "event description": "The event is related to government agreements violate agreement.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_violator} violated an agreement with {ROLE_otherparticipant} at {ROLE_place}.",
            "valid roles": [
                "violator",
                "otherparticipant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u534f\u8bae\u8fdd\u53cd\u534f\u8bae\u6709\u5173\u3002"
        },
        "government.formation.mergegpe": {
            "event type": "government.formation.mergegpe",
            "keywords": [],
            "event description": "The event is related to government formation mergegpe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} merged with {ROLE_participant} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u7ec4\u5efa\u5408\u5e76\u6709\u5173\u3002"
        },
        "government.formation.n/a": {
            "event type": "government.formation.n/a",
            "keywords": [],
            "event description": "The event is related to government formation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_gpe} was formed by {ROLE_founder} at {ROLE_place}.",
            "valid roles": [
                "gpe",
                "founder",
                "place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u7ec4\u5efa\u6709\u5173\u3002"
        },
        "government.formation.startgpe": {
            "event type": "government.formation.startgpe",
            "keywords": [],
            "event description": "The event is related to government formation startpage.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_gpe} was started by {ROLE_founder} at {ROLE_place}.",
            "valid roles": [
                "gpe",
                "founder",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u7ec4\u5efa\u6709\u5173\u3002"
        },
        "government.legislate.legislate": {
            "event type": "government.legislate.legislate",
            "keywords": [],
            "event description": "The event is related to government legislate legislate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_governmentbody} legislature enacted {ROLE_law} law at {ROLE_place}.",
            "valid roles": [
                "governmentbody",
                "law",
                "place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u7acb\u6cd5\u6709\u5173\u3002"
        },
        "government.spy.spy": {
            "event type": "government.spy.spy",
            "keywords": [],
            "event description": "The event is related to government spy spy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_spy} spied on {ROLE_observedentity} to the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "spy",
                "observedentity",
                "beneficiary",
                "place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u95f4\u8c0d\u6709\u5173\u3002"
        },
        "government.vote.castvote": {
            "event type": "government.vote.castvote",
            "keywords": [],
            "event description": "The event is related to government vote castvote.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_voter} voted for {ROLE_candidate} on {ROLE_ballot} ballot with {ROLE_result} results at {ROLE_place}.",
            "valid roles": [
                "voter",
                "candidate",
                "ballot",
                "result",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u6295\u7968\u6709\u5173\u3002"
        },
        "government.vote.n/a": {
            "event type": "government.vote.n/a",
            "keywords": [],
            "event description": "The event is related to government vote.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_voter} voted for {ROLE_candidate} on {ROLE_ballot} ballot with {ROLE_result} results at {ROLE_place}.",
            "valid roles": [
                "voter",
                "candidate",
                "ballot",
                "result",
                "place"
            ],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u653f\u5e9c\u6295\u7968\u6709\u5173\u3002"
        },
        "government.vote.violationspreventvote": {
            "event type": "government.vote.violationspreventvote",
            "keywords": [],
            "event description": "The event is related to government vote violations prevent vote.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevented {ROLE_voter} from voting for {ROLE_candidate} on {ROLE_ballot} ballot at {ROLE_place}.",
            "valid roles": [
                "preventer",
                "voter",
                "candidate",
                "ballot",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653f\u5e9c\u6295\u7968\u8fdd\u89c4\u963b\u6b62\u6295\u7968\u6709\u5173\u3002"
        },
        "inspection.sensoryobserve.inspectpeopleorganization": {
            "event type": "inspection.sensoryobserve.inspectpeopleorganization",
            "keywords": [],
            "event description": "The event is related to inspection sensory observe inspect people organization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_inspector} inspected {ROLE_inspectedentity} at {ROLE_place}.",
            "valid roles": [
                "inspector",
                "inspectedentity",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u662f\u4e0e\u68c0\u9a8c\u611f\u5b98\u89c2\u5bdf\u6709\u5173\u7684\u68c0\u9a8c\u4eba\u5458\u7ec4\u7ec7\u3002"
        },
        "inspection.sensoryobserve.monitorelection": {
            "event type": "inspection.sensoryobserve.monitorelection",
            "keywords": [],
            "event description": "The event is related to inspection sensory observe monitor election.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_monitor} monitored {ROLE_monitoredentity} taking part in an election at {ROLE_place}.",
            "valid roles": [
                "monitor",
                "monitoredentity",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u68c0\u67e5\u611f\u5b98\u89c2\u5bdf\u73ed\u957f\u9009\u4e3e\u6709\u5173\u3002"
        },
        "inspection.sensoryobserve.n/a": {
            "event type": "inspection.sensoryobserve.n/a",
            "keywords": [],
            "event description": "The event is related to inspection sensory observe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_observer} observed {ROLE_observedentity} at {ROLE_place}.",
            "valid roles": [
                "observer",
                "observedentity",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u68c0\u67e5\u611f\u5b98\u89c2\u5bdf\u6709\u5173\u3002"
        },
        "inspection.sensoryobserve.physicalinvestigateinspect": {
            "event type": "inspection.sensoryobserve.physicalinvestigateinspect",
            "keywords": [],
            "event description": "The event is related to inspection sensory observe physical investigate inspect.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_inspector} inspected {ROLE_inspectedentity} at {ROLE_place}.",
            "valid roles": [
                "inspector",
                "inspectedentity",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u68c0\u67e5\u611f\u5b98\u89c2\u5bdf\u7269\u7406\u8c03\u67e5\u68c0\u67e5\u6709\u5173\u3002"
        },
        "justice.arrestjaildetain.arrestjaildetain": {
            "event type": "justice.arrestjaildetain.arrestjaildetain",
            "keywords": [],
            "event description": "The event is related to justice arrest jail detain.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_jailer} arrested or jailed {ROLE_detainee} for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": [
                "jailer",
                "detainee",
                "crime",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u53f8\u6cd5\u902e\u6355\u3001\u76d1\u72f1\u62d8\u7559\u3002"
        },
        "justice.initiatejudicialprocess.chargeindict": {
            "event type": "justice.initiatejudicialprocess.chargeindict",
            "keywords": [],
            "event description": "The event is related to justice initiative judicial process charge indict.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_prosecutor} charged or indicted {ROLE_defendant} before {ROLE_judgecourt} court or judge for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": [
                "prosecutor",
                "defendant",
                "judgecourt",
                "crime",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u53f8\u6cd5\u4e3b\u52a8\uff0c\u53f8\u6cd5\u7a0b\u5e8f\u6307\u63a7\u8d77\u8bc9\u3002"
        },
        "justice.initiatejudicialprocess.n/a": {
            "event type": "justice.initiatejudicialprocess.n/a",
            "keywords": [],
            "event description": "The event is related to justice initiative judicial process.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_prosecutor} initiated judicial process pertaining to {ROLE_defendant} before {ROLE_judgecourt} court or judge for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": [
                "prosecutor",
                "defendant",
                "judgecourt",
                "crime",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u53f8\u6cd5\u4e3b\u52a8\u53f8\u6cd5\u7a0b\u5e8f\u3002"
        },
        "justice.initiatejudicialprocess.trialhearing": {
            "event type": "justice.initiatejudicialprocess.trialhearing",
            "keywords": [],
            "event description": "The event is related to justice initiative judicial process trial hearing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_prosecutor} tried {ROLE_defendant} before {ROLE_judgecourt} court or judge for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": [
                "prosecutor",
                "defendant",
                "judgecourt",
                "crime",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u5173\u7cfb\u5230\u53f8\u6cd5\u4e3b\u52a8\u53f8\u6cd5\u7a0b\u5e8f\u5ba1\u5224\u542c\u8bc1\u3002"
        },
        "justice.investigate.investigatecrime": {
            "event type": "justice.investigate.investigatecrime",
            "keywords": [],
            "event description": "The event is related to justice investigate investigate crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_investigator} investigated {ROLE_defendant} for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": [
                "investigator",
                "defendant",
                "crime",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u5173\u7cfb\u5230\u53f8\u6cd5\u8c03\u67e5\u8c03\u67e5\u72af\u7f6a\u3002"
        },
        "justice.investigate.n/a": {
            "event type": "justice.investigate.n/a",
            "keywords": [],
            "event description": "The event is related to justice investigate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_investigator} investigated {ROLE_defendant} at {ROLE_place}.",
            "valid roles": [
                "investigator",
                "defendant",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u53f8\u6cd5\u8c03\u67e5\u3002"
        },
        "justice.judicialconsequences.convict": {
            "event type": "justice.judicialconsequences.convict",
            "keywords": [],
            "event description": "The event is related to justice judicial consequences convict.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_judgecourt} court or judge convicted {ROLE_defendant} of {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": [
                "judgecourt",
                "defendant",
                "crime",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u5173\u7cfb\u5230\u7f6a\u72af\u7684\u53f8\u6cd5\u516c\u6b63\u548c\u53f8\u6cd5\u540e\u679c\u3002"
        },
        "justice.judicialconsequences.execute": {
            "event type": "justice.judicialconsequences.execute",
            "keywords": [],
            "event description": "The event is related to justice judicial consequences execute.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_executioner} executed {ROLE_defendant} for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": [
                "executioner",
                "defendant",
                "crime",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u5173\u7cfb\u5230\u53f8\u6cd5\u516c\u6b63\u7684\u53f8\u6cd5\u540e\u679c\u6267\u884c\u3002"
        },
        "justice.judicialconsequences.extradite": {
            "event type": "justice.judicialconsequences.extradite",
            "keywords": [],
            "event description": "The event is related to justice judicial consequences extradite.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_extraditer} extradited {ROLE_defendant} for {ROLE_crime} crime from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "extraditer",
                "defendant",
                "crime",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u53f8\u6cd5\u53f8\u6cd5\u540e\u679c\u7684\u5f15\u6e21\u3002"
        },
        "justice.judicialconsequences.n/a": {
            "event type": "justice.judicialconsequences.n/a",
            "keywords": [],
            "event description": "The event is related to justice judicial consequences.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_judgecourt} court or judge decided consequences of {ROLE_crime} crime, committed by {ROLE_defendant}, at {ROLE_place}.",
            "valid roles": [
                "judgecourt",
                "defendant",
                "crime",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u53f8\u6cd5\u516c\u6b63\u7684\u53f8\u6cd5\u540e\u679c\u3002"
        },
        "life.die.deathcausedbyviolentevents": {
            "event type": "life.die.deathcausedbyviolentevents",
            "keywords": [],
            "event description": "The event is related to life die death caused by violent events.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_killer} killed {ROLE_victim} using {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": [
                "killer",
                "victim",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u662f\u4e0e\u751f\u547d\u6b7b\u4ea1\u6709\u5173\u7684\u66b4\u529b\u4e8b\u4ef6\u3002"
        },
        "life.die.n/a": {
            "event type": "life.die.n/a",
            "keywords": [],
            "event description": "The event is related to life die.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} died at {ROLE_place} place, killed by {ROLE_killer} killer.",
            "valid roles": [
                "victim",
                "place",
                "killer"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u751f\u547d\u6b7b\u4ea1\u6709\u5173\u3002"
        },
        "life.die.nonviolentdeath": {
            "event type": "life.die.nonviolentdeath",
            "keywords": [],
            "event description": "The event is related to life die non violent death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} died at {ROLE_place} place, killed by {ROLE_killer} killer.",
            "valid roles": [
                "victim",
                "place",
                "killer"
            ],
            "chinese event description": "\u4e8b\u4ef6\u6d89\u53ca\u5230\u751f\u547d\u6b7b\u4ea1\u975e\u66b4\u529b\u6b7b\u4ea1\u3002"
        },
        "life.injure.illnessdegradationhungerthirst": {
            "event type": "life.injure.illnessdegradationhungerthirst",
            "keywords": [],
            "event description": "The event is related to life injure illness degradation hunger thirst.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} has extreme hunger imposed by {ROLE_injurer} injurer at {ROLE_place}.",
            "valid roles": [
                "victim",
                "place",
                "injurer"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u751f\u547d\u4f24\u5bb3\u75be\u75c5\u9000\u5316\u9965\u997f\u53e3\u6e34\u6709\u5173\u3002"
        },
        "life.injure.illnessdegradationphysical": {
            "event type": "life.injure.illnessdegradationphysical",
            "keywords": [],
            "event description": "The event is related to life injure illness degradation physical.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} person has some physical degradation imposed by {ROLE_injurer} injurer at {ROLE_place}.",
            "valid roles": [
                "victim",
                "place",
                "injurer"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u751f\u547d\u4f24\u5bb3\u75be\u75c5\u9000\u5316\u8eab\u4f53\u6709\u5173\u3002"
        },
        "life.injure.injurycausedbyviolentevents": {
            "event type": "life.injure.injurycausedbyviolentevents",
            "keywords": [],
            "event description": "The event is related to life injure injury caused by violent events.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_injurer} injured {ROLE_victim} using {ROLE_instrument} instrument issue at {ROLE_place}.",
            "valid roles": [
                "injurer",
                "victim",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u5230\u7531\u66b4\u529b\u4e8b\u4ef6\u9020\u6210\u7684\u4eba\u8eab\u4f24\u5bb3\u3002"
        },
        "life.injure.n/a": {
            "event type": "life.injure.n/a",
            "keywords": [],
            "event description": "The event is related to life injure.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} was injured by {ROLE_injurer} at {ROLE_place}.",
            "valid roles": [
                "victim",
                "injurer",
                "place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u6d89\u53ca\u4eba\u8eab\u4f24\u5bb3\u3002"
        },
        "manufacture.artifact.build": {
            "event type": "manufacture.artifact.build",
            "keywords": [],
            "event description": "The event is related to manufacture artifact build.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_manufacturer} manufactured or created or produced {ROLE_artifact} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "manufacturer",
                "artifact",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5236\u9020\u5de5\u4ef6\u6784\u5efa\u76f8\u5173\u3002"
        },
        "manufacture.artifact.createintellectualproperty": {
            "event type": "manufacture.artifact.createintellectualproperty",
            "keywords": [],
            "event description": "The event is related to manufacture artifact create intellectual property.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_manufacturer} manufactured or created or produced {ROLE_artifact} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "manufacturer",
                "artifact",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5236\u9020\u5de5\u4ef6\u3001\u521b\u9020\u77e5\u8bc6\u4ea7\u6743\u6709\u5173\u3002"
        },
        "manufacture.artifact.createmanufacture": {
            "event type": "manufacture.artifact.createmanufacture",
            "keywords": [],
            "event description": "The event is related to manufacture artifact create manufacture.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_manufacturer} manufactured or created or produced {ROLE_artifact} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "manufacturer",
                "artifact",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5236\u9020\u5de5\u4ef6\u521b\u5efa\u5236\u9020\u76f8\u5173\u3002"
        },
        "manufacture.artifact.n/a": {
            "event type": "manufacture.artifact.n/a",
            "keywords": [],
            "event description": "The event is related to manufacture artifact.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_manufacturer} manufactured or created or produced {ROLE_artifact} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": [
                "manufacturer",
                "artifact",
                "instrument",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5236\u9020\u5de5\u4ef6\u6709\u5173\u3002"
        },
        "movement.transportartifact.bringcarryunload": {
            "event type": "movement.transportartifact.bringcarryunload",
            "keywords": [],
            "event description": "The event is related to movement transport artifact bring carry unload.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u8fd0\u8f93\u795e\u5668\u5e26\u6765\u7684\u642c\u8fd0\u5378\u8f7d\u6709\u5173\u3002"
        },
        "movement.transportartifact.disperseseparate": {
            "event type": "movement.transportartifact.disperseseparate",
            "keywords": [],
            "event description": "The event is related to movement transport artifact disperse separate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\uff0c\u4f20\u9001\u795e\u5668\u5206\u6563\u5206\u79bb\u3002"
        },
        "movement.transportartifact.fall": {
            "event type": "movement.transportartifact.fall",
            "keywords": [],
            "event description": "The event is related to movement transport artifact fall.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_artifact} fell from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "artifact",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u4f20\u9001\u795e\u5668\u6389\u843d\u6709\u5173\u3002"
        },
        "movement.transportartifact.grantentry": {
            "event type": "movement.transportartifact.grantentry",
            "keywords": [],
            "event description": "The event is related to movement transport artifact grant entry.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} grants {ROLE_artifact} entry to {ROLE_origin} place from {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u4f20\u8f93\u5de5\u4ef6\u6388\u6743\u6761\u76ee\u76f8\u5173\u3002"
        },
        "movement.transportartifact.hide": {
            "event type": "movement.transportartifact.hide",
            "keywords": [],
            "event description": "The event is related to movement transport artifact hide.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} concealed {ROLE_artifact} in {ROLE_hidingplace} place, transported in {ROLE_vehicle} vehicle from {ROLE_origin} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "hidingplace",
                "vehicle",
                "origin"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u4f20\u8f93\u85cf\u7269\u6709\u5173\u3002"
        },
        "movement.transportartifact.n/a": {
            "event type": "movement.transportartifact.n/a",
            "keywords": [],
            "event description": "The event is related to movement transport artifact.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u4f20\u8f93\u5de5\u4ef6\u76f8\u5173\u3002"
        },
        "movement.transportartifact.nonviolentthrowlaunch": {
            "event type": "movement.transportartifact.nonviolentthrowlaunch",
            "keywords": [],
            "event description": "The event is related to movement transport artifact nonviolent throw launch.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u6d89\u53ca\u79fb\u52a8\u8fd0\u8f93\u795e\u5668\u975e\u66b4\u529b\u6295\u63b7\u53d1\u5c04\u3002"
        },
        "movement.transportartifact.prevententry": {
            "event type": "movement.transportartifact.prevententry",
            "keywords": [],
            "event description": "The event is related to movement transport artifact prevent entry.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevents {ROLE_transporter} from transporting {ROLE_artifact} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "preventer",
                "transporter",
                "artifact",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u4f20\u8f93\u5de5\u4ef6\u963b\u6b62\u8fdb\u5165\u6709\u5173\u3002"
        },
        "movement.transportartifact.preventexit": {
            "event type": "movement.transportartifact.preventexit",
            "keywords": [],
            "event description": "The event is related to movement transport artifact prevent exit.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevents {ROLE_transporter} from transporting {ROLE_artifact} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "preventer",
                "transporter",
                "artifact",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u4f20\u8f93\u5de5\u4ef6\u963b\u6b62\u9000\u51fa\u6709\u5173\u3002"
        },
        "movement.transportartifact.receiveimport": {
            "event type": "movement.transportartifact.receiveimport",
            "keywords": [],
            "event description": "The event is related to movement transport artifact receive import.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u4f20\u8f93\u5de5\u4ef6\u63a5\u6536\u5bfc\u5165\u76f8\u5173\u3002"
        },
        "movement.transportartifact.sendsupplyexport": {
            "event type": "movement.transportartifact.sendsupplyexport",
            "keywords": [],
            "event description": "The event is related to movement transport artifact send supply export.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u8fd0\u8f93\u5de5\u4ef6\u53d1\u9001\u4f9b\u5e94\u51fa\u53e3\u6709\u5173\u3002"
        },
        "movement.transportartifact.smuggleextract": {
            "event type": "movement.transportartifact.smuggleextract",
            "keywords": [],
            "event description": "The event is related to movement transport artifact smuggle extract.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "artifact",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u8fd0\u8f93\u85cf\u7269\u8d70\u79c1\u63d0\u53d6\u6709\u5173\u3002"
        },
        "movement.transportperson.bringcarryunload": {
            "event type": "movement.transportperson.bringcarryunload",
            "keywords": [],
            "event description": "The event is related to movement transport person bring carry unload.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "passenger",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u8fd0\u8f93\u4eba\u5458\u5e26\u6765\u7684\u642c\u8fd0\u5378\u8f7d\u6709\u5173\u3002"
        },
        "movement.transportperson.disperseseparate": {
            "event type": "movement.transportperson.disperseseparate",
            "keywords": [],
            "event description": "The event is related to movement transport person disperse separate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "passenger",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\uff0c\u8fd0\u8f93\u4eba\u5458\u5206\u6563\u5206\u79bb\u3002"
        },
        "movement.transportperson.evacuationrescue": {
            "event type": "movement.transportperson.evacuationrescue",
            "keywords": [],
            "event description": "The event is related to movement transport person evacuation rescue.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "passenger",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u8fd0\u52a8\u8fd0\u8f93\u4eba\u5458\u758f\u6563\u6551\u63f4\u3002"
        },
        "movement.transportperson.fall": {
            "event type": "movement.transportperson.fall",
            "keywords": [],
            "event description": "The event is related to movement transport person fall.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_passenger} fell from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "passenger",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u8fd0\u8f93\u4eba\u5458\u8dcc\u5012\u6709\u5173\u3002"
        },
        "movement.transportperson.grantentryasylum": {
            "event type": "movement.transportperson.grantentryasylum",
            "keywords": [],
            "event description": "The event is related to movement transport person grantentry asylum.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_granter} grants entry to {ROLE_transporter} transporting {ROLE_passenger} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "granter",
                "transporter",
                "passenger",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u79fb\u9001\u4eba\u6536\u5bb9\u6709\u5173\u3002"
        },
        "movement.transportperson.hide": {
            "event type": "movement.transportperson.hide",
            "keywords": [],
            "event description": "The event is related to movement transport person hide.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} concealed {ROLE_passenger} in {ROLE_hidingplace} place, transported in {ROLE_vehicle} vehicle from {ROLE_origin} place.",
            "valid roles": [
                "transporter",
                "passenger",
                "hidingplace",
                "vehicle",
                "origin"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u8fd0\u8f93\u4eba\u5458\u9690\u85cf\u6709\u5173\u3002"
        },
        "movement.transportperson.n/a": {
            "event type": "movement.transportperson.n/a",
            "keywords": [],
            "event description": "The event is related to movement transport person.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "passenger",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u8fd0\u8f93\u6709\u5173\u3002"
        },
        "movement.transportperson.prevententry": {
            "event type": "movement.transportperson.prevententry",
            "keywords": [],
            "event description": "The event is related to movement transport person prevent entry.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevents {ROLE_transporter} from transporting {ROLE_passenger} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "preventer",
                "transporter",
                "passenger",
                "origin",
                "destination"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\uff0c\u8fd0\u8f93\u4eba\u5458\u7981\u6b62\u5165\u5883\u3002"
        },
        "movement.transportperson.preventexit": {
            "event type": "movement.transportperson.preventexit",
            "keywords": [],
            "event description": "The event is related to movement transport person prevent exit.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevents {ROLE_transporter} from transporting {ROLE_passenger} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "preventer",
                "transporter",
                "passenger",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\uff0c\u8fd0\u8f93\u4eba\u5458\u7981\u6b62\u51fa\u5883\u3002"
        },
        "movement.transportperson.selfmotion": {
            "event type": "movement.transportperson.selfmotion",
            "keywords": [],
            "event description": "The event is related to movement transport person self motion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} moved in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u6709\u5173\uff0c\u8fd0\u8f93\u4eba\u81ea\u8eab\u8fd0\u52a8\u3002"
        },
        "movement.transportperson.smuggleextract": {
            "event type": "movement.transportperson.smuggleextract",
            "keywords": [],
            "event description": "The event is related to movement transport person smuggle extract.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": [
                "transporter",
                "passenger",
                "vehicle",
                "origin",
                "destination"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u4eba\u8d70\u79c1\u63d0\u53d6\u6709\u5173\u3002"
        },
        "personnel.elect.n/a": {
            "event type": "personnel.elect.n/a",
            "keywords": [],
            "event description": "The event is related to personnel elect.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_voter} elected {ROLE_candidate} at {ROLE_place}.",
            "valid roles": [
                "voter",
                "candidate",
                "place"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4eba\u4e8b\u9009\u4e3e\u6709\u5173\u3002"
        },
        "personnel.elect.winelection": {
            "event type": "personnel.elect.winelection",
            "keywords": [],
            "event description": "The event is related to personnel elect win election.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_voter} elected {ROLE_candidate} at {ROLE_place}.",
            "valid roles": [
                "voter",
                "candidate",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u4e8b\u9009\u4e3e\u6709\u5173\u3002"
        },
        "personnel.endposition.firinglayoff": {
            "event type": "personnel.endposition.firinglayoff",
            "keywords": [],
            "event description": "The event is related to personnel end position firing layoff.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} stopped working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": [
                "employee",
                "placeofemployment",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u7ec8\u6b62\u5c97\u4f4d\u89e3\u96c7\u88c1\u5458\u6709\u5173\u3002"
        },
        "personnel.endposition.n/a": {
            "event type": "personnel.endposition.n/a",
            "keywords": [],
            "event description": "The event is related to personnel end position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} stopped working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": [
                "employee",
                "placeofemployment",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u672b\u7aef\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "personnel.endposition.quitretire": {
            "event type": "personnel.endposition.quitretire",
            "keywords": [],
            "event description": "The event is related to personnel end position quit retire.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} stopped working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": [
                "employee",
                "placeofemployment",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u79bb\u804c\u9000\u4f11\u6709\u5173\u3002"
        },
        "personnel.startposition.hiring": {
            "event type": "personnel.startposition.hiring",
            "keywords": [],
            "event description": "The event is related to personnel start position hiring.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} started working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": [
                "employee",
                "placeofemployment",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u662f\u6709\u5173\u4eba\u4e8b\u5f00\u59cb\u5c97\u4f4d\u62db\u8058\u3002"
        },
        "personnel.startposition.n/a": {
            "event type": "personnel.startposition.n/a",
            "keywords": [],
            "event description": "The event is related to personnel start position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} started working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": [
                "employee",
                "placeofemployment",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u542f\u52a8\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "transaction.transaction.embargosanction": {
            "event type": "transaction.transaction.embargosanction",
            "keywords": [],
            "event description": "The event is related to transaction transaction embargo sanction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevented {ROLE_giver} from giving {ROLE_artifactmoney} to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "preventer",
                "giver",
                "recipient",
                "artifactmoney",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u6709\u5173\uff0c\u4ea4\u6613\u7981\u8fd0\u5236\u88c1\u3002"
        },
        "transaction.transaction.giftgrantprovideaid": {
            "event type": "transaction.transaction.giftgrantprovideaid",
            "keywords": [],
            "event description": "The event is related to transaction transaction gift grant provide aid.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave something to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u662f\u4e0e\u4ea4\u6613\u6709\u5173\u7684\u4ea4\u6613\uff0c\u8d60\u4e0e\u3001\u8d60\u6b3e\u3001\u63d0\u4f9b\u63f4\u52a9\u3002"
        },
        "transaction.transaction.n/a": {
            "event type": "transaction.transaction.n/a",
            "keywords": [],
            "event description": "The event is related to transaction transaction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "A transaction occurred between {ROLE_participant} and {ROLE_participant} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "participant",
                "participant",
                "beneficiary",
                "place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u4e8b\u52a1\u76f8\u5173\u3002"
        },
        "transaction.transaction.transfercontrol": {
            "event type": "transaction.transaction.transfercontrol",
            "keywords": [],
            "event description": "The event is related to transaction transaction transfer control.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} transferred control of {ROLE_territoryorfacility} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "territoryorfacility",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u76f8\u5173\uff0c\u4e8b\u52a1\u4f20\u8f93\u63a7\u5236\u3002"
        },
        "transaction.transfermoney.borrowlend": {
            "event type": "transaction.transfermoney.borrowlend",
            "keywords": [],
            "event description": "The event is related to transaction transfer money borrow lend.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "money",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u6709\u5173\uff0c\u8f6c\u8d26\u3001\u501f\u94b1\u3001\u653e\u8d37\u3002"
        },
        "transaction.transfermoney.embargosanction": {
            "event type": "transaction.transfermoney.embargosanction",
            "keywords": [],
            "event description": "The event is related to transaction transfer money embargo sanction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevented {ROLE_giver} from giving {ROLE_money} to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "preventer",
                "giver",
                "recipient",
                "money",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u8f6c\u8d26\u7981\u8fd0\u5236\u88c1\u6709\u5173\u3002"
        },
        "transaction.transfermoney.giftgrantprovideaid": {
            "event type": "transaction.transfermoney.giftgrantprovideaid",
            "keywords": [],
            "event description": "The event is related to transaction transfer money gift grant provide aid.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "money",
                "place"
            ],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u4ea4\u6613\u6709\u5173\uff0c\u8f6c\u8d26\u3001\u6350\u6b3e\u3001\u8d60\u6b3e\u3001\u63d0\u4f9b\u63f4\u52a9\u3002"
        },
        "transaction.transfermoney.n/a": {
            "event type": "transaction.transfermoney.n/a",
            "keywords": [],
            "event description": "The event is related to transaction transfer money.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "money",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8f6c\u8d26\u4ea4\u6613\u6709\u5173\u3002"
        },
        "transaction.transfermoney.payforservice": {
            "event type": "transaction.transfermoney.payforservice",
            "keywords": [],
            "event description": "The event is related to transaction transfer money payforservice.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "money",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u8f6c\u8d26\u4ed8\u6b3e\u670d\u52a1\u6709\u5173\u3002"
        },
        "transaction.transfermoney.purchase": {
            "event type": "transaction.transfermoney.purchase",
            "keywords": [],
            "event description": "The event is related to transaction transfer money purchase.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "money",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u6709\u5173\uff0c\u8f6c\u8d26\u8d2d\u4e70\u3002"
        },
        "transaction.transferownership.borrowlend": {
            "event type": "transaction.transferownership.borrowlend",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership borrow lend.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_artifact} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "artifact",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u6709\u5173\uff0c\u8f6c\u8ba9\u6240\u6709\u6743\uff0c\u501f\u6b3e\uff0c\u51fa\u501f\u3002"
        },
        "transaction.transferownership.embargosanction": {
            "event type": "transaction.transferownership.embargosanction",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership embargo sanction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevented {ROLE_giver} from giving {ROLE_artifact} to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": [
                "preventer",
                "giver",
                "recipient",
                "artifact",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u4ea4\u6613\u8f6c\u8ba9\u6240\u6709\u6743\u7981\u8fd0\u5236\u88c1\u3002"
        },
        "transaction.transferownership.giftgrantprovideaid": {
            "event type": "transaction.transferownership.giftgrantprovideaid",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership gift grant provide aid.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_artifact} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "artifact",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u662f\u6709\u5173\u4ea4\u6613\u8f6c\u8ba9\u6240\u6709\u6743\u8d60\u4e0e\u8d60\u6b3e\u63d0\u4f9b\u63f4\u52a9\u3002"
        },
        "transaction.transferownership.n/a": {
            "event type": "transaction.transferownership.n/a",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_artifact} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "artifact",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u8f6c\u79fb\u6240\u6709\u6743\u6709\u5173\u3002"
        },
        "transaction.transferownership.purchase": {
            "event type": "transaction.transferownership.purchase",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership purchase.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_artifact} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": [
                "giver",
                "recipient",
                "beneficiary",
                "artifact",
                "place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u8f6c\u8ba9\u6240\u6709\u6743\u8d2d\u4e70\u6709\u5173\u3002"
        }
    },
    "wikievents": {
        "ArtifactExistence.DamageDestroyDisableDismantle.Damage": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.Damage",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle damage.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Damager} damaged {ROLE_Artifact} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Artifact",
                "Damager",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u795e\u5668\u5b58\u5728\u4f24\u5bb3\u7834\u574f\u7981\u7528\u62c6\u9664\u4f24\u5bb3\u6709\u5173\u3002"
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Destroy": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.Destroy",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle destroy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Destroyer} destroyed {ROLE_Artifact} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Artifact",
                "Destroyer",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u795e\u5668\u5b58\u5728\uff0c\u7834\u574f\uff0c\u7834\u574f\uff0c\u7981\u7528\uff0c\u62c6\u9664\uff0c\u7834\u574f\u6709\u5173\u3002"
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.DisableDefuse": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.DisableDefuse",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle disable defuse.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Disabler} disabled or defused {ROLE_Artifact} by using {ROLE_Instrument}.",
            "valid roles": [
                "Artifact",
                "Disabler",
                "Instrument"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u795e\u5668\u7684\u5b58\u5728\u3001\u635f\u574f\u3001\u7834\u574f\u3001\u7981\u7528\u3001\u62c6\u9664\u3001\u7981\u7528\u3001\u62c6\u9664\u6709\u5173\u3002"
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Dismantle": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.Dismantle",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle dismantle.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Dismantler} dismantled {ROLE_Artifact} by using {ROLE_Instrument} from {ROLE_Components} in {ROLE_Place}.",
            "valid roles": [
                "Artifact",
                "Components",
                "Dismantler",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u795e\u5668\u5b58\u5728\u6709\u5173\uff0c\u635f\u574f\uff0c\u7834\u574f\uff0c\u7981\u7528\uff0c\u62c6\u9664\uff0c\u62c6\u9664\u3002"
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Unspecified": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.Unspecified",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_DamagerDestroyer} damaged or destroyed {ROLE_Artifact} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Artifact",
                "DamagerDestroyer",
                "Instrument",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u795e\u5668\u5b58\u5728\u3001\u635f\u574f\u3001\u6467\u6bc1\u3001\u7981\u7528\u3001\u62c6\u9664\u6709\u5173\u3002"
        },
        "ArtifactExistence.ManufactureAssemble.Unspecified": {
            "event type": "ArtifactExistence.ManufactureAssemble.Unspecified",
            "keywords": [],
            "event description": "The event is related to artifact existence manufacture assemble.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_ManufacturerAssembler} manufactured or assembled or produced {ROLE_Artifact} from {ROLE_Components} in {ROLE_Place}.",
            "valid roles": [
                "Artifact",
                "Components",
                "ManufacturerAssembler",
                "Place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u795e\u5668\u5b58\u5728\u5236\u9020\u88c5\u914d\u6709\u5173\u3002"
        },
        "Cognitive.IdentifyCategorize.Unspecified": {
            "event type": "Cognitive.IdentifyCategorize.Unspecified",
            "keywords": [],
            "event description": "The event is related to cognitive identify categorize.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Identifier} identified {ROLE_IdentifiedObject} as {ROLE_IdentifiedRole} in {ROLE_Place}.",
            "valid roles": [
                "IdentifiedObject",
                "IdentifiedRole",
                "Identifier",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8ba4\u77e5\u8bc6\u522b\u5206\u7c7b\u6709\u5173\u3002"
        },
        "Cognitive.Inspection.SensoryObserve": {
            "event type": "Cognitive.Inspection.SensoryObserve",
            "keywords": [],
            "event description": "The event is related to cognitive inspection sensory observe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Observer} observed {ROLE_ObservedEntity} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Instrument",
                "ObservedEntity",
                "Observer",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8ba4\u77e5\u68c0\u67e5\u3001\u611f\u5b98\u89c2\u5bdf\u6709\u5173\u3002"
        },
        "Cognitive.Research.Unspecified": {
            "event type": "Cognitive.Research.Unspecified",
            "keywords": [],
            "event description": "The event is related to cognitive research.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Researcher} researched {ROLE_Subject} in {ROLE_Place}.",
            "valid roles": [
                "Place",
                "Researcher",
                "Subject"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u8ba4\u77e5\u7814\u7a76\u6709\u5173\u3002"
        },
        "Cognitive.TeachingTrainingLearning.Unspecified": {
            "event type": "Cognitive.TeachingTrainingLearning.Unspecified",
            "keywords": [],
            "event description": "The event is related to cognitive teaching training learning.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_TeacherTrainer} taught or trained {ROLE_Learner}.",
            "valid roles": [
                "Learner",
                "TeacherTrainer"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8ba4\u77e5\u6559\u5b66\u8bad\u7ec3\u5b66\u4e60\u6709\u5173\u3002"
        },
        "Conflict.Attack.DetonateExplode": {
            "event type": "Conflict.Attack.DetonateExplode",
            "keywords": [],
            "event description": "The event is related to conflict attack detonate explode.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} detonated or exploded {ROLE_ExplosiveDevice} by using {ROLE_Instrument} to attack {ROLE_Target} in {ROLE_Place}.",
            "valid roles": [
                "Attacker",
                "ExplosiveDevice",
                "Instrument",
                "Place",
                "Target"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u6709\u5173\uff0c\u5f15\u7206\u7206\u70b8\u3002"
        },
        "Conflict.Attack.Unspecified": {
            "event type": "Conflict.Attack.Unspecified",
            "keywords": [],
            "event description": "The event is related to conflict attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} attacked {ROLE_Target} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Attacker",
                "Instrument",
                "Place",
                "Target"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u6709\u5173\u3002"
        },
        "Conflict.Defeat.Unspecified": {
            "event type": "Conflict.Defeat.Unspecified",
            "keywords": [],
            "event description": "The event is related to conflict defeat.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Victor} defeated {ROLE_Defeated} in a conflict in {ROLE_Place}.",
            "valid roles": [
                "Defeated",
                "Place",
                "Victor"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u5931\u8d25\u6709\u5173\u3002"
        },
        "Conflict.Demonstrate.DemonstrateWithViolence": {
            "event type": "Conflict.Demonstrate.DemonstrateWithViolence",
            "keywords": [],
            "event description": "The event is related to conflict demonstrate demonstrate with violence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Demonstrator} was in a demonstration involving violence with involvement of {ROLE_Regulator}.",
            "valid roles": [
                "Demonstrator",
                "Regulator"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u6709\u5173\u3002"
        },
        "Conflict.Demonstrate.Unspecified": {
            "event type": "Conflict.Demonstrate.Unspecified",
            "keywords": [],
            "event description": "The event is related to conflict demonstrate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Demonstrator} was in a demonstration for {ROLE_Topic} against {ROLE_Target}.",
            "valid roles": [
                "Demonstrator",
                "Target",
                "Topic"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u793a\u5a01\u6709\u5173\u3002"
        },
        "Contact.Contact.Broadcast": {
            "event type": "Contact.Contact.Broadcast",
            "keywords": [],
            "event description": "The event is related to contact contact broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} broadcasted {ROLE_Recipient} about {ROLE_Topic} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": [
                "Communicator",
                "Instrument",
                "Place",
                "Recipient",
                "Topic"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u4eba\u8054\u7cfb\u4eba\u5e7f\u64ad\u76f8\u5173\u3002"
        },
        "Contact.Contact.Correspondence": {
            "event type": "Contact.Contact.Correspondence",
            "keywords": [],
            "event description": "The event is related to contact contact correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Participant} contacted {ROLE_Participant} with correspondence about {ROLE_Topic} in {ROLE_Place}.",
            "valid roles": [
                "Participant",
                "Place",
                "Topic"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u63a5\u89e6\u901a\u4fe1\u6709\u5173\u3002"
        },
        "Contact.Contact.Meet": {
            "event type": "Contact.Contact.Meet",
            "keywords": [],
            "event description": "The event is related to contact contact meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Participant} contacted {ROLE_Participant} with meeting about {ROLE_Topic} in {ROLE_Place}.",
            "valid roles": [
                "Participant",
                "Place",
                "Topic"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u63a5\u89e6\u4f1a\u8bae\u6709\u5173\u3002"
        },
        "Contact.Contact.Unspecified": {
            "event type": "Contact.Contact.Unspecified",
            "keywords": [],
            "event description": "The event is related to contact contact.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Participant} contacted {ROLE_Participant} about {ROLE_Topic} in {ROLE_Place}.",
            "valid roles": [
                "Participant",
                "Place",
                "Topic"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u65b9\u5f0f\u6709\u5173\u3002"
        },
        "Contact.RequestCommand.Broadcast": {
            "event type": "Contact.RequestCommand.Broadcast",
            "keywords": [],
            "event description": "The event is related to contact request command broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} requested {ROLE_Recipient} for a broadcast.",
            "valid roles": [
                "Communicator",
                "Recipient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8bf7\u6c42\u547d\u4ee4\u5e7f\u64ad\u76f8\u5173\u3002"
        },
        "Contact.RequestCommand.Correspondence": {
            "event type": "Contact.RequestCommand.Correspondence",
            "keywords": [],
            "event description": "The event is related to contact request command correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} requested {ROLE_Recipient} for a correspondence about {ROLE_Topic}.",
            "valid roles": [
                "Communicator",
                "Recipient",
                "Topic"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8bf7\u6c42\u547d\u4ee4\u901a\u4fe1\u6709\u5173\u3002"
        },
        "Contact.RequestCommand.Meet": {
            "event type": "Contact.RequestCommand.Meet",
            "keywords": [],
            "event description": "The event is related to contact request command meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} requested {ROLE_Recipient} for a meeting.",
            "valid roles": [
                "Communicator",
                "Recipient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u4eba\u8bf7\u6c42\u547d\u4ee4\u4f1a\u8bae\u76f8\u5173\u3002"
        },
        "Contact.RequestCommand.Unspecified": {
            "event type": "Contact.RequestCommand.Unspecified",
            "keywords": [],
            "event description": "The event is related to contact request command.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} requested {ROLE_Recipient} in {ROLE_Place}.",
            "valid roles": [
                "Communicator",
                "Place",
                "Recipient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8bf7\u6c42\u547d\u4ee4\u76f8\u5173\u3002"
        },
        "Contact.ThreatenCoerce.Broadcast": {
            "event type": "Contact.ThreatenCoerce.Broadcast",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} threatened or coerced {ROLE_Recipient} by a broadcast.",
            "valid roles": [
                "Communicator",
                "Recipient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u5a01\u80c1\u80c1\u8feb\u5e7f\u64ad\u6709\u5173\u3002"
        },
        "Contact.ThreatenCoerce.Correspondence": {
            "event type": "Contact.ThreatenCoerce.Correspondence",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} threatened or coerced {ROLE_Recipient} by a correspondence.",
            "valid roles": [
                "Communicator",
                "Recipient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u3001\u5a01\u80c1\u3001\u80c1\u8feb\u901a\u4fe1\u6709\u5173\u3002"
        },
        "Contact.ThreatenCoerce.Unspecified": {
            "event type": "Contact.ThreatenCoerce.Unspecified",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} threatened or coerced {ROLE_Recipient}.",
            "valid roles": [
                "Communicator",
                "Recipient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u3001\u5a01\u80c1\u3001\u80c1\u8feb\u6709\u5173\u3002"
        },
        "Control.ImpedeInterfereWith.Unspecified": {
            "event type": "Control.ImpedeInterfereWith.Unspecified",
            "keywords": [],
            "event description": "The event is related to control impede interfere with.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Impeder} impeded or interfered in {ROLE_Place}.",
            "valid roles": [
                "Impeder",
                "Place"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u63a7\u5236\u3001\u963b\u788d\u3001\u5e72\u6270\u6709\u5173\u3002"
        },
        "Disaster.Crash.Unspecified": {
            "event type": "Disaster.Crash.Unspecified",
            "keywords": [],
            "event description": "The event is related to disaster crash.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Vehicle} crashed into {ROLE_CrashObject} in {ROLE_Place}.",
            "valid roles": [
                "CrashObject",
                "Place",
                "Vehicle"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u7a7a\u96be\u6709\u5173\u3002"
        },
        "Disaster.DiseaseOutbreak.Unspecified": {
            "event type": "Disaster.DiseaseOutbreak.Unspecified",
            "keywords": [],
            "event description": "The event is related to disaster disease outbreak.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Disease broke out among {ROLE_Victim} in {ROLE_Place}.",
            "valid roles": [
                "Place",
                "Victim"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u707e\u5bb3\u75be\u75c5\u66b4\u53d1\u6709\u5173\u3002"
        },
        "GenericCrime.GenericCrime.GenericCrime": {
            "event type": "GenericCrime.GenericCrime.GenericCrime",
            "keywords": [],
            "event description": "The event is related to generic crime generic crime generic crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Perpetrator} committed a crime against {ROLE_Victim} in {ROLE_Place}.",
            "valid roles": [
                "Perpetrator",
                "Place",
                "Victim"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u4e00\u822c\u72af\u7f6a\u4e00\u822c\u72af\u7f6a\u4e00\u822c\u72af\u7f6a\u3002"
        },
        "Justice.Acquit.Unspecified": {
            "event type": "Justice.Acquit.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice acquit.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Judge court acquitted {ROLE_Defendant} of a crime.",
            "valid roles": [
                "Defendant"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u65e0\u7f6a\u91ca\u653e\u6709\u5173\u3002"
        },
        "Justice.ArrestJailDetain.Unspecified": {
            "event type": "Justice.ArrestJailDetain.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice arrest jail detain.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Jailer} arrested or jailed {ROLE_Detainee} for a crime in {ROLE_Place}.",
            "valid roles": [
                "Detainee",
                "Jailer",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u53f8\u6cd5\u902e\u6355\u3001\u76d1\u72f1\u62d8\u7559\u3002"
        },
        "Justice.ChargeIndict.Unspecified": {
            "event type": "Justice.ChargeIndict.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice charge indict.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Prosecutor} charged or indicted {ROLE_Defendant} before {ROLE_JudgeCourt} for a crime in {ROLE_Place}.",
            "valid roles": [
                "Defendant",
                "JudgeCourt",
                "Place",
                "Prosecutor"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u6307\u63a7\u548c\u8d77\u8bc9\u6709\u5173\u3002"
        },
        "Justice.Convict.Unspecified": {
            "event type": "Justice.Convict.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice convict.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_JudgeCourt} convicted {ROLE_Defendant} of a crime.",
            "valid roles": [
                "Defendant",
                "JudgeCourt"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u7f6a\u72af\u6709\u5173\u3002"
        },
        "Justice.InvestigateCrime.Unspecified": {
            "event type": "Justice.InvestigateCrime.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice investigate crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Investigator} investigated {ROLE_Defendant} for a crime and {ROLE_Observer} observed {ROLE_ObservedEntity} in {ROLE_Place}.",
            "valid roles": [
                "Defendant",
                "Investigator",
                "ObservedEntity",
                "Observer",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u6d89\u53ca\u53f8\u6cd5\u8c03\u67e5\u72af\u7f6a\u3002"
        },
        "Justice.ReleaseParole.Unspecified": {
            "event type": "Justice.ReleaseParole.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice release parole.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_JudgeCourt} released or paroled {ROLE_Defendant} from a crime.",
            "valid roles": [
                "Defendant",
                "JudgeCourt"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u91ca\u653e\u5047\u91ca\u6709\u5173\u3002"
        },
        "Justice.Sentence.Unspecified": {
            "event type": "Justice.Sentence.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice sentence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_JudgeCourt} sentenced {ROLE_Defendant} for a crime to sentence in {ROLE_Place}.",
            "valid roles": [
                "Defendant",
                "JudgeCourt",
                "Place"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u5224\u51b3\u6709\u5173\u3002"
        },
        "Justice.TrialHearing.Unspecified": {
            "event type": "Justice.TrialHearing.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice trial hearing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Prosecutor} tried {ROLE_Defendant} before {ROLE_JudgeCourt} for a crime in {ROLE_Place}.",
            "valid roles": [
                "Defendant",
                "JudgeCourt",
                "Place",
                "Prosecutor"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u5ba1\u5224\u542c\u8bc1\u4f1a\u6709\u5173\u3002"
        },
        "Life.Die.Unspecified": {
            "event type": "Life.Die.Unspecified",
            "keywords": [],
            "event description": "The event is related to life die.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Victim} was killed by {ROLE_Killer} in {ROLE_Place}.",
            "valid roles": [
                "Killer",
                "Place",
                "Victim"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u751f\u547d\u6b7b\u4ea1\u6709\u5173\u3002"
        },
        "Life.Infect.Unspecified": {
            "event type": "Life.Infect.Unspecified",
            "keywords": [],
            "event description": "The event is related to life infect.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Victim} was infected.",
            "valid roles": [
                "Victim"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u751f\u547d\u611f\u67d3\u6709\u5173\u3002"
        },
        "Life.Injure.Unspecified": {
            "event type": "Life.Injure.Unspecified",
            "keywords": [],
            "event description": "The event is related to life injure.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Victim} was injured regarding {ROLE_BodyPart} by {ROLE_Injurer} by using {ROLE_Instrument}.",
            "valid roles": [
                "BodyPart",
                "Injurer",
                "Instrument",
                "Victim"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u6d89\u53ca\u4eba\u8eab\u4f24\u5bb3\u3002"
        },
        "Medical.Intervention.Unspecified": {
            "event type": "Medical.Intervention.Unspecified",
            "keywords": [],
            "event description": "The event is related to medical intervention.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Treater} treated {ROLE_Patient} in {ROLE_Place}.",
            "valid roles": [
                "Patient",
                "Place",
                "Treater"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u533b\u7597\u5e72\u9884\u6709\u5173\u3002"
        },
        "Movement.Transportation.Evacuation": {
            "event type": "Movement.Transportation.Evacuation",
            "keywords": [],
            "event description": "The event is related to movement transportation evacuation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Transporter} evacuated with {ROLE_PassengerArtifact} from {ROLE_Origin} to {ROLE_Destination}.",
            "valid roles": [
                "Destination",
                "Origin",
                "PassengerArtifact",
                "Transporter"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u3001\u4ea4\u901a\u3001\u758f\u6563\u6709\u5173\u3002"
        },
        "Movement.Transportation.IllegalTransportation": {
            "event type": "Movement.Transportation.IllegalTransportation",
            "keywords": [],
            "event description": "The event is related to movement transportation illegal transportation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Transporter} illegally transported {ROLE_PassengerArtifact} with {ROLE_Vehicle} to {ROLE_Destination}.",
            "valid roles": [
                "Destination",
                "PassengerArtifact",
                "Transporter",
                "Vehicle"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u8fd0\u8f93\u975e\u6cd5\u8fd0\u8f93\u6709\u5173\u3002"
        },
        "Movement.Transportation.PreventPassage": {
            "event type": "Movement.Transportation.PreventPassage",
            "keywords": [],
            "event description": "The event is related to movement transportation prevent passage.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Preventer} prevented {ROLE_Transporter} from entering {ROLE_Destination} from {ROLE_Origin} to transport {ROLE_PassengerArtifact} with {ROLE_Vehicle}.",
            "valid roles": [
                "Destination",
                "Origin",
                "PassengerArtifact",
                "Preventer",
                "Transporter",
                "Vehicle"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u8fd0\u8f93\u6709\u5173\uff0c\u9632\u6b62\u901a\u884c\u3002"
        },
        "Movement.Transportation.Unspecified": {
            "event type": "Movement.Transportation.Unspecified",
            "keywords": [],
            "event description": "The event is related to movement transportation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Transporter} transported {ROLE_PassengerArtifact} with {ROLE_Vehicle} from {ROLE_Origin} to {ROLE_Destination}.",
            "valid roles": [
                "Destination",
                "Origin",
                "PassengerArtifact",
                "Transporter",
                "Vehicle"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u8fd0\u8f93\u6709\u5173\u3002"
        },
        "Personnel.EndPosition.Unspecified": {
            "event type": "Personnel.EndPosition.Unspecified",
            "keywords": [],
            "event description": "The event is related to personnel end position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Employee} stopped working at {ROLE_PlaceOfEmployment}.",
            "valid roles": [
                "Employee",
                "PlaceOfEmployment"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u672b\u7aef\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "Personnel.StartPosition.Unspecified": {
            "event type": "Personnel.StartPosition.Unspecified",
            "keywords": [],
            "event description": "The event is related to personnel start position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Employee} started working in {ROLE_Position} at {ROLE_PlaceOfEmployment} in {ROLE_Place}.",
            "valid roles": [
                "Employee",
                "Place",
                "PlaceOfEmployment",
                "Position"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u542f\u52a8\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "Transaction.Donation.Unspecified": {
            "event type": "Transaction.Donation.Unspecified",
            "keywords": [],
            "event description": "The event is related to transaction donation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} gave {ROLE_ArtifactMoney} to {ROLE_Recipient}.",
            "valid roles": [
                "ArtifactMoney",
                "Giver",
                "Recipient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u6350\u8d60\u6709\u5173\u3002"
        },
        "Transaction.ExchangeBuySell.Unspecified": {
            "event type": "Transaction.ExchangeBuySell.Unspecified",
            "keywords": [],
            "event description": "The event is related to transaction exchange buy sell.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} sold or traded {ROLE_AcquiredEntity} to {ROLE_Recipient} in exchange for {ROLE_PaymentBarter}.",
            "valid roles": [
                "AcquiredEntity",
                "Giver",
                "PaymentBarter",
                "Recipient"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u4ea4\u6362\u4e70\u5356\u6709\u5173\u3002"
        }
    },
    "fewevent": {
        "Business.Collaboration": {
            "event description": "The event is related to business collaboration.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e1a\u52a1\u534f\u4f5c\u6709\u5173\u3002"
        },
        "Business.Declare-Bankruptcy": {
            "event description": "The event is related to business declare bankruptcy.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u6d89\u53ca\u4f01\u4e1a\u5ba3\u5e03\u7834\u4ea7\u3002"
        },
        "Business.Employment": {
            "event description": "The event is related to business employment.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u5546\u4e1a\u5c31\u4e1a\u6709\u5173\u3002"
        },
        "Business.Employment-Tenure": {
            "event description": "The event is related to business employment tenure.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4f01\u4e1a\u96c7\u4f63\u4efb\u671f\u6709\u5173\u3002"
        },
        "Business.End-Org": {
            "event description": "The event is related to business end organization.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e1a\u52a1\u7aef\u7ec4\u7ec7\u76f8\u5173\u3002"
        },
        "Business.Financing": {
            "event description": "The event is related to business financing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4f01\u4e1a\u878d\u8d44\u6709\u5173\u3002"
        },
        "Business.Investment": {
            "event description": "The event is related to business investment.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u5546\u4e1a\u6295\u8d44\u6709\u5173\u3002"
        },
        "Business.Layoff": {
            "event description": "The event is related to business layoff.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4f01\u4e1a\u88c1\u5458\u6709\u5173\u3002"
        },
        "Business.Merge-Org": {
            "event description": "The event is related to business merge organization.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e1a\u52a1\u5408\u5e76\u7ec4\u7ec7\u6709\u5173\u3002"
        },
        "Business.Sponsorship": {
            "event description": "The event is related to business sponsorship.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u6b21\u6d3b\u52a8\u4e0e\u5546\u4e1a\u8d5e\u52a9\u6709\u5173\u3002"
        },
        "Business.Start-Org": {
            "event description": "The event is related to business start organization.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u521b\u4e1a\u7ec4\u7ec7\u6709\u5173\u3002"
        },
        "Business.Start-Subsidiary": {
            "event description": "The event is related to business start subsidiary.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u516c\u53f8\u6210\u7acb\u5b50\u516c\u53f8\u6709\u5173\u3002"
        },
        "Conflict.Attack": {
            "event description": "The event is related to conflict attack.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u653b\u51fb\u6709\u5173\u3002"
        },
        "Conflict.Demonstrate": {
            "event description": "The event is related to conflict demonstrate.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u793a\u5a01\u6709\u5173\u3002"
        },
        "Conflict.Riot": {
            "event description": "The event is related to conflict riot.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u9a9a\u4e71\u6709\u5173\u3002"
        },
        "Conflict.Self-Immolation": {
            "event description": "The event is related to conflict self immolation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u51b2\u7a81\u81ea\u711a\u6709\u5173\u3002"
        },
        "Contact.Broadcast": {
            "event description": "The event is related to contact broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u4eba\u5e7f\u64ad\u76f8\u5173\u3002"
        },
        "Contact.Contact": {
            "event description": "The event is related to contact contact.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u65b9\u5f0f\u6709\u5173\u3002"
        },
        "Contact.Correspondence": {
            "event description": "The event is related to contact correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u901a\u4fe1\u6709\u5173\u3002"
        },
        "Contact.E-Mail": {
            "event description": "The event is related to contact e mail.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u90ae\u7bb1\u6709\u5173\u3002"
        },
        "Contact.Letter-Communication": {
            "event description": "The event is related to contact letter communication.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u4fe1\u4ef6\u901a\u4fe1\u6709\u5173\u3002"
        },
        "Contact.Meet": {
            "event description": "The event is related to contact meet.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a5\u89e6\u4f1a\u8bae\u6709\u5173\u3002"
        },
        "Contact.Online-Chat": {
            "event description": "The event is related to contact online chat.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u4eba\u5728\u7ebf\u804a\u5929\u6709\u5173\u3002"
        },
        "Contact.Phone-Write": {
            "event description": "The event is related to contact phone write.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u7535\u8bdd\u5199\u6709\u5173\u3002"
        },
        "Contact.Video-Chat": {
            "event description": "The event is related to contact video chat.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u4eba\u89c6\u9891\u804a\u5929\u76f8\u5173\u3002"
        },
        "Contact.Voice-Mail": {
            "event description": "The event is related to contact voice mail.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8054\u7cfb\u8bed\u97f3\u90ae\u4ef6\u76f8\u5173\u3002"
        },
        "Education.Education": {
            "event description": "The event is related to education education.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u6559\u80b2\u6709\u5173\u3002"
        },
        "Film.Dubbing-Performance": {
            "event description": "The event is related to film dubbing performance.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u7535\u5f71\u914d\u97f3\u8868\u6f14\u6709\u5173\u3002"
        },
        "Film.Film-Crew-Gig": {
            "event description": "The event is related to film film crew gig.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u6b21\u6d3b\u52a8\u4e0e\u7535\u5f71\u5267\u7ec4\u7684\u6f14\u51fa\u6709\u5173\u3002"
        },
        "Film.Film-Distribution": {
            "event description": "The event is related to film film distribution.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7535\u5f71\u7535\u5f71\u53d1\u884c\u6709\u5173\u3002"
        },
        "Film.Film-Festival": {
            "event description": "The event is related to film film festival.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u7535\u5f71\u8282\u6709\u5173\u3002"
        },
        "Film.Film-Production": {
            "event description": "The event is related to film film production.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u7535\u5f71\u5236\u4f5c\u6709\u5173\u3002"
        },
        "Justice.Acquit": {
            "event description": "The event is related to justice acquit.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u65e0\u7f6a\u91ca\u653e\u6709\u5173\u3002"
        },
        "Justice.Appeal": {
            "event description": "The event is related to justice appeal.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u4e0a\u8bc9\u6709\u5173\u3002"
        },
        "Justice.Arrest-Jail": {
            "event description": "The event is related to justice arrest jail.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u902e\u6355\u76d1\u72f1\u6709\u5173\u3002"
        },
        "Justice.Charge-Indict": {
            "event description": "The event is related to justice charge indict.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u6307\u63a7\u548c\u8d77\u8bc9\u6709\u5173\u3002"
        },
        "Justice.Convict": {
            "event description": "The event is related to justice convict.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u7f6a\u72af\u6709\u5173\u3002"
        },
        "Justice.Execute": {
            "event description": "The event is related to justice execute.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u6267\u884c\u6709\u5173\u3002"
        },
        "Justice.Extradite": {
            "event description": "The event is related to justice extradite.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u5f15\u6e21\u6709\u5173\u3002"
        },
        "Justice.Fine": {
            "event description": "The event is related to justice fine.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u53f8\u6cd5\u6709\u5173\u3002"
        },
        "Justice.Pardon": {
            "event description": "The event is related to justice pardon.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u8d66\u514d\u6709\u5173\u3002"
        },
        "Justice.Release-Parole": {
            "event description": "The event is related to justice release parole.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u91ca\u653e\u5047\u91ca\u6709\u5173\u3002"
        },
        "Justice.Sentence": {
            "event description": "The event is related to justice sentence.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u5224\u51b3\u6709\u5173\u3002"
        },
        "Justice.Sue": {
            "event description": "The event is related to justice sue.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u4e0e\u53f8\u6cd5\u8bc9\u8bbc\u6709\u5173\u3002"
        },
        "Justice.Trial-Hearing": {
            "event description": "The event is related to justice trial hearing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53f8\u6cd5\u5ba1\u5224\u542c\u8bc1\u4f1a\u6709\u5173\u3002"
        },
        "Life.Abortion": {
            "event description": "The event is related to life abortion.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7ec8\u8eab\u6d41\u4ea7\u6709\u5173\u3002"
        },
        "Life.Be-Born": {
            "event description": "The event is related to life be born.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u751f\u547d\u7684\u8bde\u751f\u6709\u5173\u3002"
        },
        "Life.Die": {
            "event description": "The event is related to life die.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u751f\u547d\u6b7b\u4ea1\u6709\u5173\u3002"
        },
        "Life.Divorce": {
            "event description": "The event is related to life divorce.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u751f\u6d3b\u79bb\u5a5a\u6709\u5173\u3002"
        },
        "Life.Homesick": {
            "event description": "The event is related to life homesick.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4eba\u751f\u601d\u4e61\u6709\u5173\u3002"
        },
        "Life.Injure": {
            "event description": "The event is related to life injure.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u6d89\u53ca\u4eba\u8eab\u4f24\u5bb3\u3002"
        },
        "Life.Marry": {
            "event description": "The event is related to life marry.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4ef6\u4e8b\u5173\u7cfb\u5230\u7ed3\u5a5a\u7684\u4e00\u751f\u3002"
        },
        "Life.Pregnancy": {
            "event description": "The event is related to life pregnancy.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u751f\u547d\u6000\u5b55\u6709\u5173\u3002"
        },
        "Life.Sick": {
            "event description": "The event is related to life sick.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u662f\u4e0e\u751f\u547d\u6709\u5173\u7684\u75be\u75c5\u3002"
        },
        "Life.Travel": {
            "event description": "The event is related to life travel.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u751f\u6d3b\u65c5\u884c\u6709\u5173\u3002"
        },
        "Manufacture.Artifact": {
            "event description": "The event is related to manufacture artifact.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5236\u9020\u5de5\u4ef6\u6709\u5173\u3002"
        },
        "Manufacture.Lean-Manufacturing": {
            "event description": "The event is related to manufacture lean manufacturing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5236\u9020\u7cbe\u76ca\u751f\u4ea7\u6709\u5173\u3002"
        },
        "Military.Military-Command": {
            "event description": "The event is related to military military command.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u519b\u4e8b\u6307\u6325\u6709\u5173\u3002"
        },
        "Military.Military-Service": {
            "event description": "The event is related to military military service.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u5175\u5f79\u6709\u5173\u3002"
        },
        "Military.Recruit-Training": {
            "event description": "The event is related to military recruit training.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u519b\u961f\u65b0\u5175\u8bad\u7ec3\u6709\u5173\u3002"
        },
        "Military.Recruitment": {
            "event description": "The event is related to military recruitment.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u5f81\u5175\u6709\u5173\u3002"
        },
        "Movement.Driving": {
            "event description": "The event is related to movement driving.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u9a71\u52a8\u6709\u5173\u3002"
        },
        "Movement.Parking": {
            "event description": "The event is related to movement parking.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u505c\u8f66\u6709\u5173\u3002"
        },
        "Movement.Transport": {
            "event description": "The event is related to movement transport.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u4f20\u8f93\u6709\u5173\u3002"
        },
        "Movement.Transport-Artifact": {
            "event description": "The event is related to movement transport artifact.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u79fb\u52a8\u4f20\u8f93\u5de5\u4ef6\u76f8\u5173\u3002"
        },
        "Movement.Transportperson": {
            "event description": "The event is related to movement transportperson.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8fd0\u52a8\u8fd0\u8f93\u6709\u5173\u3002"
        },
        "Music.Compose": {
            "event description": "The event is related to music compose.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u97f3\u4e50\u521b\u4f5c\u6709\u5173\u3002"
        },
        "Music.Dance": {
            "event description": "The event is related to music dance.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u97f3\u4e50\u821e\u8e48\u6709\u5173\u3002"
        },
        "Music.Group-Membership": {
            "event description": "The event is related to music group membership.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u97f3\u4e50\u56e2\u4f53\u6210\u5458\u6709\u5173\u3002"
        },
        "Music.Sing": {
            "event description": "The event is related to music sing.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u6b21\u6d3b\u52a8\u4e0e\u97f3\u4e50\u6f14\u5531\u6709\u5173\u3002"
        },
        "Music.Track-Contribution": {
            "event description": "The event is related to music track contribution.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u6d3b\u52a8\u4e0e\u97f3\u4e50\u66f2\u76ee\u8d21\u732e\u6709\u5173\u3002"
        },
        "Olympics.Closing-Ceremony": {
            "event description": "The event is related to olympics closing ceremony.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u5965\u8fd0\u4f1a\u95ed\u5e55\u5f0f\u6709\u5173\u3002"
        },
        "Olympics.Olympic-Athlete-Affiliation": {
            "event description": "The event is related to olympics olympic athlete affiliation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u5965\u6797\u5339\u514b\u8fd0\u52a8\u4f1a\u7684\u8fd0\u52a8\u5458\u5173\u7cfb\u6709\u5173\u3002"
        },
        "Olympics.Olympic-Medal-Honor": {
            "event description": "The event is related to olympics olympic medal honor.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u9879\u76ee\u5173\u7cfb\u5230\u5965\u8fd0\u4f1a\u7684\u5956\u724c\u8363\u8a89\u3002"
        },
        "Olympics.Opening-Ceremony": {
            "event description": "The event is related to olympics opening ceremony.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u5965\u8fd0\u4f1a\u5f00\u5e55\u5f0f\u6709\u5173\u3002"
        },
        "Organization.Division-Of-Labour": {
            "event description": "The event is related to organization division of labour.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u7ec4\u7ec7\u5206\u5de5\u6709\u5173\u3002"
        },
        "Organization.Leadership": {
            "event description": "The event is related to organization leadership.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u7ec4\u7ec7\u9886\u5bfc\u6709\u5173\u3002"
        },
        "Organization.Org-Communication": {
            "event description": "The event is related to organization org communication.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7ec4\u7ec7\u6c9f\u901a\u6709\u5173\u3002"
        },
        "Organization.Organization-Board-Membership": {
            "event description": "The event is related to organization organization board membership.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7ec4\u7ec7\u673a\u6784\u8463\u4e8b\u4f1a\u6210\u5458\u6709\u5173\u3002"
        },
        "People.Appointment": {
            "event description": "The event is related to people appointment.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4eba\u7684\u7ea6\u4f1a\u6709\u5173\u3002"
        },
        "People.Place-Lived": {
            "event description": "The event is related to people place lived.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4eba\u4eec\u5c45\u4f4f\u7684\u5730\u65b9\u6709\u5173\u3002"
        },
        "Personnel.Demotion": {
            "event description": "The event is related to personnel demotion.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4eba\u5458\u964d\u7ea7\u6709\u5173\u3002"
        },
        "Personnel.Elect": {
            "event description": "The event is related to personnel elect.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4eba\u4e8b\u9009\u4e3e\u6709\u5173\u3002"
        },
        "Personnel.End-Position": {
            "event description": "The event is related to personnel end position.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u672b\u7aef\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "Personnel.Nominate": {
            "event description": "The event is related to personnel nominate.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u4e8b\u63d0\u540d\u6709\u5173\u3002"
        },
        "Personnel.Performance-Appraisal": {
            "event description": "The event is related to personnel performance appraisal.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u7ee9\u6548\u8003\u6838\u6709\u5173\u3002"
        },
        "Personnel.Promotion": {
            "event description": "The event is related to personnel promotion.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u6b21\u6d3b\u52a8\u4e0e\u4eba\u4e8b\u664b\u5347\u6709\u5173\u3002"
        },
        "Personnel.Resignation": {
            "event description": "The event is related to personnel resignation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u4e8b\u8f9e\u804c\u6709\u5173\u3002"
        },
        "Personnel.Start-Position": {
            "event description": "The event is related to personnel start position.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4eba\u5458\u542f\u52a8\u4f4d\u7f6e\u6709\u5173\u3002"
        },
        "Projects.Project-Participation": {
            "event description": "The event is related to projects project participation.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u662f\u4e0e\u9879\u76ee\u6709\u5173\u7684\u9879\u76ee\u53c2\u4e0e\u3002"
        },
        "Sports.Fair-Play": {
            "event description": "The event is related to sports fair play.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u9879\u8d5b\u4e8b\u4e0e\u4f53\u80b2\u516c\u5e73\u7ade\u8d5b\u6709\u5173\u3002"
        },
        "Sports.Sports-Team-Roster": {
            "event description": "The event is related to sports sports team roster.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u8d5b\u4e8b\u4e0e\u4f53\u80b2\u8fd0\u52a8\u961f\u82b1\u540d\u518c\u6709\u5173\u3002"
        },
        "Sports.Sports-Team-Season-Record": {
            "event description": "The event is related to sports sports team season record.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u9879\u8d5b\u4e8b\u4e0e\u8fd0\u52a8\u961f\u7684\u8d5b\u5b63\u7eaa\u5f55\u6709\u5173\u3002"
        },
        "Sports.Tournament": {
            "event description": "The event is related to sports tournament.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u6d3b\u52a8\u4e0e\u4f53\u80b2\u6bd4\u8d5b\u6709\u5173\u3002"
        },
        "Transaction.Deposit": {
            "event description": "The event is related to transaction deposit.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u4fdd\u8bc1\u91d1\u6709\u5173\u3002"
        },
        "Transaction.Money-Laundering": {
            "event description": "The event is related to transaction money laundering.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4ea4\u6613\u6d17\u94b1\u6709\u5173\u3002"
        },
        "Transaction.Transaction": {
            "event description": "The event is related to transaction transaction.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u4e8b\u52a1\u76f8\u5173\u3002"
        },
        "Transaction.Transfer-Money": {
            "event description": "The event is related to transaction transfer money.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8f6c\u8d26\u4ea4\u6613\u6709\u5173\u3002"
        },
        "Transaction.Transfer-Ownership": {
            "event description": "The event is related to transaction transfer ownership.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e8b\u52a1\u8f6c\u79fb\u6240\u6709\u6743\u6709\u5173\u3002"
        },
        "Wine.Grape-Variety-Composition": {
            "event description": "The event is related to wine grape variety composition.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u917f\u9152\u8461\u8404\u54c1\u79cd\u7ec4\u6210\u6709\u5173\u3002"
        }
    },
    "phee": {
        "Adverse_event": {
            "event type": "Adverse_event",
            "keywords": [],
            "event description": "The event is related to adverse event.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Combination Drug {ROLE_Combination_Drug} Effect {ROLE_Effect} Subject {ROLE_Subject} Subject Age {ROLE_Subject_Age} Subject Disorder {ROLE_Subject_Disorder} Subject Gender {ROLE_Subject_Gender} Subject Population {ROLE_Subject_Population} Subject Race {ROLE_Subject_Race} Treatment {ROLE_Treatment} Treatment Disorder {ROLE_Treatment_Disorder} Treatment Dosage {ROLE_Treatment_Dosage} Treatment Drug {ROLE_Treatment_Drug} Treatment Duration {ROLE_Treatment_Duration} Treatment Frequency {ROLE_Treatment_Freq} Treatment Route {ROLE_Treatment_Route} Treatment Time Elapsed {ROLE_Treatment_Time_elapsed}.",
            "valid roles": [
                "Combination_Drug",
                "Effect",
                "Subject",
                "Subject_Age",
                "Subject_Disorder",
                "Subject_Gender",
                "Subject_Population",
                "Subject_Race",
                "Treatment",
                "Treatment_Disorder",
                "Treatment_Dosage",
                "Treatment_Drug",
                "Treatment_Duration",
                "Treatment_Freq",
                "Treatment_Route",
                "Treatment_Time_elapsed"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u4e0d\u826f\u4e8b\u4ef6\u6709\u5173\u3002"
        },
        "Potential_therapeutic_event": {
            "event type": "Potential_therapeutic_event",
            "keywords": [],
            "event description": "The event is related to potential therapeutic event.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Combination Drug {ROLE_Combination_Drug} Effect {ROLE_Effect} Subject {ROLE_Subject} Subject Age {ROLE_Subject_Age} Subject Disorder {ROLE_Subject_Disorder} Subject Gender {ROLE_Subject_Gender} Subject Population {ROLE_Subject_Population} Subject Race {ROLE_Subject_Race} Treatment {ROLE_Treatment} Treatment Disorder {ROLE_Treatment_Disorder} Treatment Dosage {ROLE_Treatment_Dosage} Treatment Drug {ROLE_Treatment_Drug} Treatment Duration {ROLE_Treatment_Duration} Treatment Frequency {ROLE_Treatment_Freq} Treatment Route {ROLE_Treatment_Route} Treatment Time Elapsed {ROLE_Treatment_Time_elapsed}.",
            "valid roles": [
                "Combination_Drug",
                "Effect",
                "Subject",
                "Subject_Age",
                "Subject_Disorder",
                "Subject_Gender",
                "Subject_Population",
                "Subject_Race",
                "Treatment",
                "Treatment_Disorder",
                "Treatment_Dosage",
                "Treatment_Drug",
                "Treatment_Duration",
                "Treatment_Freq",
                "Treatment_Route",
                "Treatment_Time_elapsed"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6f5c\u5728\u7684\u6cbb\u7597\u4e8b\u4ef6\u6709\u5173\u3002"
        }
    },
    "casie": {
        "Attack:Databreach": {
            "event type": "Attack:Databreach",
            "keywords": [],
            "event description": "The event is related to attack databreach.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Attack Pattern {ROLE_Attack-Pattern} Attacker {ROLE_Attacker} Compromised Data {ROLE_Compromised-Data} Damage Amount {ROLE_Damage-Amount} Number of Data {ROLE_Number-of-Data} Number of Victim {ROLE_Number-of-Victim} Place {ROLE_Place} Purpose {ROLE_Purpose} Time {ROLE_Time} Tool {ROLE_Tool} Victim {ROLE_Victim}",
            "valid roles": [
                "Attack-Pattern",
                "Attacker",
                "Compromised-Data",
                "Damage-Amount",
                "Number-of-Data",
                "Number-of-Victim",
                "Place",
                "Purpose",
                "Time",
                "Tool",
                "Victim"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653b\u51fbdatabreach\u6709\u5173\u3002"
        },
        "Attack:Phishing": {
            "event type": "Attack:Phishing",
            "keywords": [],
            "event description": "The event is related to attack phishing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Attack Pattern {ROLE_Attack-Pattern} Attacker {ROLE_Attacker} Damage Amount {ROLE_Damage-Amount} Place {ROLE_Place} Purpose {ROLE_Purpose} Time {ROLE_Time} Tool {ROLE_Tool} Trusted Entity {ROLE_Trusted-Entity} Victim {ROLE_Victim}",
            "valid roles": [
                "Attack-Pattern",
                "Attacker",
                "Damage-Amount",
                "Place",
                "Purpose",
                "Time",
                "Tool",
                "Trusted-Entity",
                "Victim"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7f51\u7edc\u9493\u9c7c\u653b\u51fb\u6709\u5173\u3002"
        },
        "Attack:Ransom": {
            "event type": "Attack:Ransom",
            "keywords": [],
            "event description": "The event is related to attack ransom.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Attack Pattern {ROLE_Attack-Pattern} Attacker {ROLE_Attacker} Damage Amount {ROLE_Damage-Amount} Payment Method {ROLE_Payment-Method} Place {ROLE_Place} Price {ROLE_Price} Time {ROLE_Time} Tool {ROLE_Tool} Victim {ROLE_Victim}",
            "valid roles": [
                "Attack-Pattern",
                "Attacker",
                "Damage-Amount",
                "Payment-Method",
                "Place",
                "Price",
                "Time",
                "Tool",
                "Victim"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u653b\u51fb\u8d4e\u91d1\u6709\u5173\u3002"
        },
        "Vulnerability-related:DiscoverVulnerability": {
            "event type": "Vulnerability-related:DiscoverVulnerability",
            "keywords": [],
            "event description": "The event is related to vulnerability-related discover vulnerability.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CVE {ROLE_CVE} Capabilities {ROLE_Capabilities} Discoverer {ROLE_Discoverer} Supported Platform {ROLE_Supported_Platform} Time {ROLE_Time} Vulnerability {ROLE_Vulnerability} Vulnerable System {ROLE_Vulnerable_System} Vulnerable System Owner {ROLE_Vulnerable_System_Owner} Vulnerable System Version {ROLE_Vulnerable_System_Version}",
            "valid roles": [
                "CVE",
                "Capabilities",
                "Discoverer",
                "Supported_Platform",
                "Time",
                "Vulnerability",
                "Vulnerable_System",
                "Vulnerable_System_Owner",
                "Vulnerable_System_Version"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6f0f\u6d1e\u76f8\u5173\u7684\u53d1\u73b0\u6f0f\u6d1e\u3002"
        },
        "Vulnerability-related:PatchVulnerability": {
            "event type": "Vulnerability-related:PatchVulnerability",
            "keywords": [],
            "event description": "The event is related to vulnerability-related patch vulnerability.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CVE {ROLE_CVE} Issues Addressed {ROLE_Issues-Addressed} Patch {ROLE_Patch} Patch Number {ROLE_Patch-Number} Releaser {ROLE_Releaser} Supported Platform {ROLE_Supported_Platform} Time {ROLE_Time} Vulnerability {ROLE_Vulnerability} Vulnerable System {ROLE_Vulnerable_System} Vulnerable System Version {ROLE_Vulnerable_System_Version}",
            "valid roles": [
                "CVE",
                "Issues-Addressed",
                "Patch",
                "Patch-Number",
                "Releaser",
                "Supported_Platform",
                "Time",
                "Vulnerability",
                "Vulnerable_System",
                "Vulnerable_System_Version"
            ],
            "chinese event description": "\u6b64\u4e8b\u4ef6\u4e0e\u6f0f\u6d1e\u76f8\u5173\u7684\u8865\u4e01\u6f0f\u6d1e\u6709\u5173\u3002"
        }
    },
    "mlee": {
        "Acetylation": {
            "event type": "Acetylation",
            "keywords": [],
            "event description": "The event is related to acetylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4e59\u9170\u5316\u6709\u5173\u3002"
        },
        "Binding": {
            "event type": "Binding",
            "keywords": [],
            "event description": "The event is related to binding.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2}",
            "valid roles": [
                "Site",
                "Theme",
                "Theme2"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7ed1\u5b9a\u76f8\u5173\u3002"
        },
        "Blood_vessel_development": {
            "event type": "Blood_vessel_development",
            "keywords": [],
            "event description": "The event is related to blood vessel development.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "At Loc {ROLE_AtLoc} From Loc {ROLE_FromLoc} Theme {ROLE_Theme}",
            "valid roles": [
                "AtLoc",
                "FromLoc",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8840\u7ba1\u53d1\u80b2\u6709\u5173\u3002"
        },
        "Breakdown": {
            "event type": "Breakdown",
            "keywords": [],
            "event description": "The event is related to breakdown.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6545\u969c\u6709\u5173\u3002"
        },
        "Catabolism": {
            "event type": "Catabolism",
            "keywords": [],
            "event description": "The event is related to catabolism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5206\u89e3\u4ee3\u8c22\u6709\u5173\u3002"
        },
        "Cell_division": {
            "event type": "Cell_division",
            "keywords": [],
            "event description": "The event is related to cell division.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u7ec6\u80de\u5206\u88c2\u6709\u5173\u3002"
        },
        "Cell_proliferation": {
            "event type": "Cell_proliferation",
            "keywords": [],
            "event description": "The event is related to cell proliferation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7ec6\u80de\u589e\u6b96\u6709\u5173\u3002"
        },
        "DNA_methylation": {
            "event type": "DNA_methylation",
            "keywords": [],
            "event description": "The event is related to dna methylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0edna\u7532\u57fa\u5316\u6709\u5173\u3002"
        },
        "Death": {
            "event type": "Death",
            "keywords": [],
            "event description": "The event is related to death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6b7b\u4ea1\u6709\u5173\u3002"
        },
        "Dephosphorylation": {
            "event type": "Dephosphorylation",
            "keywords": [],
            "event description": "The event is related to dephosphorylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u53bb\u78f7\u9178\u5316\u6709\u5173\u3002"
        },
        "Development": {
            "event type": "Development",
            "keywords": [],
            "event description": "The event is related to development.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53d1\u5c55\u6709\u5173\u3002"
        },
        "Dissociation": {
            "event type": "Dissociation",
            "keywords": [],
            "event description": "The event is related to dissociation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u89e3\u79bb\u6709\u5173\u3002"
        },
        "Gene_expression": {
            "event type": "Gene_expression",
            "keywords": [],
            "event description": "The event is related to gene expression.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u57fa\u56e0\u8868\u8fbe\u6709\u5173\u3002"
        },
        "Growth": {
            "event type": "Growth",
            "keywords": [],
            "event description": "The event is related to growth.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u589e\u957f\u6709\u5173\u3002"
        },
        "Localization": {
            "event type": "Localization",
            "keywords": [],
            "event description": "The event is related to localization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "At Loc {ROLE_AtLoc} From Loc {ROLE_FromLoc} Theme {ROLE_Theme} To Loc {ROLE_ToLoc}",
            "valid roles": [
                "AtLoc",
                "FromLoc",
                "Theme",
                "ToLoc"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u672c\u5730\u5316\u76f8\u5173\u3002"
        },
        "Metabolism": {
            "event type": "Metabolism",
            "keywords": [],
            "event description": "The event is related to metabolism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u65b0\u9648\u4ee3\u8c22\u6709\u5173\u3002"
        },
        "Negative_regulation": {
            "event type": "Negative_regulation",
            "keywords": [],
            "event description": "The event is related to negative regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8d1f\u9762\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Pathway": {
            "event type": "Pathway",
            "keywords": [],
            "event description": "The event is related to pathway.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Participant {ROLE_Participant} Participant 2 {ROLE_Participant2} Participant 3 {ROLE_Participant3} Participant 4 {ROLE_Participant4}",
            "valid roles": [
                "Participant",
                "Participant2",
                "Participant3",
                "Participant4"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u901a\u8def\u6709\u5173\u3002"
        },
        "Phosphorylation": {
            "event type": "Phosphorylation",
            "keywords": [],
            "event description": "The event is related to phosphorylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u78f7\u9178\u5316\u6709\u5173\u3002"
        },
        "Planned_process": {
            "event type": "Planned_process",
            "keywords": [],
            "event description": "The event is related to planned process.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Instrument {ROLE_Instrument} Instrument 2 {ROLE_Instrument2} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2}",
            "valid roles": [
                "Instrument",
                "Instrument2",
                "Theme",
                "Theme2"
            ],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u8ba1\u5212\u8fc7\u7a0b\u76f8\u5173\u3002"
        },
        "Positive_regulation": {
            "event type": "Positive_regulation",
            "keywords": [],
            "event description": "The event is related to positive regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme",
                "Theme2"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u79ef\u6781\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Protein_processing": {
            "event type": "Protein_processing",
            "keywords": [],
            "event description": "The event is related to protein processing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u86cb\u767d\u8d28\u52a0\u5de5\u6709\u5173\u3002"
        },
        "Regulation": {
            "event type": "Regulation",
            "keywords": [],
            "event description": "The event is related to regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Remodeling": {
            "event type": "Remodeling",
            "keywords": [],
            "event description": "The event is related to remodeling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u91cd\u5851\u6709\u5173\u3002"
        },
        "Reproduction": {
            "event type": "Reproduction",
            "keywords": [],
            "event description": "The event is related to reproduction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u751f\u6b96\u6709\u5173\u3002"
        },
        "Synthesis": {
            "event type": "Synthesis",
            "keywords": [],
            "event description": "The event is related to synthesis.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u5408\u6210\u6709\u5173\u3002"
        },
        "Transcription": {
            "event type": "Transcription",
            "keywords": [],
            "event description": "The event is related to transcription.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u8f6c\u5f55\u6709\u5173\u3002"
        },
        "Translation": {
            "event type": "Translation",
            "keywords": [],
            "event description": "The event is related to translation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7ffb\u8bd1\u6709\u5173\u3002"
        },
        "Ubiquitination": {
            "event type": "Ubiquitination",
            "keywords": [],
            "event description": "The event is related to ubiquitination.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6cdb\u7d20\u5316\u6709\u5173\u3002"
        }
    },
    "genia2011": {
        "Binding": {
            "event type": "Binding",
            "keywords": [],
            "event description": "The event is related to binding.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Site 2 {ROLE_Site2} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2} Theme 3 {ROLE_Theme3} Theme 4 {ROLE_Theme4}",
            "valid roles": [
                "Site",
                "Site2",
                "Theme",
                "Theme2",
                "Theme3",
                "Theme4"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7ed1\u5b9a\u76f8\u5173\u3002"
        },
        "Gene_expression": {
            "event type": "Gene_expression",
            "keywords": [],
            "event description": "The event is related to gene expression.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u57fa\u56e0\u8868\u8fbe\u6709\u5173\u3002"
        },
        "Localization": {
            "event type": "Localization",
            "keywords": [],
            "event description": "The event is related to localization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "At Loc {ROLE_AtLoc} Theme {ROLE_Theme} To Loc {ROLE_ToLoc}",
            "valid roles": [
                "AtLoc",
                "Theme",
                "ToLoc"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u672c\u5730\u5316\u76f8\u5173\u3002"
        },
        "Negative_regulation": {
            "event type": "Negative_regulation",
            "keywords": [],
            "event description": "The event is related to negative regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8d1f\u9762\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Phosphorylation": {
            "event type": "Phosphorylation",
            "keywords": [],
            "event description": "The event is related to phosphorylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u78f7\u9178\u5316\u6709\u5173\u3002"
        },
        "Positive_regulation": {
            "event type": "Positive_regulation",
            "keywords": [],
            "event description": "The event is related to positive regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u79ef\u6781\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Protein_catabolism": {
            "event type": "Protein_catabolism",
            "keywords": [],
            "event description": "The event is related to protein catabolism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u86cb\u767d\u8d28\u5206\u89e3\u4ee3\u8c22\u6709\u5173\u3002"
        },
        "Regulation": {
            "event type": "Regulation",
            "keywords": [],
            "event description": "The event is related to regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Transcription": {
            "event type": "Transcription",
            "keywords": [],
            "event description": "The event is related to transcription.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u8f6c\u5f55\u6709\u5173\u3002"
        }
    },
    "genia2013": {
        "Acetylation": {
            "event type": "Acetylation",
            "keywords": [],
            "event description": "The event is related to acetylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u4e59\u9170\u5316\u6709\u5173\u3002"
        },
        "Binding": {
            "event type": "Binding",
            "keywords": [],
            "event description": "The event is related to binding.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Site 2 {ROLE_Site2} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2}",
            "valid roles": [
                "Site",
                "Site2",
                "Theme",
                "Theme2"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u7ed1\u5b9a\u76f8\u5173\u3002"
        },
        "Deacetylation": {
            "event type": "Deacetylation",
            "keywords": [],
            "event description": "The event is related to deacetylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u53bb\u4e59\u9170\u5316\u6709\u5173\u3002"
        },
        "Gene_expression": {
            "event type": "Gene_expression",
            "keywords": [],
            "event description": "The event is related to gene expression.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u57fa\u56e0\u8868\u8fbe\u6709\u5173\u3002"
        },
        "Localization": {
            "event type": "Localization",
            "keywords": [],
            "event description": "The event is related to localization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme} To Loc {ROLE_ToLoc}",
            "valid roles": [
                "Theme",
                "ToLoc"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u672c\u5730\u5316\u76f8\u5173\u3002"
        },
        "Negative_regulation": {
            "event type": "Negative_regulation",
            "keywords": [],
            "event description": "The event is related to negative regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u8d1f\u9762\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Phosphorylation": {
            "event type": "Phosphorylation",
            "keywords": [],
            "event description": "The event is related to phosphorylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u78f7\u9178\u5316\u6709\u5173\u3002"
        },
        "Positive_regulation": {
            "event type": "Positive_regulation",
            "keywords": [],
            "event description": "The event is related to positive regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u79ef\u6781\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Protein_catabolism": {
            "event type": "Protein_catabolism",
            "keywords": [],
            "event description": "The event is related to protein catabolism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u86cb\u767d\u8d28\u5206\u89e3\u4ee3\u8c22\u6709\u5173\u3002"
        },
        "Protein_modification": {
            "event type": "Protein_modification",
            "keywords": [],
            "event description": "The event is related to protein modification.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u86cb\u767d\u8d28\u4fee\u9970\u6709\u5173\u3002"
        },
        "Regulation": {
            "event type": "Regulation",
            "keywords": [],
            "event description": "The event is related to regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "CSite",
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u76d1\u7ba1\u6709\u5173\u3002"
        },
        "Transcription": {
            "event type": "Transcription",
            "keywords": [],
            "event description": "The event is related to transcription.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": [
                "Theme"
            ],
            "chinese event description": "\u8fd9\u4e00\u4e8b\u4ef6\u4e0e\u8f6c\u5f55\u6709\u5173\u3002"
        },
        "Ubiquitination": {
            "event type": "Ubiquitination",
            "keywords": [],
            "event description": "The event is related to ubiquitination.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": [
                "Cause",
                "Site",
                "Theme"
            ],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6cdb\u7d20\u5316\u6709\u5173\u3002"
        }
    },
    "speed": {
        "control": {
            "event type": "Control",
            "keywords": [],
            "event description": "The event is related to control.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u63a7\u5236\u6709\u5173\u3002"
        },
        "cure": {
            "event type": "Cure",
            "keywords": [],
            "event description": "The event is related to cure.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u6cbb\u7597\u6709\u5173\u3002"
        },
        "death": {
            "event type": "Death",
            "keywords": [],
            "event description": "The event is related to death.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8fd9\u4e2a\u4e8b\u4ef6\u4e0e\u6b7b\u4ea1\u6709\u5173\u3002"
        },
        "infect": {
            "event type": "Infect",
            "keywords": [],
            "event description": "The event is related to infect.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u8be5\u4e8b\u4ef6\u4e0e\u611f\u67d3\u6709\u5173\u3002"
        },
        "prevent": {
            "event type": "Prevent",
            "keywords": [],
            "event description": "The event is related to prevent.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u9884\u9632\u6709\u5173\u3002"
        },
        "spread": {
            "event type": "Spread",
            "keywords": [],
            "event description": "The event is related to spread.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u4f20\u64ad\u6709\u5173\u3002"
        },
        "symptom": {
            "event type": "Symptom",
            "keywords": [],
            "event description": "The event is related to symptom.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
            "chinese event description": "\u4e8b\u4ef6\u4e0e\u75c7\u72b6\u76f8\u5173\u3002"
        }
    },
    "muc4": {
        "Dummy": {
            "event type": "Dummy",
            "keywords": [],
            "event description": "This is a event.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "PerpInd {ROLE_PerpInd} PerpOrg {ROLE_PerpOrg} Target {ROLE_Target} Victim {ROLE_Victim} Weapon {ROLE_Weapon}",
            "valid roles": [
                "PerpInd",
                "PerpOrg",
                "Target",
                "Victim",
                "Weapon"
            ],
            "chinese event description": "\u8fd9\u662f\u4e00\u4e2a\u4e8b\u4ef6\u3002"
        }
    }
}

patterns_0730 = {
    "ace05": {
        "Business:Declare-Bankruptcy": {
            "event subtype": "declare bankruptcy",
            "event type": "Business:Declare-Bankruptcy",
            "keywords": ['bankruptcy', 'bankrupt', 'Bankruptcy'],
            "event description": "The event is related to some organization declaring bankruptcy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} declared bankruptcy.",
            "valid roles": ["Org"],
        },
        "Business:End-Org": {
            "event subtype": "end organization",
            "event type": "Business:End-Org",
            "keywords": ['dissolve', 'disbanded', 'close'],
            "event description": "The event is related to some organization ceasing to exist.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} dissolved at {ROLE_Place}.",
            "valid roles": ["Org", "Place"],
        },
        "Business:Merge-Org": {
            "event subtype": "merge organization",
            "event type": "Business:Merge-Org",
            "keywords": ['merge', 'merging', 'merger'],
            "event description": "The event is related to two or more organization coming together to form a new organization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} was merged.",
            "valid roles": ["Org"],
        },
        "Business:Start-Org": {
            "event subtype": "start organization",
            "event type": "Business:Start-Org",
            "keywords": ['founded', 'create', 'launch'],
            "event description": "The event is related to a new organization being created.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} launched {ROLE_Org} in {ROLE_Place}.",
            "valid roles": ["Agent", "Org", "Place"],
        },
        "Conflict:Attack": {
            "event subtype": "attack",
            "event type": "Conflict:Attack",
            "keywords": ['war', 'attack', 'terrorism'],
            "event description": "The event is related to conflict and some violent physical act.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} attacked {ROLE_Target} by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ["Attacker", "Target", "Instrument", "Place", "Agent"],
        },
        "Conflict:Demonstrate": {
            "event subtype": "demonstrate",
            "event type": "Conflict:Demonstrate",
            "keywords": ['rally', 'protest', 'demonstrate'],
            "event description": "The event is related to a large number of people coming together to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} protested at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Contact:Meet": {
            "event subtype": "meet",
            "event type": "Contact:Meet",
            "keywords": ['meeting', 'met', 'summit'],
            "event description": "The event is related to a group of people meeting and interacting with one another face-to-face.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} met at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Contact:Phone-Write": {
            "event subtype": "phone write",
            "event type": "Contact:Phone-Write",
            "keywords": ['call', 'communicate', 'e-mail'],
            "event description": "The event is related to people phone calling or messaging one another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} called or texted messages at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Justice:Acquit": {
            "event subtype": "acquit",
            "event type": "Justice:Acquit",
            "keywords": ['acquitted', 'acquittal', 'acquit'],
            "event description": "The event is related to someone being acquitted.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was acquitted of the charges by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Adjudicator"],
        },
        "Justice:Appeal": {
            "event subtype": "appeal",
            "event type": "Justice:Appeal",
            "keywords": ['appeal', 'appealing', 'appeals'],
            "event description": "The event is related to someone appealing the decision of a court.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Plaintiff} in {ROLE_Place} appealed the adjudication from {ROLE_Adjudicator}.",
            "valid roles": ["Plaintiff", "Place", "Adjudicator"],
        },
        "Justice:Arrest-Jail": {
            "event subtype": "arrest jail",
            "event type": "Justice:Arrest-Jail",
            "keywords": ['arrest', 'jail', 'detained'],
            "event description": "The event is related to a person getting arrested or a person being sent to jail.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was sent to jailed or arrested by {ROLE_Agent} in {ROLE_Place}.",
            "valid roles": ["Person", "Agent", "Place"],
        },
        "Justice:Charge-Indict": {
            "event subtype": "charge indict",
            "event type": "Justice:Charge-Indict",
            "keywords": ['indict', 'charged', 'accused'],
            "event description": "The event is related to someone or some organization being accused of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was charged by {ROLE_Prosecutor} in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Prosecutor", "Place", "Adjudicator"],
        }, 
        "Justice:Convict": {
            "event subtype": "convict",
            "event type": "Justice:Convict",
            "keywords": ['convicted', 'guilty', 'verdict'],
            "event description": "The event is related to someone being found guilty of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was convicted of a crime in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Place", "Adjudicator"],
        }, 
        "Justice:Execute": {
            "event subtype": "execute",
            "event type": "Justice:Execute",
            "keywords": ['execution', 'executed', 'execute'],
            "event description": "The event is related to someone being executed to death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was executed by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": ["Person", "Agent", "Place"],
        },
        "Justice:Extradite": {
            "event subtype": "extradite",
            "event type": "Justice:Extradite",
            "keywords": ['extradition', 'extradited', 'extraditing'],
            "event description": "The event is related to justice. The event occurs when a person was extradited from one place to another place.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was extradicted to {ROLE_Destination} from {ROLE_Origin}, and {ROLE_Agent} was responsible for the extradition.",
            "valid roles": ["Person", "Destination", "Origin", "Agent"],
        },
        "Justice:Fine": {
            "event subtype": "fine",
            "event type": "Justice:Fine",
            "keywords": ['fine', 'fined', 'payouts'],
            "event description": "The event is related to someone being issued a financial punishment.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} in {ROLE_Place} was ordered by {ROLE_Adjudicator} to pay a fine.",
            "valid roles": ["Entity", "Place", "Adjudicator"], 
        },
        "Justice:Pardon": {
            "event subtype": "pardon",
            "event type": "Justice:Pardon",
            "keywords": ['pardon', 'pardoned', 'remission'],
            "event description": "The event is related to someone being pardoned.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} received a pardon from {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Adjudicator"],
        }, 
        "Justice:Release-Parole": {
            "event subtype": "release parole",
            "event type": "Justice:Release-Parole",
            "keywords": ['parole', 'release', 'free'],
            "event description": "The event is related to an end to someone's custody in prison.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was released by {ROLE_Entity} from {ROLE_Place}.",
            "valid roles": ["Person", "Entity", "Place"],
        },
        "Justice:Sentence": {
            "event subtype": "sentence",
            "event type": "Justice:Sentence",
            "keywords": ['sentenced', 'sentencing', 'sentence'],
            "event description": "The event is related to someone being sentenced to punishment because of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was sentenced to punishment in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Place", "Adjudicator"],
        }, 
        "Justice:Sue": {
            "event subtype": "sue",
            "event type": "Justice:Sue",
            "keywords": ['sue', 'lawsuit', 'suit'],
            "event description": "The event is related to a court proceeding that has been initiated and someone sue the other.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was sued by {ROLE_Plaintiff} in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Plaintiff", "Place", "Adjudicator"], 
        }, 
        "Justice:Trial-Hearing": {
            "event subtype": "trial hearing",
            "event type": "Justice:Trial-Hearing",
            "keywords": ['trial', 'hearing', 'proceeding'],
            "event description": "The event is related to a trial or hearing for someone.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant}, prosecuted by {ROLE_Prosecutor}, faced a trial in {ROLE_Place}, and the hearing was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Prosecutor", "Place", "Adjudicator"], 
        }, 
        "Life:Be-Born": {
            "event subtype": "born",
            "event type": "Life:Be-Born",
            "keywords": ['born', 'birth', 'bore'],
            "event description": "The event is related to life and someone is given birth to.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was born in {ROLE_Place}.",
            "valid roles": ["Person", "Place"], 
        }, 
        "Life:Die": {
            "event subtype": "die",
            "event type": "Life:Die",
            "keywords": ['kill', 'death', 'assassination'],
            "event description": "The event is related to life and someone died.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} died by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ["Agent", "Victim", "Instrument", "Place"],
        },
        "Life:Divorce": {
            "event subtype": "divorce",
            "event type": "Life:Divorce",
            "keywords": ['divorce', 'divorced', 'Divorce'],
            "event description": "The event is related to life and someone was divorced.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} divorced in {ROLE_Place}.",
            "valid roles": ["Person", "Place"], 
        }, 
        "Life:Injure": {
            "event subtype": "injure",
            "event type": "Life:Injure",
            "keywords": ['injure', 'wounded', 'hurt'],
            "event description": "The event is related to life and someone is injured.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} injured by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ["Agent", "Victim", "Instrument", "Place"],
        },
        "Life:Marry": {
            "event subtype": "marry",
            "event type": "Life:Marry",
            "keywords": ['marry', 'marriage', 'married'],
            "event description": "The event is related to life and someone is married.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} got married in {ROLE_Place}.",
            "valid roles": ["Person", "Place"], 
        },
        "Movement:Transport": {
            "event subtype": "transport",
            "event type": "Movement:Transport",
            "keywords": ['travel', 'go', 'move'],
            "event description": "The event is related to movement. The event occurs when a weapon or vehicle is moved from one place to another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Artifact} was sent to {ROLE_Destination} from {ROLE_Origin} by {ROLE_Vehicle}, and {ROLE_Agent} was responsible for the transport.",
            "valid roles": ["Artifact", "Destination", "Origin", "Vehicle", "Agent", "Place"], 
        },
        "Personnel:Elect": {
            "event subtype": "elect",
            "event type": "Personnel:Elect",
            "keywords": ['election', 'elect', 'elected'],
            "event description": "The event is related to a candidate wins an election.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was elected a position, and the election was voted by {ROLE_Entity} in {ROLE_Place}.",
            "valid roles": ["Person", "Entity", "Place"], 
        },
        "Personnel:End-Position": {
            "event subtype": "end position",
            "event type": "Personnel:End-Position",
            "keywords": ['former', 'laid off', 'fired'],
            "event description": "The event is related to a person stops working for an organization or a hiring manager.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} stopped working for {ROLE_Entity} at {ROLE_Place}.",
            "valid roles": ["Person", "Entity", "Place"],
        }, 
        "Personnel:Nominate": {
            "event subtype": "nominate",
            "event type": "Personnel:Nominate",
            "keywords": ['named', 'nomination', 'nominate'],
            "event description": "The event is related to a person being nominated for a position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was nominated by {ROLE_Agent} to do a job.",
            "valid roles": ["Person", "Agent"], 
        },  
        "Personnel:Start-Position": {
            "event subtype": "start position",
            "event type": "Personnel:Start-Position",
            "keywords": ['hire', 'appoint', 'join'],
            "event description": "The event is related to a person begins working for an organization or a hiring manager.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} got new job and was hired by {ROLE_Entity} in {ROLE_Place}.",
            "valid roles": ["Person", "Entity", "Place"], 
        },  
        "Transaction:Transfer-Money": {
            "event subtype": "transfer money",
            "event type": "Transaction:Transfer-Money",
            "keywords": ['pay', 'donation', 'loan'],
            "event description": "The event is related to transaction. The event occurs when someone is giving, receiving, borrowing, or lending money.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} paid {ROLE_Recipient} in {ROLE_Place}.",
            "valid roles": ["Giver", "Recipient", "Place", "Beneficiary"], 
        },  
        "Transaction:Transfer-Ownership": {
            "event subtype": "transfer ownership",
            "event type": "Transaction:Transfer-Ownership",
            "keywords": ['sell', 'buy', 'acquire'],
            "event description": "The event is related to transaction. The event occurs when an item or an organization is sold or gave to some other.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Buyer} got {ROLE_Artifact} from {ROLE_Place} in {ROLE_Place}.",
            "valid roles": ["Buyer", "Artifact", "Seller", "Place", "Beneficiary"], 
        }, 
    }, 
    "richere-en": {
        "Business:Declare-Bankruptcy": {
            "event subtype": "declare bankruptcy",
            "event type": "Business:Declare-Bankruptcy",
            "keywords": ['bankruptcy', 'bankrupt', 'Bankruptcy'],
            "event description": "The event is related to some organization declaring bankruptcy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} declared bankruptcy.",
            "valid roles": ["Org"],
        },
        "Business:End-Org": {
            "event subtype": "end organization",
            "event type": "Business:End-Org",
            "keywords": ['dissolve', 'disbanded', 'close'],
            "event description": "The event is related to some organization ceasing to exist.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} dissolved in {ROLE_Place}.",
            "valid roles": ["Org", "Place"],
        },
        "Business:Merge-Org": {
            "event subtype": "merge organization",
            "event type": "Business:Merge-Org",
            "keywords": ['merge', 'merging', 'merger'],
            "event description": "The event is related to two or more organization coming together to form a new organization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Org} was merged.",
            "valid roles": ["Org"],
        },
        "Business:Start-Org": {
            "event subtype": "start organization",
            "event type": "Business:Start-Org",
            "keywords": ['founded', 'create', 'launch'],
            "event description": "The event is related to a new organization being created.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} launched {ROLE_Org} at {ROLE_Place}.",
            "valid roles": ["Agent", "Org", "Place"],
        },
        "Conflict:Attack": {
            "event subtype": "attack",
            "event type": "Conflict:Attack",
            "keywords": ['war', 'attack', 'terrorism'],
            "event description": "The event is related to conflict and some violent physical act.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} attacked {ROLE_Target} by {ROLE_Instrument} at {ROLE_Place}.",
            "valid roles": ["Attacker", "Target", "Instrument", "Place", "Agent"],
        },
        "Conflict:Demonstrate": {
            "event subtype": "demonstrate",
            "event type": "Conflict:Demonstrate",
            "keywords": ['rally', 'protest', 'demonstrate'],
            "event description": "The event is related to a large number of people coming together to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} protested at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Contact:Meet": {
            "event subtype": "meet",
            "event type": "Contact:Meet",
            "keywords": ['meeting', 'met', 'summit'],
            "event description": "The event is related to a group of people meeting and interacting with one another face-to-face.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} met at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Contact:Correspondence": {
            "event subtype": "contact correspondence",
            "event type": "Contact:Correspondence",
            "keywords": ['call', 'teleconference', 'e-mail'],
            "event description": "The event happens when a face‐to‐face meeting between sender and receiver is not explicitly stated. This includes written, phone, or electronic communication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} contacted each other at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Contact:Broadcast": {
            "event subtype": "broadcast",
            "event type": "Contact:Broadcast",
            "keywords": ['statement', 'announce', 'say'],
            "event description": "The event happens when a person or an organization contact with the media and other publicity or announcement conference.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} made announcement to {ROLE_Audience} at {ROLE_Place}.",
            "valid roles": ["Entity", "Audience", "Place"],
        },
        "Contact:Contact": {
            "event subtype": "contact",
            "event type": "Contact:Contact",
            "keywords": ['said', 'talk', 'tell'],
            "event description": "The event happens when there is no explicit mention of contact ways of communication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} talked to each other at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Justice:Acquit": {
            "event subtype": "acquit",
            "event type": "Justice:Acquit",
            "keywords": ['acquitted', 'acquittal', 'acquit'],
            "event description": "The event is related to someone being acquitted.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was acquitted of the charges by {ROLE_Adjudicator} at {ROLE_Place}.",
            "valid roles": ["Defendant", "Adjudicator", "Place"],
        },
        "Justice:Appeal": {
            "event subtype": "appeal",
            "event type": "Justice:Appeal",
            "keywords": ['appeal', 'appealing', 'appeals'],
            "event description": "The event is related to someone appealing the decision of a court.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} in {ROLE_Place} appealed the adjudication by {ROLE_Prosecutor} from {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Place", "Adjudicator", "Prosecutor"],
        },
        "Justice:Arrest-Jail": {
            "event subtype": "arrest jail",
            "event type": "Justice:Arrest-Jail",
            "keywords": ['arrest', 'jail', 'detained'],
            "event description": "The event is related to a person getting arrested or a person being sent to jail.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was sent to jailed or arrested by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": ["Person", "Agent", "Place"],
        },
        "Justice:Charge-Indict": {
            "event subtype": "charge indict",
            "event type": "Justice:Charge-Indict",
            "keywords": ['indict', 'charged', 'accused'],
            "event description": "The event is related to someone or some organization being accused of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was charged by {ROLE_Prosecutor} at {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Prosecutor", "Place", "Adjudicator"],
        }, 
        "Justice:Convict": {
            "event subtype": "convict",
            "event type": "Justice:Convict",
            "keywords": ['convicted', 'guilty', 'verdict'],
            "event description": "The event is related to someone being found guilty of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was convicted of a crime in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Place", "Adjudicator"],
        }, 
        "Justice:Execute": {
            "event subtype": "execute",
            "event type": "Justice:Execute",
            "keywords": ['execution', 'executed', 'execute'],
            "event description": "The event is related to someone being executed to death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was executed by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": ["Person", "Agent", "Place"],
        },
        "Justice:Extradite": {
            "event subtype": "extradite",
            "event type": "Justice:Extradite",
            "keywords": ['extradition', 'extradited', 'extraditing'],
            "event description": "The event is related to justice. The event occurs when a person was extradited from one place to another place.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was extradicted to {ROLE_Destination} from {ROLE_Origin}, and {ROLE_Agent} was responsible for the extradition.",
            "valid roles": ["Person", "Destination", "Origin", "Agent"],
        },
        "Justice:Fine": {
            "event subtype": "fine",
            "event type": "Justice:Fine",
            "keywords": ['fine', 'fined', 'payouts'],
            "event description": "The event is related to someone being issued a financial punishment.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} in {ROLE_Place} was ordered by {ROLE_Adjudicator} to pay a fine.",
            "valid roles": ["Entity", "Place", "Adjudicator"], 
        },
        "Justice:Pardon": {
            "event subtype": "pardon",
            "event type": "Justice:Pardon",
            "keywords": ['pardon', 'pardoned', 'remission'],
            "event description": "The event is related to someone being pardoned.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} received a pardon from {ROLE_Adjudicator} at {ROLE_Place}.",
            "valid roles": ["Defendant", "Adjudicator", "Place"],
        }, 
        "Justice:Release-Parole": {
            "event subtype": "release parole",
            "event type": "Justice:Release-Parole",
            "keywords": ['parole', 'release', 'free'],
            "event description": "The event is related to an end to someone's custody in prison.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was released by {ROLE_Agent} from {ROLE_Place}.",
            "valid roles": ["Person", "Agent", "Place"],
        },
        "Justice:Sentence": {
            "event subtype": "sentence",
            "event type": "Justice:Sentence",
            "keywords": ['sentenced', 'sentencing', 'sentence'],
            "event description": "The event is related to someone being sentenced to punishment because of a crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was sentenced to punishment in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Place", "Adjudicator"],
        }, 
        "Justice:Sue": {
            "event subtype": "sue",
            "event type": "Justice:Sue",
            "keywords": ['sue', 'lawsuit', 'suit'],
            "event description": "The event is related to a court proceeding that has been initiated and someone sue the other.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant} was sued by {ROLE_Plaintiff} in {ROLE_Place}, and the adjudication was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Plaintiff", "Place", "Adjudicator"], 
        }, 
        "Justice:Trial-Hearing": {
            "event subtype": "trial hearing",
            "event type": "Justice:Trial-Hearing",
            "keywords": ['trial', 'hearing', 'proceeding'],
            "event description": "The event is related to a trial or hearing for someone.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Defendant}, prosecuted by {ROLE_Prosecutor}, faced a trial in {ROLE_Place}. The hearing was judged by {ROLE_Adjudicator}.",
            "valid roles": ["Defendant", "Prosecutor", "Place", "Adjudicator"], 
        }, 
        "Life:Be-Born": {
            "event subtype": "born",
            "event type": "Life:Be-Born",
            "keywords": ['born', 'birth', 'bore'],
            "event description": "The event is related to life and someone is given birth to.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was born at {ROLE_Place}.",
            "valid roles": ["Person", "Place"], 
        }, 
        "Life:Die": {
            "event subtype": "die",
            "event type": "Life:Die",
            "keywords": ['kill', 'death', 'assassination'],
            "event description": "The event is related to life and someone died.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} died by {ROLE_Instrument} at {ROLE_Place}.",
            "valid roles": ["Agent", "Victim", "Instrument", "Place"],
        },
        "Life:Divorce": {
            "event subtype": "divorce",
            "event type": "Life:Divorce",
            "keywords": ['divorce', 'divorced', 'Divorce'],
            "event description": "The event is related to life and someone was divorced.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} divorced at {ROLE_Place}.",
            "valid roles": ["Person", "Place"], 
        }, 
        "Life:Injure": {
            "event subtype": "injure",
            "event type": "Life:Injure",
            "keywords": ['injure', 'wounded', 'hurt'],
            "event description": "The event is related to life and someone is injured.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} injured by {ROLE_Instrument} at {ROLE_Place}.",
            "valid roles": ["Agent", "Victim", "Instrument", "Place"],
        },
        "Life:Marry": {
            "event subtype": "marry",
            "event type": "Life:Marry",
            "keywords": ['marry', 'marriage', 'married'],
            "event description": "The event is related to life and someone is married.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} got married at {ROLE_Place}.",
            "valid roles": ["Person", "Place"], 
        },
        "Movement:Transport-Person": {
            "event subtype": "transport person",
            "event type": "Movement:Transport-Person",
            "keywords": ['travel', 'go', 'move'],
            "event description": "The event is related to movement. The event occurs when a person moves or is moved from one place to another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was moved to {ROLE_Destination} from {ROLE_Origin} by {ROLE_Instrument}, and {ROLE_Agent} was responsible for the movement.",
            "valid roles": ["Person", "Destination", "Origin", "Instrument", "Agent"], 
        },
        "Movement:Transport-Artifact": {
            "event subtype": "transport artifact",
            "event type": "Movement:Transport-Artifact",
            "keywords": ['export', 'deliver', 'send'],
            "event description": "The event is related to movement. The event occurs when an artifact, like items or weapon, is moved from one place to another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Artifact} was sent to {ROLE_Destination} from {ROLE_Origin}, and {ROLE_Agent} was responsible for the transport.",
            "valid roles": ["Artifact", "Destination", "Origin", "Agent"], 
        },
        "Personnel:Elect": {
            "event subtype": "elect",
            "event type": "Personnel:Elect",
            "keywords": ['election', 'elect', 'elected'],
            "event description": "The event is related to a candidate wins an election.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was elected a position, and the election was voted by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": ["Person", "Agent", "Place"], 
        },
        "Personnel:End-Position": {
            "event subtype": "end position",
            "event type": "Personnel:End-Position",
            "keywords": ['former', 'laid off', 'fired'],
            "event description": "The event is related to a person stops working for an organization or a hiring manager.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} stopped working for {ROLE_Entity} at {ROLE_Place}.",
            "valid roles": ["Person", "Entity", "Place"],
        }, 
        "Personnel:Nominate": {
            "event subtype": "nominate",
            "event type": "Personnel:Nominate",
            "keywords": ['named', 'nomination', 'nominate'],
            "event description": "The event is related to a person being nominated for a position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was nominated by {ROLE_Entity} to do a job at {ROLE_Place}.",
            "valid roles": ["Person", "Agent", "Place"], 
        },  
        "Personnel:Start-Position": {
            "event subtype": "start position",
            "event type": "Personnel:Start-Position",
            "keywords": ['hire', 'appoint', 'join'],
            "event description": "The event is related to a person begins working for an organization or a hiring manager.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} got new job and was hired by {ROLE_Entity} at {ROLE_Place}.",
            "valid roles": ["Person", "Entity", "Place"], 
        },  
        "Transaction:Transfer-Money": {
            "event subtype": "transfer money",
            "event type": "Transaction:Transfer-Money",
            "keywords": ['pay', 'donation', 'loan'],
            "event description": "The event is related to transaction. The event occurs when someone is giving, receiving, borrowing, or lending money.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} paid {ROLE_Recipient} at {ROLE_Place}.",
            "valid roles": ["Giver", "Recipient", "Place", "Beneficiary"], 
        },  
        "Transaction:Transfer-Ownership": {
            "event subtype": "transfer ownership",
            "event type": "Transaction:Transfer-Ownership",
            "keywords": ['sell', 'buy', 'acquire'],
            "event description": "The event is events refer to the buying, selling, loaning, borrowing, giving, receiving, bartering, stealing, or renting of physical items, assets,or organizations.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "The ownership of {ROLE_Thing} from {ROLE_Giver} was transferred to {ROLE_Recipient} at {ROLE_Place}.",
            "valid roles": ["Thing", "Giver", "Recipient", "Place", "Beneficiary"], 
        }, 
        "Transaction:Transaction": {
            "event subtype": "transaction",
            "event type": "Transaction:Transaction",
            "keywords": ['receive', 'give', 'get'],
            "event description": "The event is related to transaction. The event occurs when someone is giving, receiving, borrowing, or lending something when you cannot tell whether it is money or an asset in the context.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} give some things to {ROLE_Recipient} at {ROLE_Place}.",
            "valid roles": ["Giver", "Recipient", "Place", "Beneficiary"], 
        },
        "Manufacture:Artifact": {
            "event subtype": "artifact",
            "event type": "Manufacture:Artifact",
            "keywords": ['develop', 'produce', 'construct'],
            "event description": "The event occurs whenever a person or an organization builds or manufactures a facility or a weapon, etc",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Artifact} was built by {ROLE_Agent} at {ROLE_Place}.",
            "valid roles": ["Artifact", "Agent", "Place"], 
        }, 
    },
    "m2e2": {
        "Conflict:Attack": {
            "event subtype": "attack",
            "event type": "Conflict:Attack",
            "keywords": ['war', 'attack', 'terrorism'],
            "event description": "The event is related to conflict and some violent physical act.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} attacked {ROLE_Target} by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ["Attacker", "Target", "Instrument", "Place"],
        },
        "Conflict:Demonstrate": {
            "event subtype": "demonstrate",
            "event type": "Conflict:Demonstrate",
            "keywords": ['rally', 'protest', 'demonstrate'],
            "event description": "The event is related to a large number of people coming together to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} protested at {ROLE_Place} with {ROLE_Police}.",
            "valid roles": ["Entity", "Place", "Police"],
        },
        "Contact:Meet": {
            "event subtype": "meet",
            "event type": "Contact:Meet",
            "keywords": ['meeting', 'met', 'summit'],
            "event description": "The event is related to a group of people meeting and interacting with one another face-to-face.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} met at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Contact:Phone-Write": {
            "event subtype": "phone write",
            "event type": "Contact:Phone-Write",
            "keywords": ['call', 'communicate', 'e-mail'],
            "event description": "The event is related to people phone calling or messaging one another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Entity} called or texted messages at {ROLE_Place}.",
            "valid roles": ["Entity", "Place"],
        },
        "Justice:Arrest-Jail": {
            "event subtype": "arrest jail",
            "event type": "Justice:Arrest-Jail",
            "keywords": ['arrest', 'jail', 'detained'],
            "event description": "The event is related to a person getting arrested or a person being sent to jail.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Person} was sent to jailed or arrested by {ROLE_Agent} in {ROLE_Place}.",
            "valid roles": ["Person", "Agent", "Place"],
        },
        "Life:Die": {
            "event subtype": "die",
            "event type": "Life:Die",
            "keywords": ['kill', 'death', 'assassination'],
            "event description": "The event is related to life and someone died.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Agent} led to {ROLE_Victim} died by {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ["Agent", "Victim", "Instrument", "Place"],
        },
        "Movement:Transport": {
            "event subtype": "transport",
            "event type": "Movement:Transport",
            "keywords": ['travel', 'go', 'move'],
            "event description": "The event is related to movement. The event occurs when a weapon or vehicle is moved from one place to another.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Artifact} was sent to {ROLE_Destination} from {ROLE_Origin} by {ROLE_Vehicle}, and {ROLE_Agent} was responsible for the transport.",
            "valid roles": ["Artifact", "Destination", "Origin", "Vehicle", "Agent"], 
        },
        "Transaction:Transfer-Money": {
            "event subtype": "transfer money",
            "event type": "Transaction:Transfer-Money",
            "keywords": ['pay', 'donation', 'loan'],
            "event description": "The event is related to transaction. The event occurs when someone is giving, receiving, borrowing, or lending money.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} paid {ROLE_Recipient}.",
            "valid roles": ["Giver", "Recipient"], 
        },  
    }, 
    "maven": {
        "Achieve": {
            "event description": "The event is related to achieve.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Action": {
            "event description": "The event is related to action.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Adducing": {
            "event description": "The event is related to adducing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Agree_or_refuse_to_act": {
            "event description": "The event is related to agree or refuse to act.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Aiming": {
            "event description": "The event is related to aiming.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Arranging": {
            "event description": "The event is related to arranging.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Arrest": {
            "event description": "The event is related to arrest.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Arriving": {
            "event description": "The event is related to arriving.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Assistance": {
            "event description": "The event is related to assistance.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Attack": {
            "event description": "The event is related to attack.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Award": {
            "event description": "The event is related to award.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Bearing_arms": {
            "event description": "The event is related to bearing arms.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Becoming": {
            "event description": "The event is related to becoming.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Becoming_a_member": {
            "event description": "The event is related to becoming a member.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Being_in_operation": {
            "event description": "The event is related to being in operation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Besieging": {
            "event description": "The event is related to besieging.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Bodily_harm": {
            "event description": "The event is related to bodily harm.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Body_movement": {
            "event description": "The event is related to body movement.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Breathing": {
            "event description": "The event is related to breathing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Bringing": {
            "event description": "The event is related to bringing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Building": {
            "event description": "The event is related to building.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Carry_goods": {
            "event description": "The event is related to carry goods.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Catastrophe": {
            "event description": "The event is related to catastrophe.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Causation": {
            "event description": "The event is related to causation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Cause_change_of_position_on_a_scale": {
            "event description": "The event is related to cause change of position on a scale.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Cause_change_of_strength": {
            "event description": "The event is related to cause change of strength.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Cause_to_amalgamate": {
            "event description": "The event is related to cause to amalgamate.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Cause_to_be_included": {
            "event description": "The event is related to cause to be included.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Cause_to_make_progress": {
            "event description": "The event is related to cause to make progress.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Change": {
            "event description": "The event is related to change.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Change_event_time": {
            "event description": "The event is related to change event time.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Change_of_leadership": {
            "event description": "The event is related to change of leadership.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Change_sentiment": {
            "event description": "The event is related to change sentiment.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Change_tool": {
            "event description": "The event is related to change tool.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Check": {
            "event description": "The event is related to check.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Choosing": {
            "event description": "The event is related to choosing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Collaboration": {
            "event description": "The event is related to collaboration.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Come_together": {
            "event description": "The event is related to come together.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Coming_to_be": {
            "event description": "The event is related to coming to be.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Coming_to_believe": {
            "event description": "The event is related to coming to believe.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Commerce_buy": {
            "event description": "The event is related to commerce buy.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Commerce_pay": {
            "event description": "The event is related to commerce pay.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Commerce_sell": {
            "event description": "The event is related to commerce sell.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Commitment": {
            "event description": "The event is related to commitment.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Committing_crime": {
            "event description": "The event is related to committing crime.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Communication": {
            "event description": "The event is related to communication.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Competition": {
            "event description": "The event is related to competition.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Confronting_problem": {
            "event description": "The event is related to confronting problem.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Connect": {
            "event description": "The event is related to connect.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Conquering": {
            "event description": "The event is related to conquering.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Containing": {
            "event description": "The event is related to containing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Control": {
            "event description": "The event is related to control.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Convincing": {
            "event description": "The event is related to convincing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Cost": {
            "event description": "The event is related to cost.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Create_artwork": {
            "event description": "The event is related to create artwork.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Creating": {
            "event description": "The event is related to creating.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Criminal_investigation": {
            "event description": "The event is related to criminal investigation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Cure": {
            "event description": "The event is related to cure.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Damaging": {
            "event description": "The event is related to damaging.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Death": {
            "event description": "The event is related to death.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Deciding": {
            "event description": "The event is related to deciding.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Defending": {
            "event description": "The event is related to defending.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Departing": {
            "event description": "The event is related to departing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Destroying": {
            "event description": "The event is related to destroying.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Dispersal": {
            "event description": "The event is related to dispersal.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Earnings_and_losses": {
            "event description": "The event is related to earnings and losses.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Education_teaching": {
            "event description": "The event is related to education teaching.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Emergency": {
            "event description": "The event is related to emergency.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Employment": {
            "event description": "The event is related to employment.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Emptying": {
            "event description": "The event is related to emptying.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Escaping": {
            "event description": "The event is related to escaping.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Exchange": {
            "event description": "The event is related to exchange.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Expansion": {
            "event description": "The event is related to expansion.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Expend_resource": {
            "event description": "The event is related to expend resource.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Expressing_publicly": {
            "event description": "The event is related to expressing publicly.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Extradition": {
            "event description": "The event is related to extradition.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Filling": {
            "event description": "The event is related to filling.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Forming_relationships": {
            "event description": "The event is related to forming relationships.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "GetReady": {
            "event description": "The event is related to getready.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Getting": {
            "event description": "The event is related to getting.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "GiveUp": {
            "event description": "The event is related to giveup.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Giving": {
            "event description": "The event is related to giving.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Having_or_lacking_access": {
            "event description": "The event is related to having or lacking access.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Hiding_objects": {
            "event description": "The event is related to hiding objects.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Hindering": {
            "event description": "The event is related to hindering.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Hold": {
            "event description": "The event is related to hold.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Hostile_encounter": {
            "event description": "The event is related to hostile encounter.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Imposing_obligation": {
            "event description": "The event is related to imposing obligation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Incident": {
            "event description": "The event is related to incident.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Influence": {
            "event description": "The event is related to influence.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Ingestion": {
            "event description": "The event is related to ingestion.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Institutionalization": {
            "event description": "The event is related to institutionalization.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Judgment_communication": {
            "event description": "The event is related to judgment communication.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justifying": {
            "event description": "The event is related to justifying.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Kidnapping": {
            "event description": "The event is related to kidnapping.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Killing": {
            "event description": "The event is related to killing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Know": {
            "event description": "The event is related to know.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Labeling": {
            "event description": "The event is related to labeling.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Legal_rulings": {
            "event description": "The event is related to legal rulings.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Legality": {
            "event description": "The event is related to legality.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Lighting": {
            "event description": "The event is related to lighting.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Limiting": {
            "event description": "The event is related to limiting.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Manufacturing": {
            "event description": "The event is related to manufacturing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Military_operation": {
            "event description": "The event is related to military operation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Motion": {
            "event description": "The event is related to motion.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Motion_directional": {
            "event description": "The event is related to motion directional.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Name_conferral": {
            "event description": "The event is related to name conferral.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Openness": {
            "event description": "The event is related to openness.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Participation": {
            "event description": "The event is related to participation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Patrolling": {
            "event description": "The event is related to patrolling.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Perception_active": {
            "event description": "The event is related to perception active.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Placing": {
            "event description": "The event is related to placing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Practice": {
            "event description": "The event is related to practice.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Presence": {
            "event description": "The event is related to presence.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Preserving": {
            "event description": "The event is related to preserving.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Preventing_or_letting": {
            "event description": "The event is related to preventing or letting.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Prison": {
            "event description": "The event is related to prison.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Process_end": {
            "event description": "The event is related to process end.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Process_start": {
            "event description": "The event is related to process start.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Protest": {
            "event description": "The event is related to protest.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Publishing": {
            "event description": "The event is related to publishing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Quarreling": {
            "event description": "The event is related to quarreling.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Ratification": {
            "event description": "The event is related to ratification.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Receiving": {
            "event description": "The event is related to receiving.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Recording": {
            "event description": "The event is related to recording.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Recovering": {
            "event description": "The event is related to recovering.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Reforming_a_system": {
            "event description": "The event is related to reforming a system.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Releasing": {
            "event description": "The event is related to releasing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Removing": {
            "event description": "The event is related to removing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Renting": {
            "event description": "The event is related to renting.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Reporting": {
            "event description": "The event is related to reporting.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Request": {
            "event description": "The event is related to request.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Rescuing": {
            "event description": "The event is related to rescuing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Research": {
            "event description": "The event is related to research.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Resolve_problem": {
            "event description": "The event is related to resolve problem.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Response": {
            "event description": "The event is related to response.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Reveal_secret": {
            "event description": "The event is related to reveal secret.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Revenge": {
            "event description": "The event is related to revenge.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Rewards_and_punishments": {
            "event description": "The event is related to rewards and punishments.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Risk": {
            "event description": "The event is related to risk.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Rite": {
            "event description": "The event is related to rite.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Robbery": {
            "event description": "The event is related to robbery.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Scouring": {
            "event description": "The event is related to scouring.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Scrutiny": {
            "event description": "The event is related to scrutiny.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Self_motion": {
            "event description": "The event is related to self motion.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Sending": {
            "event description": "The event is related to sending.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Sign_agreement": {
            "event description": "The event is related to sign agreement.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Social_event": {
            "event description": "The event is related to social event.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Statement": {
            "event description": "The event is related to statement.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Submitting_documents": {
            "event description": "The event is related to submitting documents.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Supply": {
            "event description": "The event is related to supply.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Supporting": {
            "event description": "The event is related to supporting.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Surrendering": {
            "event description": "The event is related to surrendering.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Surrounding": {
            "event description": "The event is related to surrounding.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Suspicion": {
            "event description": "The event is related to suspicion.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Telling": {
            "event description": "The event is related to telling.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Temporary_stay": {
            "event description": "The event is related to temporary stay.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Terrorism": {
            "event description": "The event is related to terrorism.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Testing": {
            "event description": "The event is related to testing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Theft": {
            "event description": "The event is related to theft.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Traveling": {
            "event description": "The event is related to traveling.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Use_firearm": {
            "event description": "The event is related to use firearm.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Using": {
            "event description": "The event is related to using.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Violence": {
            "event description": "The event is related to violence.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Vocalizations": {
            "event description": "The event is related to vocalizations.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Warning": {
            "event description": "The event is related to warning.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Wearing": {
            "event description": "The event is related to wearing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Writing": {
            "event description": "The event is related to writing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },  
    },
    "geneva": {
        "Achieve": {
            "event type": "Achieve",
            "keywords": [],
            "event description": "The event is related to achieve.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Goal {ROLE_Goal} Means {ROLE_Means}.",
            "valid roles": ["Agent", "Goal", "Means"],
        },
        "Action": {
            "event type": "Action",
            "keywords": [],
            "event description": "The event is related to action.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Act {ROLE_Act} Agent {ROLE_Agent} Domain {ROLE_Domain} Manner {ROLE_Manner}.",
            "valid roles": ["Act", "Agent", "Domain", "Manner"],
        },
        "Adducing": {
            "event type": "Adducing",
            "keywords": [],
            "event description": "The event is related to adducing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Medium {ROLE_Medium} Role {ROLE_Role} Speaker {ROLE_Speaker} Specified Entity {ROLE_Specified_entity}.",
            "valid roles": ["Medium", "Role", "Speaker", "Specified_entity"],
        },
        "Agree_or_refuse_to_act": {
            "event type": "Agree_or_refuse_to_act",
            "keywords": [],
            "event description": "The event is related to agree refuse act.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Proposed Action {ROLE_Proposed_action} Speaker {ROLE_Speaker}.",
            "valid roles": ["Proposed_action", "Speaker"],
        },
        "Arranging": {
            "event type": "Arranging",
            "keywords": [],
            "event description": "The event is related to arranging.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Configuration {ROLE_Configuration} Location {ROLE_Location} Theme {ROLE_Theme}.",
            "valid roles": ["Agent", "Configuration", "Location", "Theme"],
        },
        "Arrest": {
            "event type": "Arrest",
            "keywords": [],
            "event description": "The event is related to arrest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Authorities {ROLE_Authorities} Charges {ROLE_Charges} Offense {ROLE_Offense} Suspect {ROLE_Suspect}.",
            "valid roles": ["Authorities", "Charges", "Offense", "Suspect"],
        },
        "Arriving": {
            "event type": "Arriving",
            "keywords": [],
            "event description": "The event is related to arriving.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Goal {ROLE_Goal} Means {ROLE_Means} Path {ROLE_Path} Place {ROLE_Place} Purpose {ROLE_Purpose} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": ["Goal", "Means", "Path", "Place", "Purpose", "Source", "Theme"],
        },
        "Assistance": {
            "event type": "Assistance",
            "keywords": [],
            "event description": "The event is related to assistance.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Benefited Party {ROLE_Benefited_party} Focal Entity {ROLE_Focal_entity} Goal {ROLE_Goal} Helper {ROLE_Helper} Means {ROLE_Means}.",
            "valid roles": ["Benefited_party", "Focal_entity", "Goal", "Helper", "Means"],
        },
        "Attack": {
            "event type": "Attack",
            "keywords": [],
            "event description": "The event is related to attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Assailant {ROLE_Assailant} Means {ROLE_Means} Victim {ROLE_Victim} Weapon {ROLE_Weapon}.",
            "valid roles": ["Assailant", "Means", "Victim", "Weapon"],
        },
        "Bearing_arms": {
            "event type": "Bearing_arms",
            "keywords": [],
            "event description": "The event is related to bearing arms.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Protagonist {ROLE_Protagonist} Weapon {ROLE_Weapon}.",
            "valid roles": ["Protagonist", "Weapon"],
        },
        "Becoming": {
            "event type": "Becoming",
            "keywords": [],
            "event description": "The event is related to becoming.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Entity {ROLE_Entity} Final Category {ROLE_Final_category} Final Quality {ROLE_Final_quality}.",
            "valid roles": ["Entity", "Final_category", "Final_quality"],
        },
        "Becoming_a_member": {
            "event type": "Becoming_a_member",
            "keywords": [],
            "event description": "The event is related to becoming a member.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Group {ROLE_Group} New Member {ROLE_New_member}.",
            "valid roles": ["Group", "New_member"],
        },
        "Bodily_harm": {
            "event type": "Bodily_harm",
            "keywords": [],
            "event description": "The event is related to bodily harm.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Body Part {ROLE_Body_part} Cause {ROLE_Cause} Instrument {ROLE_Instrument} Victim {ROLE_Victim}.",
            "valid roles": ["Agent", "Body_part", "Cause", "Instrument", "Victim"],
        },
        "Bringing": {
            "event type": "Bringing",
            "keywords": [],
            "event description": "The event is related to bringing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Area {ROLE_Area} Carrier {ROLE_Carrier} Goal {ROLE_Goal} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": ["Agent", "Area", "Carrier", "Goal", "Source", "Theme"],
        },
        "Building": {
            "event type": "Building",
            "keywords": [],
            "event description": "The event is related to building.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Components {ROLE_Components} Created Entity {ROLE_Created_entity} Place {ROLE_Place}.",
            "valid roles": ["Agent", "Components", "Created_entity", "Place"],
        },
        "Catastrophe": {
            "event type": "Catastrophe",
            "keywords": [],
            "event description": "The event is related to catastrophe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Patient {ROLE_Patient} Place {ROLE_Place} Undesirable Event {ROLE_Undesirable_event}.",
            "valid roles": ["Cause", "Patient", "Place", "Undesirable_event"],
        },
        "Causation": {
            "event type": "Causation",
            "keywords": [],
            "event description": "The event is related to causation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Actor {ROLE_Actor} Affected {ROLE_Affected} Cause {ROLE_Cause} Effect {ROLE_Effect} Means {ROLE_Means}.",
            "valid roles": ["Actor", "Affected", "Cause", "Effect", "Means"],
        },
        "Cause_change_of_position_on_a_scale": {
            "event type": "Cause_change_of_position_on_a_scale",
            "keywords": [],
            "event description": "The event is related to cause change position on acale.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Attribute {ROLE_Attribute} Cause {ROLE_Cause} Difference {ROLE_Difference} Item {ROLE_Item} Value 1 {ROLE_Value_1} Value 2 {ROLE_Value_2}.",
            "valid roles": ["Agent", "Attribute", "Cause", "Difference", "Item", "Value_1", "Value_2"],
        },
        "Cause_to_amalgamate": {
            "event type": "Cause_to_amalgamate",
            "keywords": [],
            "event description": "The event is related to cause amalgamate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Part 1 {ROLE_Part_1} Part 2 {ROLE_Part_2} Parts {ROLE_Parts} Whole {ROLE_Whole}.",
            "valid roles": ["Agent", "Part_1", "Part_2", "Parts", "Whole"],
        },
        "Cause_to_make_progress": {
            "event type": "Cause_to_make_progress",
            "keywords": [],
            "event description": "The event is related to cause make_ progress.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Project {ROLE_Project}.",
            "valid roles": ["Agent", "Project"],
        },
        "Change": {
            "event type": "Change",
            "keywords": [],
            "event description": "The event is related to change.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Attribute {ROLE_Attribute} Cause {ROLE_Cause} Entity {ROLE_Entity} Final Category {ROLE_Final_category} Final Value {ROLE_Final_value} Initial Category {ROLE_Initial_category}.",
            "valid roles": ["Agent", "Attribute", "Cause", "Entity", "Final_category", "Final_value", "Initial_category"],
        },
        "Change_of_leadership": {
            "event type": "Change_of_leadership",
            "keywords": [],
            "event description": "The event is related to change leadership.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Body {ROLE_Body} New Leader {ROLE_New_leader} Old Leader {ROLE_Old_leader} Old Order {ROLE_Old_order} Role {ROLE_Role} Selector {ROLE_Selector}.",
            "valid roles": ["Body", "New_leader", "Old_leader", "Old_order", "Role", "Selector"],
        },
        "Check": {
            "event type": "Check",
            "keywords": [],
            "event description": "The event is related to check.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Inspector {ROLE_Inspector} Means {ROLE_Means} Unconfirmed Content {ROLE_Unconfirmed_content}.",
            "valid roles": ["Inspector", "Means", "Unconfirmed_content"],
        },
        "Choosing": {
            "event type": "Choosing",
            "keywords": [],
            "event description": "The event is related to choosing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Chosen {ROLE_Chosen} Cognizer {ROLE_Cognizer} Possibilities {ROLE_Possibilities}.",
            "valid roles": ["Chosen", "Cognizer", "Possibilities"],
        },
        "Collaboration": {
            "event type": "Collaboration",
            "keywords": [],
            "event description": "The event is related to collaboration.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Partners {ROLE_Partners} Undertaking {ROLE_Undertaking}.",
            "valid roles": ["Partners", "Undertaking"],
        },
        "Come_together": {
            "event type": "Come_together",
            "keywords": [],
            "event description": "The event is related to come together.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Configuration {ROLE_Configuration} Individuals {ROLE_Individuals} Place {ROLE_Place}.",
            "valid roles": ["Configuration", "Individuals", "Place"],
        },
        "Coming_to_be": {
            "event type": "Coming_to_be",
            "keywords": [],
            "event description": "The event is related to coming.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Components {ROLE_Components} Entity {ROLE_Entity} Place {ROLE_Place} Time {ROLE_Time}.",
            "valid roles": ["Components", "Entity", "Place", "Time"],
        },
        "Coming_to_believe": {
            "event type": "Coming_to_believe",
            "keywords": [],
            "event description": "The event is related to coming believe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cognizer {ROLE_Cognizer} Content {ROLE_Content} Means {ROLE_Means}.",
            "valid roles": ["Cognizer", "Content", "Means"],
        },
        "Commerce_buy": {
            "event type": "Commerce_buy",
            "keywords": [],
            "event description": "The event is related to commerce buy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Buyer {ROLE_Buyer} Goods {ROLE_Goods} Seller {ROLE_Seller}.",
            "valid roles": ["Buyer", "Goods", "Seller"],
        },
        "Commerce_pay": {
            "event type": "Commerce_pay",
            "keywords": [],
            "event description": "The event is related to commerce pay.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Buyer {ROLE_Buyer} Goods {ROLE_Goods} Money {ROLE_Money} Seller {ROLE_Seller}.",
            "valid roles": ["Buyer", "Goods", "Money", "Seller"],
        },
        "Commerce_sell": {
            "event type": "Commerce_sell",
            "keywords": [],
            "event description": "The event is related to commerce sell.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Buyer {ROLE_Buyer} Goods {ROLE_Goods} Money {ROLE_Money} Seller {ROLE_Seller}.",
            "valid roles": ["Buyer", "Goods", "Money", "Seller"],
        },
        "Commitment": {
            "event type": "Commitment",
            "keywords": [],
            "event description": "The event is related to commitment.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Message {ROLE_Message} Speaker {ROLE_Speaker}.",
            "valid roles": ["Addressee", "Message", "Speaker"],
        },
        "Committing_crime": {
            "event type": "Committing_crime",
            "keywords": [],
            "event description": "The event is related to committing crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Crime {ROLE_Crime} Instrument {ROLE_Instrument} Perpetrator {ROLE_Perpetrator}.",
            "valid roles": ["Crime", "Instrument", "Perpetrator"],
        },
        "Communication": {
            "event type": "Communication",
            "keywords": [],
            "event description": "The event is related to communication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Interlocutors {ROLE_Interlocutors} Message {ROLE_Message} Speaker {ROLE_Speaker} Topic {ROLE_Topic} Trigger {ROLE_Trigger}.",
            "valid roles": ["Addressee", "Interlocutors", "Message", "Speaker", "Topic", "Trigger"],
        },
        "Competition": {
            "event type": "Competition",
            "keywords": [],
            "event description": "The event is related to competition.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Competition {ROLE_Competition} Participants {ROLE_Participants} Venue {ROLE_Venue}.",
            "valid roles": ["Competition", "Participants", "Venue"],
        },
        "Confronting_problem": {
            "event type": "Confronting_problem",
            "keywords": [],
            "event description": "The event is related to confronting problem.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Activity {ROLE_Activity} Experiencer {ROLE_Experiencer}.",
            "valid roles": ["Activity", "Experiencer"],
        },
        "Connect": {
            "event type": "Connect",
            "keywords": [],
            "event description": "The event is related to connect.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Figures {ROLE_Figures} Ground {ROLE_Ground}.",
            "valid roles": ["Figures", "Ground"],
        },
        "Conquering": {
            "event type": "Conquering",
            "keywords": [],
            "event description": "The event is related to conquering.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Conqueror {ROLE_Conqueror} Means {ROLE_Means} Theme {ROLE_Theme}.",
            "valid roles": ["Conqueror", "Means", "Theme"],
        },
        "Containing": {
            "event type": "Containing",
            "keywords": [],
            "event description": "The event is related to containing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Container {ROLE_Container} Contents {ROLE_Contents}.",
            "valid roles": ["Container", "Contents"],
        },
        "Control": {
            "event type": "Control",
            "keywords": [],
            "event description": "The event is related to control.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Controlling Variable {ROLE_Controlling_variable} Dependent Variable {ROLE_Dependent_variable}.",
            "valid roles": ["Controlling_variable", "Dependent_variable"],
        },
        "Convincing": {
            "event type": "Convincing",
            "keywords": [],
            "event description": "The event is related to convincing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Content {ROLE_Content} Speaker {ROLE_Speaker} Topic {ROLE_Topic}.",
            "valid roles": ["Addressee", "Content", "Speaker", "Topic"],
        },
        "Cost": {
            "event type": "Cost",
            "keywords": [],
            "event description": "The event is related to cost.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Asset {ROLE_Asset} Goods {ROLE_Goods} Intended Event {ROLE_Intended_event} Payer {ROLE_Payer} Rate {ROLE_Rate}.",
            "valid roles": ["Asset", "Goods", "Intended_event", "Payer", "Rate"],
        },
        "Create_artwork": {
            "event type": "Create_artwork",
            "keywords": [],
            "event description": "The event is related to create artwork.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Activity {ROLE_Activity} Culture {ROLE_Culture}.",
            "valid roles": ["Activity", "Culture"],
        },
        "Creating": {
            "event type": "Creating",
            "keywords": [],
            "event description": "The event is related to creating.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Created Entity {ROLE_Created_entity} Creator {ROLE_Creator}.",
            "valid roles": ["Cause", "Created_entity", "Creator"],
        },
        "Criminal_investigation": {
            "event type": "Criminal_investigation",
            "keywords": [],
            "event description": "The event is related to criminal investigation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Incident {ROLE_Incident} Investigator {ROLE_Investigator} Suspect {ROLE_Suspect}.",
            "valid roles": ["Incident", "Investigator", "Suspect"],
        },
        "Cure": {
            "event type": "Cure",
            "keywords": [],
            "event description": "The event is related to cure.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Affliction {ROLE_Affliction} Medication {ROLE_Medication} Patient {ROLE_Patient} Treatment {ROLE_Treatment}.",
            "valid roles": ["Affliction", "Medication", "Patient", "Treatment"],
        },
        "Damaging": {
            "event type": "Damaging",
            "keywords": [],
            "event description": "The event is related to damaging.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Patient {ROLE_Patient}.",
            "valid roles": ["Agent", "Cause", "Patient"],
        },
        "Death": {
            "event type": "Death",
            "keywords": [],
            "event description": "The event is related to death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Deceased {ROLE_Deceased}.",
            "valid roles": ["Deceased"],
        },
        "Deciding": {
            "event type": "Deciding",
            "keywords": [],
            "event description": "The event is related to deciding.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cognizer {ROLE_Cognizer} Decision {ROLE_Decision}.",
            "valid roles": ["Cognizer", "Decision"],
        },
        "Defending": {
            "event type": "Defending",
            "keywords": [],
            "event description": "The event is related to defending.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Assailant {ROLE_Assailant} Defender {ROLE_Defender} Instrument {ROLE_Instrument} Victim {ROLE_Victim}.",
            "valid roles": ["Assailant", "Defender", "Instrument", "Victim"],
        },
        "Departing": {
            "event type": "Departing",
            "keywords": [],
            "event description": "The event is related to departing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Goal {ROLE_Goal} Path {ROLE_Path} Source {ROLE_Source} Traveller {ROLE_Traveller}.",
            "valid roles": ["Goal", "Path", "Source", "Traveller"],
        },
        "Destroying": {
            "event type": "Destroying",
            "keywords": [],
            "event description": "The event is related to destroying.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Destroyer {ROLE_Destroyer} Means {ROLE_Means} Patient {ROLE_Patient}.",
            "valid roles": ["Cause", "Destroyer", "Means", "Patient"],
        },
        "Dispersal": {
            "event type": "Dispersal",
            "keywords": [],
            "event description": "The event is related to dispersal.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Goal Area {ROLE_Goal_area} Individuals {ROLE_Individuals}.",
            "valid roles": ["Agent", "Cause", "Goal_area", "Individuals"],
        },
        "Earnings_and_losses": {
            "event type": "Earnings_and_losses",
            "keywords": [],
            "event description": "The event is related to earnings losses.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Earner {ROLE_Earner} Earnings {ROLE_Earnings} Goods {ROLE_Goods}.",
            "valid roles": ["Earner", "Earnings", "Goods"],
        },
        "Education_teaching": {
            "event type": "Education_teaching",
            "keywords": [],
            "event description": "The event is related to education teaching.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Course {ROLE_Course} Fact {ROLE_Fact} Role {ROLE_Role} Skill {ROLE_Skill} Student {ROLE_Student} Subject {ROLE_Subject} Teacher {ROLE_Teacher}.",
            "valid roles": ["Course", "Fact", "Role", "Skill", "Student", "Subject", "Teacher"],
        },
        "Emergency": {
            "event type": "Emergency",
            "keywords": [],
            "event description": "The event is related to emergency.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Place {ROLE_Place} Undesirable Event {ROLE_Undesirable_event}.",
            "valid roles": ["Place", "Undesirable_event"],
        },
        "Employment": {
            "event type": "Employment",
            "keywords": [],
            "event description": "The event is related to employment.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Employee {ROLE_Employee} Employer {ROLE_Employer} Field {ROLE_Field} Place Of Employment {ROLE_Place_of_employment} Position {ROLE_Position} Task {ROLE_Task} Type {ROLE_Type}.",
            "valid roles": ["Employee", "Employer", "Field", "Place_of_employment", "Position", "Task", "Type"],
        },
        "Emptying": {
            "event type": "Emptying",
            "keywords": [],
            "event description": "The event is related to emptying.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": ["Agent", "Cause", "Source", "Theme"],
        },
        "Exchange": {
            "event type": "Exchange",
            "keywords": [],
            "event description": "The event is related to exchange.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Exchanger 1 {ROLE_Exchanger_1} Exchanger 2 {ROLE_Exchanger_2} Exchangers {ROLE_Exchangers} Theme 1 {ROLE_Theme_1} Theme 2 {ROLE_Theme_2} Themes {ROLE_Themes}.",
            "valid roles": ["Exchanger_1", "Exchanger_2", "Exchangers", "Theme_1", "Theme_2", "Themes"],
        },
        "Expansion": {
            "event type": "Expansion",
            "keywords": [],
            "event description": "The event is related to expansion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Dimension {ROLE_Dimension} Initial Size {ROLE_Initial_size} Item {ROLE_Item} Result Size {ROLE_Result_size}.",
            "valid roles": ["Agent", "Dimension", "Initial_size", "Item", "Result_size"],
        },
        "Filling": {
            "event type": "Filling",
            "keywords": [],
            "event description": "The event is related to filling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Goal {ROLE_Goal} Theme {ROLE_Theme}.",
            "valid roles": ["Agent", "Cause", "Goal", "Theme"],
        },
        "GetReady": {
            "event type": "GetReady",
            "keywords": [],
            "event description": "The event is related to getready.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Activity {ROLE_Activity} Protagonist {ROLE_Protagonist}.",
            "valid roles": ["Activity", "Protagonist"],
        },
        "Getting": {
            "event type": "Getting",
            "keywords": [],
            "event description": "The event is related to getting.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Means {ROLE_Means} Recipient {ROLE_Recipient} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": ["Means", "Recipient", "Source", "Theme"],
        },
        "Giving": {
            "event type": "Giving",
            "keywords": [],
            "event description": "The event is related to giving.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Offerer {ROLE_Offerer} Recipient {ROLE_Recipient} Theme {ROLE_Theme}.",
            "valid roles": ["Offerer", "Recipient", "Theme"],
        },
        "Hindering": {
            "event type": "Hindering",
            "keywords": [],
            "event description": "The event is related to hindering.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Action {ROLE_Action} Hindrance {ROLE_Hindrance} Protagonist {ROLE_Protagonist}.",
            "valid roles": ["Action", "Hindrance", "Protagonist"],
        },
        "Hold": {
            "event type": "Hold",
            "keywords": [],
            "event description": "The event is related to hold.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Entity {ROLE_Entity} Manipulator {ROLE_Manipulator}.",
            "valid roles": ["Entity", "Manipulator"],
        },
        "Hostile_encounter": {
            "event type": "Hostile_encounter",
            "keywords": [],
            "event description": "The event is related to hostile encounter.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Instrument {ROLE_Instrument} Issue {ROLE_Issue} Purpose {ROLE_Purpose} Side 1 {ROLE_Side_1} Side 2 {ROLE_Side_2} Sides {ROLE_Sides}.",
            "valid roles": ["Instrument", "Issue", "Purpose", "Side_1", "Side_2", "Sides"],
        },
        "Influence": {
            "event type": "Influence",
            "keywords": [],
            "event description": "The event is related to influence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Action {ROLE_Action} Agent {ROLE_Agent} Behavior {ROLE_Behavior} Cognizer {ROLE_Cognizer} Product {ROLE_Product} Situation {ROLE_Situation}.",
            "valid roles": ["Action", "Agent", "Behavior", "Cognizer", "Product", "Situation"],
        },
        "Ingestion": {
            "event type": "Ingestion",
            "keywords": [],
            "event description": "The event is related to ingestion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Ingestibles {ROLE_Ingestibles} Ingestor {ROLE_Ingestor}.",
            "valid roles": ["Ingestibles", "Ingestor"],
        },
        "Judgment_communication": {
            "event type": "Judgment_communication",
            "keywords": [],
            "event description": "The event is related to judgment communication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Communicator {ROLE_Communicator} Evaluee {ROLE_Evaluee} Medium {ROLE_Medium} Reason {ROLE_Reason} Topic {ROLE_Topic}.",
            "valid roles": ["Addressee", "Communicator", "Evaluee", "Medium", "Reason", "Topic"],
        },
        "Killing": {
            "event type": "Killing",
            "keywords": [],
            "event description": "The event is related to killing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Instrument {ROLE_Instrument} Killer {ROLE_Killer} Means {ROLE_Means} Victim {ROLE_Victim}.",
            "valid roles": ["Cause", "Instrument", "Killer", "Means", "Victim"],
        },
        "Know": {
            "event type": "Know",
            "keywords": [],
            "event description": "The event is related to know.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cognizer {ROLE_Cognizer} Evidence {ROLE_Evidence} Instrument {ROLE_Instrument} Means {ROLE_Means} Phenomenon {ROLE_Phenomenon} Topic {ROLE_Topic}.",
            "valid roles": ["Cognizer", "Evidence", "Instrument", "Means", "Phenomenon", "Topic"],
        },
        "Labeling": {
            "event type": "Labeling",
            "keywords": [],
            "event description": "The event is related to labeling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Entity {ROLE_Entity} Label {ROLE_Label} Speaker {ROLE_Speaker}.",
            "valid roles": ["Entity", "Label", "Speaker"],
        },
        "Legality": {
            "event type": "Legality",
            "keywords": [],
            "event description": "The event is related to legality.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Action {ROLE_Action} Object {ROLE_Object}.",
            "valid roles": ["Action", "Object"],
        },
        "Manufacturing": {
            "event type": "Manufacturing",
            "keywords": [],
            "event description": "The event is related to manufacturing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Factory {ROLE_Factory} Instrument {ROLE_Instrument} Producer {ROLE_Producer} Product {ROLE_Product} Resource {ROLE_Resource}.",
            "valid roles": ["Factory", "Instrument", "Producer", "Product", "Resource"],
        },
        "Motion": {
            "event type": "Motion",
            "keywords": [],
            "event description": "The event is related to motion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Area {ROLE_Area} Cause {ROLE_Cause} Distance {ROLE_Distance} Goal {ROLE_Goal} Means {ROLE_Means} Path {ROLE_Path} Source {ROLE_Source} Speed {ROLE_Speed} Theme {ROLE_Theme}.",
            "valid roles": ["Agent", "Area", "Cause", "Distance", "Goal", "Means", "Path", "Source", "Speed", "Theme"],
        },
        "Motion_directional": {
            "event type": "Motion_directional",
            "keywords": [],
            "event description": "The event is related to motion directional.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Area {ROLE_Area} Direction {ROLE_Direction} Goal {ROLE_Goal} Path {ROLE_Path} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": ["Area", "Direction", "Goal", "Path", "Source", "Theme"],
        },
        "Openness": {
            "event type": "Openness",
            "keywords": [],
            "event description": "The event is related to openness.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Barrier {ROLE_Barrier} Theme {ROLE_Theme} Useful Location {ROLE_Useful_location}.",
            "valid roles": ["Barrier", "Theme", "Useful_location"],
        },
        "Participation": {
            "event type": "Participation",
            "keywords": [],
            "event description": "The event is related to participation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Event {ROLE_Event} Participants {ROLE_Participants}.",
            "valid roles": ["Event", "Participants"],
        },
        "Perception_active": {
            "event type": "Perception_active",
            "keywords": [],
            "event description": "The event is related to perception active.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Direction {ROLE_Direction} Perceiver Agentive {ROLE_Perceiver_agentive} Phenomenon {ROLE_Phenomenon}.",
            "valid roles": ["Direction", "Perceiver_agentive", "Phenomenon"],
        },
        "Placing": {
            "event type": "Placing",
            "keywords": [],
            "event description": "The event is related to placing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Location {ROLE_Location} Theme {ROLE_Theme}.",
            "valid roles": ["Agent", "Cause", "Location", "Theme"],
        },
        "Practice": {
            "event type": "Practice",
            "keywords": [],
            "event description": "The event is related to practice.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Action {ROLE_Action} Agent {ROLE_Agent} Occasion {ROLE_Occasion}.",
            "valid roles": ["Action", "Agent", "Occasion"],
        },
        "Presence": {
            "event type": "Presence",
            "keywords": [],
            "event description": "The event is related to presence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Circumstances {ROLE_Circumstances} Duration {ROLE_Duration} Entity {ROLE_Entity} Inherent Purpose {ROLE_Inherent_purpose} Place {ROLE_Place} Time {ROLE_Time}.",
            "valid roles": ["Circumstances", "Duration", "Entity", "Inherent_purpose", "Place", "Time"],
        },
        "Preventing_or_letting": {
            "event type": "Preventing_or_letting",
            "keywords": [],
            "event description": "The event is related to preventing letting.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Event {ROLE_Event} Means {ROLE_Means} Potential Hindrance {ROLE_Potential_hindrance}.",
            "valid roles": ["Agent", "Event", "Means", "Potential_hindrance"],
        },
        "Process_end": {
            "event type": "Process_end",
            "keywords": [],
            "event description": "The event is related to process end.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Final Subevent {ROLE_Final_subevent} Process {ROLE_Process} State {ROLE_State} Time {ROLE_Time}.",
            "valid roles": ["Agent", "Cause", "Final_subevent", "Process", "State", "Time"],
        },
        "Process_start": {
            "event type": "Process_start",
            "keywords": [],
            "event description": "The event is related to process start.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Event {ROLE_Event} Initial Subevent {ROLE_Initial_subevent} Time {ROLE_Time}.",
            "valid roles": ["Agent", "Event", "Initial_subevent", "Time"],
        },
        "Protest": {
            "event type": "Protest",
            "keywords": [],
            "event description": "The event is related to protest.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Arguer {ROLE_Arguer} Content {ROLE_Content}.",
            "valid roles": ["Addressee", "Arguer", "Content"],
        },
        "Quarreling": {
            "event type": "Quarreling",
            "keywords": [],
            "event description": "The event is related to quarreling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Arguer2 {ROLE_Arguer2} Arguers {ROLE_Arguers} Issue {ROLE_Issue}.",
            "valid roles": ["Arguer2", "Arguers", "Issue"],
        },
        "Ratification": {
            "event type": "Ratification",
            "keywords": [],
            "event description": "The event is related to ratification.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Proposal {ROLE_Proposal} Ratifier {ROLE_Ratifier}.",
            "valid roles": ["Proposal", "Ratifier"],
        },
        "Receiving": {
            "event type": "Receiving",
            "keywords": [],
            "event description": "The event is related to receiving.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Donor {ROLE_Donor} Recipient {ROLE_Recipient} Theme {ROLE_Theme}.",
            "valid roles": ["Donor", "Recipient", "Theme"],
        },
        "Recovering": {
            "event type": "Recovering",
            "keywords": [],
            "event description": "The event is related to recovering.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Entity {ROLE_Entity} Means {ROLE_Means}.",
            "valid roles": ["Agent", "Entity", "Means"],
        },
        "Removing": {
            "event type": "Removing",
            "keywords": [],
            "event description": "The event is related to removing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Goal {ROLE_Goal} Source {ROLE_Source} Theme {ROLE_Theme}.",
            "valid roles": ["Agent", "Cause", "Goal", "Source", "Theme"],
        },
        "Request": {
            "event type": "Request",
            "keywords": [],
            "event description": "The event is related to request.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Medium {ROLE_Medium} Message {ROLE_Message} Speaker {ROLE_Speaker}.",
            "valid roles": ["Addressee", "Medium", "Message", "Speaker"],
        },
        "Research": {
            "event type": "Research",
            "keywords": [],
            "event description": "The event is related to research.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Field {ROLE_Field} Researcher {ROLE_Researcher} Topic {ROLE_Topic}.",
            "valid roles": ["Field", "Researcher", "Topic"],
        },
        "Resolve_problem": {
            "event type": "Resolve_problem",
            "keywords": [],
            "event description": "The event is related to resolve problem.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Cause {ROLE_Cause} Means {ROLE_Means} Problem {ROLE_Problem}.",
            "valid roles": ["Agent", "Cause", "Means", "Problem"],
        },
        "Response": {
            "event type": "Response",
            "keywords": [],
            "event description": "The event is related to response.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Responding Entity {ROLE_Responding_entity} Response {ROLE_Response} Trigger {ROLE_Trigger}.",
            "valid roles": ["Agent", "Responding_entity", "Response", "Trigger"],
        },
        "Reveal_secret": {
            "event type": "Reveal_secret",
            "keywords": [],
            "event description": "The event is related to reveal secret.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Information {ROLE_Information} Speaker {ROLE_Speaker} Topic {ROLE_Topic}.",
            "valid roles": ["Addressee", "Information", "Speaker", "Topic"],
        },
        "Revenge": {
            "event type": "Revenge",
            "keywords": [],
            "event description": "The event is related to revenge.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Avenger {ROLE_Avenger} Injured Party {ROLE_Injured_party} Injury {ROLE_Injury} Offender {ROLE_Offender} Punishment {ROLE_Punishment}.",
            "valid roles": ["Avenger", "Injured_party", "Injury", "Offender", "Punishment"],
        },
        "Rite": {
            "event type": "Rite",
            "keywords": [],
            "event description": "The event is related to rite.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Member {ROLE_Member} Object {ROLE_Object} Type {ROLE_Type}.",
            "valid roles": ["Member", "Object", "Type"],
        },
        "Scrutiny": {
            "event type": "Scrutiny",
            "keywords": [],
            "event description": "The event is related to scrutiny.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cognizer {ROLE_Cognizer} Ground {ROLE_Ground} Instrument {ROLE_Instrument} Phenomenon {ROLE_Phenomenon} Unwanted Entity {ROLE_Unwanted_entity}.",
            "valid roles": ["Cognizer", "Ground", "Instrument", "Phenomenon", "Unwanted_entity"],
        },
        "Self_motion": {
            "event type": "Self_motion",
            "keywords": [],
            "event description": "The event is related to self motion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Direction {ROLE_Direction} Distance {ROLE_Distance} Goal {ROLE_Goal} Path {ROLE_Path} Self Mover {ROLE_Self_mover} Source {ROLE_Source}.",
            "valid roles": ["Direction", "Distance", "Goal", "Path", "Self_mover", "Source"],
        },
        "Sending": {
            "event type": "Sending",
            "keywords": [],
            "event description": "The event is related to sending.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Goal {ROLE_Goal} Means {ROLE_Means} Recipient {ROLE_Recipient} Sender {ROLE_Sender} Source {ROLE_Source} Theme {ROLE_Theme} Transferors {ROLE_Transferors} Vehicle {ROLE_Vehicle}.",
            "valid roles": ["Goal", "Means", "Recipient", "Sender", "Source", "Theme", "Transferors", "Vehicle"],
        },
        "Sign_agreement": {
            "event type": "Sign_agreement",
            "keywords": [],
            "event description": "The event is related to sign agreement.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agreement {ROLE_Agreement} Signatory {ROLE_Signatory}.",
            "valid roles": ["Agreement", "Signatory"],
        },
        "Social_event": {
            "event type": "Social_event",
            "keywords": [],
            "event description": "The event is related to social event.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Attendees {ROLE_Attendees} Beneficiary {ROLE_Beneficiary} Host {ROLE_Host} Occasion {ROLE_Occasion} Social Event {ROLE_Social_event}.",
            "valid roles": ["Attendees", "Beneficiary", "Host", "Occasion", "Social_event"],
        },
        "Statement": {
            "event type": "Statement",
            "keywords": [],
            "event description": "The event is related to statement.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Medium {ROLE_Medium} Message {ROLE_Message} Speaker {ROLE_Speaker}.",
            "valid roles": ["Addressee", "Medium", "Message", "Speaker"],
        },
        "Supply": {
            "event type": "Supply",
            "keywords": [],
            "event description": "The event is related to supply.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Imposed Purpose {ROLE_Imposed_purpose} Recipient {ROLE_Recipient} Supplier {ROLE_Supplier} Theme {ROLE_Theme}.",
            "valid roles": ["Imposed_purpose", "Recipient", "Supplier", "Theme"],
        },
        "Supporting": {
            "event type": "Supporting",
            "keywords": [],
            "event description": "The event is related to supporting.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Supported {ROLE_Supported} Supporter {ROLE_Supporter}.",
            "valid roles": ["Supported", "Supporter"],
        },
        "Telling": {
            "event type": "Telling",
            "keywords": [],
            "event description": "The event is related to telling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Message {ROLE_Message} Speaker {ROLE_Speaker}.",
            "valid roles": ["Addressee", "Message", "Speaker"],
        },
        "Terrorism": {
            "event type": "Terrorism",
            "keywords": [],
            "event description": "The event is related to terrorism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Act {ROLE_Act} Instrument {ROLE_Instrument} Terrorist {ROLE_Terrorist} Victim {ROLE_Victim}.",
            "valid roles": ["Act", "Instrument", "Terrorist", "Victim"],
        },
        "Testing": {
            "event type": "Testing",
            "keywords": [],
            "event description": "The event is related to testing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Circumstances {ROLE_Circumstances} Means {ROLE_Means} Product {ROLE_Product} Result {ROLE_Result} Tested Property {ROLE_Tested_property} Tester {ROLE_Tester}.",
            "valid roles": ["Circumstances", "Means", "Product", "Result", "Tested_property", "Tester"],
        },
        "Theft": {
            "event type": "Theft",
            "keywords": [],
            "event description": "The event is related to theft.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Goods {ROLE_Goods} Instrument {ROLE_Instrument} Means {ROLE_Means} Perpetrator {ROLE_Perpetrator} Source {ROLE_Source} Victim {ROLE_Victim}.",
            "valid roles": ["Goods", "Instrument", "Means", "Perpetrator", "Source", "Victim"],
        },
        "Traveling": {
            "event type": "Traveling",
            "keywords": [],
            "event description": "The event is related to traveling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Area {ROLE_Area} Distance {ROLE_Distance} Entity {ROLE_Entity} Goal {ROLE_Goal} Means {ROLE_Means} Path {ROLE_Path} Purpose {ROLE_Purpose} Traveler {ROLE_Traveler}.",
            "valid roles": ["Area", "Distance", "Entity", "Goal", "Means", "Path", "Purpose", "Traveler"],
        },
        "Using": {
            "event type": "Using",
            "keywords": [],
            "event description": "The event is related to using.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Agent {ROLE_Agent} Instrument {ROLE_Instrument} Means {ROLE_Means} Purpose {ROLE_Purpose}.",
            "valid roles": ["Agent", "Instrument", "Means", "Purpose"],
        },
        "Wearing": {
            "event type": "Wearing",
            "keywords": [],
            "event description": "The event is related to wearing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Body Location {ROLE_Body_location} Clothing {ROLE_Clothing} Wearer {ROLE_Wearer}.",
            "valid roles": ["Body_location", "Clothing", "Wearer"],
        },
        "Writing": {
            "event type": "Writing",
            "keywords": [],
            "event description": "The event is related to writing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Addressee {ROLE_Addressee} Author {ROLE_Author} Instrument {ROLE_Instrument} Text {ROLE_Text}.",
            "valid roles": ["Addressee", "Author", "Instrument", "Text"],
        },  
    },
    "mee-en": {
        "Business_START-ORG": {
            "event description": "The event is related to business start organization.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },  
        "Conflict_Attack": {
            "event description": "The event is related to conflict attack.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },  
        "Conflict_Demonstrate": {
            "event description": "The event is related to conflict demonstrate.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },  
        "Contact_Meet": {
            "event description": "The event is related to contact meet.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Contact_Phone-Write": {
            "event description": "The event is related to contact phone write.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Justice_Arrest-Jail": {
            "event description": "The event is related to justice arrest jail.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Life_Be-Born": {
            "event description": "The event is related to life born.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Life_Die": {
            "event description": "The event is related to life die.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },  
        "Life_Divorce": {
            "event description": "The event is related to life divorce.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Life_Injure": {
            "event description": "The event is related to life injure.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Life_Marry": {
            "event description": "The event is related to life marry.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Movement_Transport": {
            "event description": "The event is related to movement transport.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Personnel_End-Position": {
            "event description": "The event is related to personnel end position.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Personnel_Start-Position": {
            "event description": "The event is related to personnel start position.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Transaction_Transfer-Money": {
            "event description": "The event is related to transaction transfer-money.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "Transaction_Transfer-Ownership": {
            "event description": "The event is related to transaction transfer ownership.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
    },
    "rams": {
        "artifactexistence.damagedestroy.damage": {
            "event type": "artifactexistence.damagedestroy.damage",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy damage.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_damager} damaged {ROLE_artifact} using {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": ['damager', 'artifact', 'instrument', 'place'],
        },
        "artifactexistence.damagedestroy.destroy": {
            "event type": "artifactexistence.damagedestroy.destroy",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy destroy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_destroyer} destroyed {ROLE_artifact} using {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": ['destroyer', 'artifact', 'instrument', 'place'],
        },
        "artifactexistence.damagedestroy.n/a": {
            "event type": "artifactexistence.damagedestroy.n/a",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_damagerdestroyer} damaged or destroyed {ROLE_artifact} using {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": ['damagerdestroyer', 'artifact', 'instrument', 'place'],
        },
        "conflict.attack.airstrikemissilestrike": {
            "event type": "conflict.attack.airstrikemissilestrike",
            "keywords": [],
            "event description": "The event is related to conflict attack airstrike missile strike.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.biologicalchemicalpoisonattack": {
            "event type": "conflict.attack.biologicalchemicalpoisonattack",
            "keywords": [],
            "event description": "The event is related to conflict attack biological chemical poison attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.bombing": {
            "event type": "conflict.attack.bombing",
            "keywords": [],
            "event description": "The event is related to conflict attack bombing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.firearmattack": {
            "event type": "conflict.attack.firearmattack",
            "keywords": [],
            "event description": "The event is related to conflict attack firearm attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.hanging": {
            "event type": "conflict.attack.hanging",
            "keywords": [],
            "event description": "The event is related to conflict attack hanging.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.invade": {
            "event type": "conflict.attack.invade",
            "keywords": [],
            "event description": "The event is related to conflict attack invade.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.n/a": {
            "event type": "conflict.attack.n/a",
            "keywords": [],
            "event description": "The event is related to conflict attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.selfdirectedbattle": {
            "event type": "conflict.attack.selfdirectedbattle",
            "keywords": [],
            "event description": "The event is related to conflict attack self directed battle.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.setfire": {
            "event type": "conflict.attack.setfire",
            "keywords": [],
            "event description": "The event is related to conflict attack setfire.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.stabbing": {
            "event type": "conflict.attack.stabbing",
            "keywords": [],
            "event description": "The event is related to conflict attack stabbing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.attack.stealrobhijack": {
            "event type": "conflict.attack.stealrobhijack",
            "keywords": [],
            "event description": "The event is related to conflict attack steal rob hijack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place} place, in order to take {ROLE_artifact}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place', 'artifact'],
        },
        "conflict.attack.strangling": {
            "event type": "conflict.attack.strangling",
            "keywords": [],
            "event description": "The event is related to conflict attack strangling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_attacker} attacked {ROLE_target} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['attacker', 'target', 'instrument', 'place'],
        },
        "conflict.demonstrate.marchprotestpoliticalgathering": {
            "event type": "conflict.demonstrate.marchprotestpoliticalgathering",
            "keywords": [],
            "event description": "The event is related to conflict demonstrate march protest political gathering.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_demonstrator} was in a demonstration or protest at {ROLE_place}.",
            "valid roles": ['demonstrator', 'place'],
        },
        "conflict.demonstrate.n/a": {
            "event type": "conflict.demonstrate.n/a",
            "keywords": [],
            "event description": "The event is related to conflict demonstrate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_demonstrator} was in a demonstration at {ROLE_place}.",
            "valid roles": ['demonstrator', 'place'],
        },
        "conflict.yield.n/a": {
            "event type": "conflict.yield.n/a",
            "keywords": [],
            "event description": "The event is related to conflict yield.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_yielder} yielded to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['yielder', 'recipient', 'place'],
        },
        "conflict.yield.retreat": {
            "event type": "conflict.yield.retreat",
            "keywords": [],
            "event description": "The event is related to conflict yield retreat.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_retreater} retreated from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['retreater', 'origin', 'destination'],
        },
        "conflict.yield.surrender": {
            "event type": "conflict.yield.surrender",
            "keywords": [],
            "event description": "The event is related to conflict yield surrender.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_surrenderer} surrendered to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['surrenderer', 'recipient', 'place'],
        },
        "contact.collaborate.correspondence": {
            "event type": "contact.collaborate.correspondence",
            "keywords": [],
            "event description": "The event is related to contact collaborate correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated remotely with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.collaborate.meet": {
            "event type": "contact.collaborate.meet",
            "keywords": [],
            "event description": "The event is related to contact collaborate meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} met face-to-face with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.collaborate.n/a": {
            "event type": "contact.collaborate.n/a",
            "keywords": [],
            "event description": "The event is related to contact collaborate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.commandorder.broadcast": {
            "event type": "contact.commandorder.broadcast",
            "keywords": [],
            "event description": "The event is related to contact command order broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.commandorder.correspondence": {
            "event type": "contact.commandorder.correspondence",
            "keywords": [],
            "event description": "The event is related to contact command order correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.commandorder.meet": {
            "event type": "contact.commandorder.meet",
            "keywords": [],
            "event description": "The event is related to contact command order meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.commandorder.n/a": {
            "event type": "contact.commandorder.n/a",
            "keywords": [],
            "event description": "The event is related to contact command order.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.commitmentpromiseexpressintent.broadcast": {
            "event type": "contact.commitmentpromiseexpressintent.broadcast",
            "keywords": [],
            "event description": "The event is related to contact commitment promise express intent broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.commitmentpromiseexpressintent.correspondence": {
            "event type": "contact.commitmentpromiseexpressintent.correspondence",
            "keywords": [],
            "event description": "The event is related to contact commitment promise express intent correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.commitmentpromiseexpressintent.meet": {
            "event type": "contact.commitmentpromiseexpressintent.meet",
            "keywords": [],
            "event description": "The event is related to contact commitment promise express intent meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.commitmentpromiseexpressintent.n/a": {
            "event type": "contact.commitmentpromiseexpressintent.n/a",
            "keywords": [],
            "event description": "The event is related to contact commitment promise express intent.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.discussion.correspondence": {
            "event type": "contact.discussion.correspondence",
            "keywords": [],
            "event description": "The event is related to contact discussion correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated remotely with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.discussion.meet": {
            "event type": "contact.discussion.meet",
            "keywords": [],
            "event description": "The event is related to contact discussion meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} met face-to-face with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.discussion.n/a": {
            "event type": "contact.discussion.n/a",
            "keywords": [],
            "event description": "The event is related to contact discussion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.funeralvigil.meet": {
            "event type": "contact.funeralvigil.meet",
            "keywords": [],
            "event description": "The event is related to contact funeral vigil meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} met face-to-face with {ROLE_participant} during a funeral or vigil for {ROLE_deceased} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'deceased', 'place'],
        },
        "contact.funeralvigil.n/a": {
            "event type": "contact.funeralvigil.n/a",
            "keywords": [],
            "event description": "The event is related to contact funeral vigil.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated with {ROLE_participant} during a funeral or vigil for {ROLE_deceased} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'deceased', 'place'],
        },
        "contact.mediastatement.broadcast": {
            "event type": "contact.mediastatement.broadcast",
            "keywords": [],
            "event description": "The event is related to contact media statement broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.mediastatement.n/a": {
            "event type": "contact.mediastatement.n/a",
            "keywords": [],
            "event description": "The event is related to contact media statement.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.negotiate.correspondence": {
            "event type": "contact.negotiate.correspondence",
            "keywords": [],
            "event description": "The event is related to contact negotiate correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated remotely with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.negotiate.meet": {
            "event type": "contact.negotiate.meet",
            "keywords": [],
            "event description": "The event is related to contact negotiate meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} met face-to-face with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.negotiate.n/a": {
            "event type": "contact.negotiate.n/a",
            "keywords": [],
            "event description": "The event is related to contact negotiate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} communicated with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "contact.prevarication.broadcast": {
            "event type": "contact.prevarication.broadcast",
            "keywords": [],
            "event description": "The event is related to contact prevarication broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.prevarication.correspondence": {
            "event type": "contact.prevarication.correspondence",
            "keywords": [],
            "event description": "The event is related to contact prevarication correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.prevarication.meet": {
            "event type": "contact.prevarication.meet",
            "keywords": [],
            "event description": "The event is related to contact prevarication meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.prevarication.n/a": {
            "event type": "contact.prevarication.n/a",
            "keywords": [],
            "event description": "The event is related to contact prevarication.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.publicstatementinperson.broadcast": {
            "event type": "contact.publicstatementinperson.broadcast",
            "keywords": [],
            "event description": "The event is related to contact public statement in person broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.publicstatementinperson.n/a": {
            "event type": "contact.publicstatementinperson.n/a",
            "keywords": [],
            "event description": "The event is related to contact public statement in person.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.requestadvise.broadcast": {
            "event type": "contact.requestadvise.broadcast",
            "keywords": [],
            "event description": "The event is related to contact request advise broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.requestadvise.correspondence": {
            "event type": "contact.requestadvise.correspondence",
            "keywords": [],
            "event description": "The event is related to contact request advise correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.requestadvise.meet": {
            "event type": "contact.requestadvise.meet",
            "keywords": [],
            "event description": "The event is related to contact request advise meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.requestadvise.n/a": {
            "event type": "contact.requestadvise.n/a",
            "keywords": [],
            "event description": "The event is related to contact request advise.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.threatencoerce.broadcast": {
            "event type": "contact.threatencoerce.broadcast",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated to {ROLE_recipient} at {ROLE_place} place (one-way communication).",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.threatencoerce.correspondence": {
            "event type": "contact.threatencoerce.correspondence",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated remotely with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.threatencoerce.meet": {
            "event type": "contact.threatencoerce.meet",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} met face-to-face with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "contact.threatencoerce.n/a": {
            "event type": "contact.threatencoerce.n/a",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_communicator} communicated with {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['communicator', 'recipient', 'place'],
        },
        "disaster.accidentcrash.accidentcrash": {
            "event type": "disaster.accidentcrash.accidentcrash",
            "keywords": [],
            "event description": "The event is related to disaster accidentcrash accidentcrash.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_driverpassenger} person in {ROLE_vehicle} vehicle crashed into {ROLE_crashobject} at {ROLE_place}.",
            "valid roles": ['driverpassenger', 'vehicle', 'crashobject', 'place'],
        },
        "disaster.fireexplosion.fireexplosion": {
            "event type": "disaster.fireexplosion.fireexplosion",
            "keywords": [],
            "event description": "The event is related to disaster fireexplosion fireexplosion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_fireexplosionobject} caught fire or exploded from {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": ['fireexplosionobject', 'instrument', 'place'],
        },
        "government.agreements.acceptagreementcontractceasefire": {
            "event type": "government.agreements.acceptagreementcontractceasefire",
            "keywords": [],
            "event description": "The event is related to government agreements accept agreement contract ceasefire.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} and {ROLE_participant} signed an agreement at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "government.agreements.n/a": {
            "event type": "government.agreements.n/a",
            "keywords": [],
            "event description": "The event is related to government agreements.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} and {ROLE_participant} signed an agreement at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "government.agreements.rejectnullifyagreementcontractceasefire": {
            "event type": "government.agreements.rejectnullifyagreementcontractceasefire",
            "keywords": [],
            "event description": "The event is related to government agreements reject nullify agreement contract ceasefire.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_rejecternullifier} rejected or nullified an agreement with {ROLE_otherparticipant} at {ROLE_place}.",
            "valid roles": ['rejecternullifier', 'otherparticipant', 'place'],
        },
        "government.agreements.violateagreement": {
            "event type": "government.agreements.violateagreement",
            "keywords": [],
            "event description": "The event is related to government agreements violate agreement.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_violator} violated an agreement with {ROLE_otherparticipant} at {ROLE_place}.",
            "valid roles": ['violator', 'otherparticipant', 'place'],
        },
        "government.formation.mergegpe": {
            "event type": "government.formation.mergegpe",
            "keywords": [],
            "event description": "The event is related to government formation mergegpe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_participant} merged with {ROLE_participant} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'place'],
        },
        "government.formation.n/a": {
            "event type": "government.formation.n/a",
            "keywords": [],
            "event description": "The event is related to government formation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_gpe} was formed by {ROLE_founder} at {ROLE_place}.",
            "valid roles": ['gpe', 'founder', 'place'],
        },
        "government.formation.startgpe": {
            "event type": "government.formation.startgpe",
            "keywords": [],
            "event description": "The event is related to government formation startpage.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_gpe} was started by {ROLE_founder} at {ROLE_place}.",
            "valid roles": ['gpe', 'founder', 'place'],
        },
        "government.legislate.legislate": {
            "event type": "government.legislate.legislate",
            "keywords": [],
            "event description": "The event is related to government legislate legislate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_governmentbody} legislature enacted {ROLE_law} law at {ROLE_place}.",
            "valid roles": ['governmentbody', 'law', 'place'],
        },
        "government.spy.spy": {
            "event type": "government.spy.spy",
            "keywords": [],
            "event description": "The event is related to government spy spy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_spy} spied on {ROLE_observedentity} to the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['spy', 'observedentity', 'beneficiary', 'place'],
        },
        "government.vote.castvote": {
            "event type": "government.vote.castvote",
            "keywords": [],
            "event description": "The event is related to government vote castvote.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_voter} voted for {ROLE_candidate} on {ROLE_ballot} ballot with {ROLE_result} results at {ROLE_place}.",
            "valid roles": ['voter', 'candidate', 'ballot', 'result', 'place'],
        },
        "government.vote.n/a": {
            "event type": "government.vote.n/a",
            "keywords": [],
            "event description": "The event is related to government vote.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_voter} voted for {ROLE_candidate} on {ROLE_ballot} ballot with {ROLE_result} results at {ROLE_place}.",
            "valid roles": ['voter', 'candidate', 'ballot', 'result', 'place'],
        },
        "government.vote.violationspreventvote": {
            "event type": "government.vote.violationspreventvote",
            "keywords": [],
            "event description": "The event is related to government vote violations prevent vote.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevented {ROLE_voter} from voting for {ROLE_candidate} on {ROLE_ballot} ballot at {ROLE_place}.",
            "valid roles": ['preventer', 'voter', 'candidate', 'ballot', 'place'],
        },
        "inspection.sensoryobserve.inspectpeopleorganization": {
            "event type": "inspection.sensoryobserve.inspectpeopleorganization",
            "keywords": [],
            "event description": "The event is related to inspection sensory observe inspect people organization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_inspector} inspected {ROLE_inspectedentity} at {ROLE_place}.",
            "valid roles": ['inspector', 'inspectedentity', 'place'],
        },
        "inspection.sensoryobserve.monitorelection": {
            "event type": "inspection.sensoryobserve.monitorelection",
            "keywords": [],
            "event description": "The event is related to inspection sensory observe monitor election.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_monitor} monitored {ROLE_monitoredentity} taking part in an election at {ROLE_place}.",
            "valid roles": ['monitor', 'monitoredentity', 'place'],
        },
        "inspection.sensoryobserve.n/a": {
            "event type": "inspection.sensoryobserve.n/a",
            "keywords": [],
            "event description": "The event is related to inspection sensory observe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_observer} observed {ROLE_observedentity} at {ROLE_place}.",
            "valid roles": ['observer', 'observedentity', 'place'],
        },
        "inspection.sensoryobserve.physicalinvestigateinspect": {
            "event type": "inspection.sensoryobserve.physicalinvestigateinspect",
            "keywords": [],
            "event description": "The event is related to inspection sensory observe physical investigate inspect.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_inspector} inspected {ROLE_inspectedentity} at {ROLE_place}.",
            "valid roles": ['inspector', 'inspectedentity', 'place'],
        },
        "justice.arrestjaildetain.arrestjaildetain": {
            "event type": "justice.arrestjaildetain.arrestjaildetain",
            "keywords": [],
            "event description": "The event is related to justice arrest jail detain.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_jailer} arrested or jailed {ROLE_detainee} for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": ['jailer', 'detainee', 'crime', 'place'],
        },
        "justice.initiatejudicialprocess.chargeindict": {
            "event type": "justice.initiatejudicialprocess.chargeindict",
            "keywords": [],
            "event description": "The event is related to justice initiative judicial process charge indict.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_prosecutor} charged or indicted {ROLE_defendant} before {ROLE_judgecourt} court or judge for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": ['prosecutor', 'defendant', 'judgecourt', 'crime', 'place'],
        },
        "justice.initiatejudicialprocess.n/a": {
            "event type": "justice.initiatejudicialprocess.n/a",
            "keywords": [],
            "event description": "The event is related to justice initiative judicial process.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_prosecutor} initiated judicial process pertaining to {ROLE_defendant} before {ROLE_judgecourt} court or judge for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": ['prosecutor', 'defendant', 'judgecourt', 'crime', 'place'],
        },
        "justice.initiatejudicialprocess.trialhearing": {
            "event type": "justice.initiatejudicialprocess.trialhearing",
            "keywords": [],
            "event description": "The event is related to justice initiative judicial process trial hearing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_prosecutor} tried {ROLE_defendant} before {ROLE_judgecourt} court or judge for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": ['prosecutor', 'defendant', 'judgecourt', 'crime', 'place'],
        },
        "justice.investigate.investigatecrime": {
            "event type": "justice.investigate.investigatecrime",
            "keywords": [],
            "event description": "The event is related to justice investigate investigate crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_investigator} investigated {ROLE_defendant} for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": ['investigator', 'defendant', 'crime', 'place'],
        },
        "justice.investigate.n/a": {
            "event type": "justice.investigate.n/a",
            "keywords": [],
            "event description": "The event is related to justice investigate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_investigator} investigated {ROLE_defendant} at {ROLE_place}.",
            "valid roles": ['investigator', 'defendant', 'place'],
        },
        "justice.judicialconsequences.convict": {
            "event type": "justice.judicialconsequences.convict",
            "keywords": [],
            "event description": "The event is related to justice judicial consequences convict.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_judgecourt} court or judge convicted {ROLE_defendant} of {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": ['judgecourt', 'defendant', 'crime', 'place'],
        },
        "justice.judicialconsequences.execute": {
            "event type": "justice.judicialconsequences.execute",
            "keywords": [],
            "event description": "The event is related to justice judicial consequences execute.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_executioner} executed {ROLE_defendant} for {ROLE_crime} crime at {ROLE_place}.",
            "valid roles": ['executioner', 'defendant', 'crime', 'place'],
        },
        "justice.judicialconsequences.extradite": {
            "event type": "justice.judicialconsequences.extradite",
            "keywords": [],
            "event description": "The event is related to justice judicial consequences extradite.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_extraditer} extradited {ROLE_defendant} for {ROLE_crime} crime from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['extraditer', 'defendant', 'crime', 'origin', 'destination'],
        },
        "justice.judicialconsequences.n/a": {
            "event type": "justice.judicialconsequences.n/a",
            "keywords": [],
            "event description": "The event is related to justice judicial consequences.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_judgecourt} court or judge decided consequences of {ROLE_crime} crime, committed by {ROLE_defendant}, at {ROLE_place}.",
            "valid roles": ['judgecourt', 'defendant', 'crime', 'place'],
        },
        "life.die.deathcausedbyviolentevents": {
            "event type": "life.die.deathcausedbyviolentevents",
            "keywords": [],
            "event description": "The event is related to life die death caused by violent events.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_killer} killed {ROLE_victim} using {ROLE_instrument} instrument at {ROLE_place}.",
            "valid roles": ['killer', 'victim', 'instrument', 'place'],
        },
        "life.die.n/a": {
            "event type": "life.die.n/a",
            "keywords": [],
            "event description": "The event is related to life die.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} died at {ROLE_place} place, killed by {ROLE_killer} killer.",
            "valid roles": ['victim', 'place', 'killer'],
        },
        "life.die.nonviolentdeath": {
            "event type": "life.die.nonviolentdeath",
            "keywords": [],
            "event description": "The event is related to life die non violent death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} died at {ROLE_place} place, killed by {ROLE_killer} killer.",
            "valid roles": ['victim', 'place', 'killer'],
        },
        "life.injure.illnessdegradationhungerthirst": {
            "event type": "life.injure.illnessdegradationhungerthirst",
            "keywords": [],
            "event description": "The event is related to life injure illness degradation hunger thirst.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} has extreme hunger imposed by {ROLE_injurer} injurer at {ROLE_place}.",
            "valid roles": ['victim', 'place', 'injurer'],
        },
        "life.injure.illnessdegradationphysical": {
            "event type": "life.injure.illnessdegradationphysical",
            "keywords": [],
            "event description": "The event is related to life injure illness degradation physical.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} person has some physical degradation imposed by {ROLE_injurer} injurer at {ROLE_place}.",
            "valid roles": ['victim', 'place', 'injurer'],
        },
        "life.injure.injurycausedbyviolentevents": {
            "event type": "life.injure.injurycausedbyviolentevents",
            "keywords": [],
            "event description": "The event is related to life injure injury caused by violent events.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_injurer} injured {ROLE_victim} using {ROLE_instrument} instrument issue at {ROLE_place}.",
            "valid roles": ['injurer', 'victim', 'instrument', 'place'],
        },
        "life.injure.n/a": {
            "event type": "life.injure.n/a",
            "keywords": [],
            "event description": "The event is related to life injure.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_victim} was injured by {ROLE_injurer} at {ROLE_place}.",
            "valid roles": ['victim', 'injurer', 'place'],
        },
        "manufacture.artifact.build": {
            "event type": "manufacture.artifact.build",
            "keywords": [],
            "event description": "The event is related to manufacture artifact build.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_manufacturer} manufactured or created or produced {ROLE_artifact} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['manufacturer', 'artifact', 'instrument', 'place'],
        },
        "manufacture.artifact.createintellectualproperty": {
            "event type": "manufacture.artifact.createintellectualproperty",
            "keywords": [],
            "event description": "The event is related to manufacture artifact create intellectual property.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_manufacturer} manufactured or created or produced {ROLE_artifact} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['manufacturer', 'artifact', 'instrument', 'place'],
        },
        "manufacture.artifact.createmanufacture": {
            "event type": "manufacture.artifact.createmanufacture",
            "keywords": [],
            "event description": "The event is related to manufacture artifact create manufacture.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_manufacturer} manufactured or created or produced {ROLE_artifact} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['manufacturer', 'artifact', 'instrument', 'place'],
        },
        "manufacture.artifact.n/a": {
            "event type": "manufacture.artifact.n/a",
            "keywords": [],
            "event description": "The event is related to manufacture artifact.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_manufacturer} manufactured or created or produced {ROLE_artifact} using {ROLE_instrument} at {ROLE_place}.",
            "valid roles": ['manufacturer', 'artifact', 'instrument', 'place'],
        },
        "movement.transportartifact.bringcarryunload": {
            "event type": "movement.transportartifact.bringcarryunload",
            "keywords": [],
            "event description": "The event is related to movement transport artifact bring carry unload.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'artifact', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportartifact.disperseseparate": {
            "event type": "movement.transportartifact.disperseseparate",
            "keywords": [],
            "event description": "The event is related to movement transport artifact disperse separate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'artifact', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportartifact.fall": {
            "event type": "movement.transportartifact.fall",
            "keywords": [],
            "event description": "The event is related to movement transport artifact fall.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_artifact} fell from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['artifact', 'origin', 'destination'],
        },
        "movement.transportartifact.grantentry": {
            "event type": "movement.transportartifact.grantentry",
            "keywords": [],
            "event description": "The event is related to movement transport artifact grant entry.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} grants {ROLE_artifact} entry to {ROLE_origin} place from {ROLE_destination} place.",
            "valid roles": ['transporter', 'artifact', 'origin', 'destination'],
        },
        "movement.transportartifact.hide": {
            "event type": "movement.transportartifact.hide",
            "keywords": [],
            "event description": "The event is related to movement transport artifact hide.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} concealed {ROLE_artifact} in {ROLE_hidingplace} place, transported in {ROLE_vehicle} vehicle from {ROLE_origin} place.",
            "valid roles": ['transporter', 'artifact', 'hidingplace', 'vehicle', 'origin'],
        },
        "movement.transportartifact.n/a": {
            "event type": "movement.transportartifact.n/a",
            "keywords": [],
            "event description": "The event is related to movement transport artifact.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'artifact', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportartifact.nonviolentthrowlaunch": {
            "event type": "movement.transportartifact.nonviolentthrowlaunch",
            "keywords": [],
            "event description": "The event is related to movement transport artifact nonviolent throw launch.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'artifact', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportartifact.prevententry": {
            "event type": "movement.transportartifact.prevententry",
            "keywords": [],
            "event description": "The event is related to movement transport artifact prevent entry.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevents {ROLE_transporter} from transporting {ROLE_artifact} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['preventer', 'transporter', 'artifact', 'origin', 'destination'],
        },
        "movement.transportartifact.preventexit": {
            "event type": "movement.transportartifact.preventexit",
            "keywords": [],
            "event description": "The event is related to movement transport artifact prevent exit.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevents {ROLE_transporter} from transporting {ROLE_artifact} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['preventer', 'transporter', 'artifact', 'origin', 'destination'],
        },
        "movement.transportartifact.receiveimport": {
            "event type": "movement.transportartifact.receiveimport",
            "keywords": [],
            "event description": "The event is related to movement transport artifact receive import.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'artifact', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportartifact.sendsupplyexport": {
            "event type": "movement.transportartifact.sendsupplyexport",
            "keywords": [],
            "event description": "The event is related to movement transport artifact send supply export.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'artifact', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportartifact.smuggleextract": {
            "event type": "movement.transportartifact.smuggleextract",
            "keywords": [],
            "event description": "The event is related to movement transport artifact smuggle extract.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_artifact} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'artifact', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportperson.bringcarryunload": {
            "event type": "movement.transportperson.bringcarryunload",
            "keywords": [],
            "event description": "The event is related to movement transport person bring carry unload.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'passenger', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportperson.disperseseparate": {
            "event type": "movement.transportperson.disperseseparate",
            "keywords": [],
            "event description": "The event is related to movement transport person disperse separate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'passenger', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportperson.evacuationrescue": {
            "event type": "movement.transportperson.evacuationrescue",
            "keywords": [],
            "event description": "The event is related to movement transport person evacuation rescue.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'passenger', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportperson.fall": {
            "event type": "movement.transportperson.fall",
            "keywords": [],
            "event description": "The event is related to movement transport person fall.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_passenger} fell from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['passenger', 'origin', 'destination'],
        },
        "movement.transportperson.grantentryasylum": {
            "event type": "movement.transportperson.grantentryasylum",
            "keywords": [],
            "event description": "The event is related to movement transport person grantentry asylum.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_granter} grants entry to {ROLE_transporter} transporting {ROLE_passenger} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['granter', 'transporter', 'passenger', 'origin', 'destination'],
        },
        "movement.transportperson.hide": {
            "event type": "movement.transportperson.hide",
            "keywords": [],
            "event description": "The event is related to movement transport person hide.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} concealed {ROLE_passenger} in {ROLE_hidingplace} place, transported in {ROLE_vehicle} vehicle from {ROLE_origin} place.",
            "valid roles": ['transporter', 'passenger', 'hidingplace', 'vehicle', 'origin'],
        },
        "movement.transportperson.n/a": {
            "event type": "movement.transportperson.n/a",
            "keywords": [],
            "event description": "The event is related to movement transport person.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'passenger', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportperson.prevententry": {
            "event type": "movement.transportperson.prevententry",
            "keywords": [],
            "event description": "The event is related to movement transport person prevent entry.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevents {ROLE_transporter} from transporting {ROLE_passenger} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['preventer', 'transporter', 'passenger', 'origin', 'destination'],
        },
        "movement.transportperson.preventexit": {
            "event type": "movement.transportperson.preventexit",
            "keywords": [],
            "event description": "The event is related to movement transport person prevent exit.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevents {ROLE_transporter} from transporting {ROLE_passenger} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['preventer', 'transporter', 'passenger', 'origin', 'destination'],
        },
        "movement.transportperson.selfmotion": {
            "event type": "movement.transportperson.selfmotion",
            "keywords": [],
            "event description": "The event is related to movement transport person self motion.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} moved in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'vehicle', 'origin', 'destination'],
        },
        "movement.transportperson.smuggleextract": {
            "event type": "movement.transportperson.smuggleextract",
            "keywords": [],
            "event description": "The event is related to movement transport person smuggle extract.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_transporter} transported {ROLE_passenger} in {ROLE_vehicle} from {ROLE_origin} place to {ROLE_destination} place.",
            "valid roles": ['transporter', 'passenger', 'vehicle', 'origin', 'destination'],
        },
        "personnel.elect.n/a": {
            "event type": "personnel.elect.n/a",
            "keywords": [],
            "event description": "The event is related to personnel elect.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_voter} elected {ROLE_candidate} at {ROLE_place}.",
            "valid roles": ['voter', 'candidate', 'place'],
        },
        "personnel.elect.winelection": {
            "event type": "personnel.elect.winelection",
            "keywords": [],
            "event description": "The event is related to personnel elect win election.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_voter} elected {ROLE_candidate} at {ROLE_place}.",
            "valid roles": ['voter', 'candidate', 'place'],
        },
        "personnel.endposition.firinglayoff": {
            "event type": "personnel.endposition.firinglayoff",
            "keywords": [],
            "event description": "The event is related to personnel end position firing layoff.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} stopped working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": ['employee', 'placeofemployment', 'place'],
        },
        "personnel.endposition.n/a": {
            "event type": "personnel.endposition.n/a",
            "keywords": [],
            "event description": "The event is related to personnel end position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} stopped working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": ['employee', 'placeofemployment', 'place'],
        },
        "personnel.endposition.quitretire": {
            "event type": "personnel.endposition.quitretire",
            "keywords": [],
            "event description": "The event is related to personnel end position quit retire.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} stopped working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": ['employee', 'placeofemployment', 'place'],
        },
        "personnel.startposition.hiring": {
            "event type": "personnel.startposition.hiring",
            "keywords": [],
            "event description": "The event is related to personnel start position hiring.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} started working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": ['employee', 'placeofemployment', 'place'],
        },
        "personnel.startposition.n/a": {
            "event type": "personnel.startposition.n/a",
            "keywords": [],
            "event description": "The event is related to personnel start position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_employee} started working at {ROLE_placeofemployment} at {ROLE_place}.",
            "valid roles": ['employee', 'placeofemployment', 'place'],
        },
        "transaction.transaction.embargosanction": {
            "event type": "transaction.transaction.embargosanction",
            "keywords": [],
            "event description": "The event is related to transaction transaction embargo sanction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevented {ROLE_giver} from giving {ROLE_artifactmoney} to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['preventer', 'giver', 'recipient', 'artifactmoney', 'place'],
        },
        "transaction.transaction.giftgrantprovideaid": {
            "event type": "transaction.transaction.giftgrantprovideaid",
            "keywords": [],
            "event description": "The event is related to transaction transaction gift grant provide aid.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave something to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'place'],
        },
        "transaction.transaction.n/a": {
            "event type": "transaction.transaction.n/a",
            "keywords": [],
            "event description": "The event is related to transaction transaction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "A transaction occurred between {ROLE_participant} and {ROLE_participant} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['participant', 'participant', 'beneficiary', 'place'],
        },
        "transaction.transaction.transfercontrol": {
            "event type": "transaction.transaction.transfercontrol",
            "keywords": [],
            "event description": "The event is related to transaction transaction transfer control.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} transferred control of {ROLE_territoryorfacility} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'territoryorfacility', 'place'],
        },
        "transaction.transfermoney.borrowlend": {
            "event type": "transaction.transfermoney.borrowlend",
            "keywords": [],
            "event description": "The event is related to transaction transfer money borrow lend.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'money', 'place'],
        },
        "transaction.transfermoney.embargosanction": {
            "event type": "transaction.transfermoney.embargosanction",
            "keywords": [],
            "event description": "The event is related to transaction transfer money embargo sanction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevented {ROLE_giver} from giving {ROLE_money} to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['preventer', 'giver', 'recipient', 'money', 'place'],
        },
        "transaction.transfermoney.giftgrantprovideaid": {
            "event type": "transaction.transfermoney.giftgrantprovideaid",
            "keywords": [],
            "event description": "The event is related to transaction transfer money gift grant provide aid.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'money', 'place'],
        },
        "transaction.transfermoney.n/a": {
            "event type": "transaction.transfermoney.n/a",
            "keywords": [],
            "event description": "The event is related to transaction transfer money.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'money', 'place'],
        },
        "transaction.transfermoney.payforservice": {
            "event type": "transaction.transfermoney.payforservice",
            "keywords": [],
            "event description": "The event is related to transaction transfer money payforservice.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'money', 'place'],
        },
        "transaction.transfermoney.purchase": {
            "event type": "transaction.transfermoney.purchase",
            "keywords": [],
            "event description": "The event is related to transaction transfer money purchase.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_money} money to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'money', 'place'],
        },
        "transaction.transferownership.borrowlend": {
            "event type": "transaction.transferownership.borrowlend",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership borrow lend.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_artifact} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'artifact', 'place'],
        },
        "transaction.transferownership.embargosanction": {
            "event type": "transaction.transferownership.embargosanction",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership embargo sanction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_preventer} prevented {ROLE_giver} from giving {ROLE_artifact} to {ROLE_recipient} at {ROLE_place}.",
            "valid roles": ['preventer', 'giver', 'recipient', 'artifact', 'place'],
        },
        "transaction.transferownership.giftgrantprovideaid": {
            "event type": "transaction.transferownership.giftgrantprovideaid",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership gift grant provide aid.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_artifact} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'artifact', 'place'],
        },
        "transaction.transferownership.n/a": {
            "event type": "transaction.transferownership.n/a",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_artifact} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'artifact', 'place'],
        },
        "transaction.transferownership.purchase": {
            "event type": "transaction.transferownership.purchase",
            "keywords": [],
            "event description": "The event is related to transaction transfer ownership purchase.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_giver} gave {ROLE_artifact} to {ROLE_recipient} for the benefit of {ROLE_beneficiary} at {ROLE_place}.",
            "valid roles": ['giver', 'recipient', 'beneficiary', 'artifact', 'place'],
        },
    },
    "wikievents": {
        "ArtifactExistence.DamageDestroyDisableDismantle.Damage": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.Damage",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle damage.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Damager} damaged {ROLE_Artifact} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ['Artifact', 'Damager', 'Instrument', 'Place'],
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Destroy": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.Destroy",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle destroy.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Destroyer} destroyed {ROLE_Artifact} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ['Artifact', 'Destroyer', 'Instrument', 'Place'],
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.DisableDefuse": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.DisableDefuse",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle disable defuse.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Disabler} disabled or defused {ROLE_Artifact} by using {ROLE_Instrument}.",
            "valid roles": ['Artifact', 'Disabler', 'Instrument'],
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Dismantle": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.Dismantle",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle dismantle.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Dismantler} dismantled {ROLE_Artifact} by using {ROLE_Instrument} from {ROLE_Components} in {ROLE_Place}.",
            "valid roles": ['Artifact', 'Components', 'Dismantler', 'Instrument', 'Place'],
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Unspecified": {
            "event type": "ArtifactExistence.DamageDestroyDisableDismantle.Unspecified",
            "keywords": [],
            "event description": "The event is related to artifact existence damage destroy disable dismantle.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_DamagerDestroyer} damaged or destroyed {ROLE_Artifact} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ['Artifact', 'DamagerDestroyer', 'Instrument', 'Place'],
        },
        "ArtifactExistence.ManufactureAssemble.Unspecified": {
            "event type": "ArtifactExistence.ManufactureAssemble.Unspecified",
            "keywords": [],
            "event description": "The event is related to artifact existence manufacture assemble.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_ManufacturerAssembler} manufactured or assembled or produced {ROLE_Artifact} from {ROLE_Components} in {ROLE_Place}.",
            "valid roles": ['Artifact', 'Components', 'ManufacturerAssembler', 'Place'],
        },
        "Cognitive.IdentifyCategorize.Unspecified": {
            "event type": "Cognitive.IdentifyCategorize.Unspecified",
            "keywords": [],
            "event description": "The event is related to cognitive identify categorize.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Identifier} identified {ROLE_IdentifiedObject} as {ROLE_IdentifiedRole} in {ROLE_Place}.",
            "valid roles": ['IdentifiedObject', 'IdentifiedRole', 'Identifier', 'Place'],
        },
        "Cognitive.Inspection.SensoryObserve": {
            "event type": "Cognitive.Inspection.SensoryObserve",
            "keywords": [],
            "event description": "The event is related to cognitive inspection sensory observe.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Observer} observed {ROLE_ObservedEntity} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ['Instrument', 'ObservedEntity', 'Observer', 'Place'],
        },
        "Cognitive.Research.Unspecified": {
            "event type": "Cognitive.Research.Unspecified",
            "keywords": [],
            "event description": "The event is related to cognitive research.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Researcher} researched {ROLE_Subject} in {ROLE_Place}.",
            "valid roles": ['Place', 'Researcher', 'Subject'],
        },
        "Cognitive.TeachingTrainingLearning.Unspecified": {
            "event type": "Cognitive.TeachingTrainingLearning.Unspecified",
            "keywords": [],
            "event description": "The event is related to cognitive teaching training learning.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_TeacherTrainer} taught or trained {ROLE_Learner}.",
            "valid roles": ['Learner', 'TeacherTrainer'],
        },
        "Conflict.Attack.DetonateExplode": {
            "event type": "Conflict.Attack.DetonateExplode",
            "keywords": [],
            "event description": "The event is related to conflict attack detonate explode.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} detonated or exploded {ROLE_ExplosiveDevice} by using {ROLE_Instrument} to attack {ROLE_Target} in {ROLE_Place}.",
            "valid roles": ['Attacker', 'ExplosiveDevice', 'Instrument', 'Place', 'Target'],
        },
        "Conflict.Attack.Unspecified": {
            "event type": "Conflict.Attack.Unspecified",
            "keywords": [],
            "event description": "The event is related to conflict attack.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Attacker} attacked {ROLE_Target} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ['Attacker', 'Instrument', 'Place', 'Target'],
        },
        "Conflict.Defeat.Unspecified": {
            "event type": "Conflict.Defeat.Unspecified",
            "keywords": [],
            "event description": "The event is related to conflict defeat.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Victor} defeated {ROLE_Defeated} in a conflict in {ROLE_Place}.",
            "valid roles": ['Defeated', 'Place', 'Victor'],
        },
        "Conflict.Demonstrate.DemonstrateWithViolence": {
            "event type": "Conflict.Demonstrate.DemonstrateWithViolence",
            "keywords": [],
            "event description": "The event is related to conflict demonstrate demonstrate with violence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Demonstrator} was in a demonstration involving violence with involvement of {ROLE_Regulator}.",
            "valid roles": ['Demonstrator', 'Regulator'],
        },
        "Conflict.Demonstrate.Unspecified": {
            "event type": "Conflict.Demonstrate.Unspecified",
            "keywords": [],
            "event description": "The event is related to conflict demonstrate.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Demonstrator} was in a demonstration for {ROLE_Topic} against {ROLE_Target}.",
            "valid roles": ['Demonstrator', 'Target', 'Topic'],
        },
        "Contact.Contact.Broadcast": {
            "event type": "Contact.Contact.Broadcast",
            "keywords": [],
            "event description": "The event is related to contact contact broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} broadcasted {ROLE_Recipient} about {ROLE_Topic} by using {ROLE_Instrument} in {ROLE_Place}.",
            "valid roles": ['Communicator', 'Instrument', 'Place', 'Recipient', 'Topic'],
        },
        "Contact.Contact.Correspondence": {
            "event type": "Contact.Contact.Correspondence",
            "keywords": [],
            "event description": "The event is related to contact contact correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Participant} contacted {ROLE_Participant} with correspondence about {ROLE_Topic} in {ROLE_Place}.",
            "valid roles": ['Participant', 'Place', 'Topic'],
        },
        "Contact.Contact.Meet": {
            "event type": "Contact.Contact.Meet",
            "keywords": [],
            "event description": "The event is related to contact contact meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Participant} contacted {ROLE_Participant} with meeting about {ROLE_Topic} in {ROLE_Place}.",
            "valid roles": ['Participant', 'Place', 'Topic'],
        },
        "Contact.Contact.Unspecified": {
            "event type": "Contact.Contact.Unspecified",
            "keywords": [],
            "event description": "The event is related to contact contact.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Participant} contacted {ROLE_Participant} about {ROLE_Topic} in {ROLE_Place}.",
            "valid roles": ['Participant', 'Place', 'Topic'],
        },
        "Contact.RequestCommand.Broadcast": {
            "event type": "Contact.RequestCommand.Broadcast",
            "keywords": [],
            "event description": "The event is related to contact request command broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} requested {ROLE_Recipient} for a broadcast.",
            "valid roles": ['Communicator', 'Recipient'],
        },
        "Contact.RequestCommand.Correspondence": {
            "event type": "Contact.RequestCommand.Correspondence",
            "keywords": [],
            "event description": "The event is related to contact request command correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} requested {ROLE_Recipient} for a correspondence about {ROLE_Topic}.",
            "valid roles": ['Communicator', 'Recipient', 'Topic'],
        },
        "Contact.RequestCommand.Meet": {
            "event type": "Contact.RequestCommand.Meet",
            "keywords": [],
            "event description": "The event is related to contact request command meet.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} requested {ROLE_Recipient} for a meeting.",
            "valid roles": ['Communicator', 'Recipient'],
        },
        "Contact.RequestCommand.Unspecified": {
            "event type": "Contact.RequestCommand.Unspecified",
            "keywords": [],
            "event description": "The event is related to contact request command.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} requested {ROLE_Recipient} in {ROLE_Place}.",
            "valid roles": ['Communicator', 'Place', 'Recipient'],
        },
        "Contact.ThreatenCoerce.Broadcast": {
            "event type": "Contact.ThreatenCoerce.Broadcast",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce broadcast.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} threatened or coerced {ROLE_Recipient} by a broadcast.",
            "valid roles": ['Communicator', 'Recipient'],
        },
        "Contact.ThreatenCoerce.Correspondence": {
            "event type": "Contact.ThreatenCoerce.Correspondence",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce correspondence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} threatened or coerced {ROLE_Recipient} by a correspondence.",
            "valid roles": ['Communicator', 'Recipient'],
        },
        "Contact.ThreatenCoerce.Unspecified": {
            "event type": "Contact.ThreatenCoerce.Unspecified",
            "keywords": [],
            "event description": "The event is related to contact threaten coerce.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Communicator} threatened or coerced {ROLE_Recipient}.",
            "valid roles": ['Communicator', 'Recipient'],
        },
        "Control.ImpedeInterfereWith.Unspecified": {
            "event type": "Control.ImpedeInterfereWith.Unspecified",
            "keywords": [],
            "event description": "The event is related to control impede interfere with.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Impeder} impeded or interfered in {ROLE_Place}.",
            "valid roles": ['Impeder', 'Place'],
        },
        "Disaster.Crash.Unspecified": {
            "event type": "Disaster.Crash.Unspecified",
            "keywords": [],
            "event description": "The event is related to disaster crash.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Vehicle} crashed into {ROLE_CrashObject} in {ROLE_Place}.",
            "valid roles": ['CrashObject', 'Place', 'Vehicle'],
        },
        "Disaster.DiseaseOutbreak.Unspecified": {
            "event type": "Disaster.DiseaseOutbreak.Unspecified",
            "keywords": [],
            "event description": "The event is related to disaster disease outbreak.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Disease broke out among {ROLE_Victim} in {ROLE_Place}.",
            "valid roles": ['Place', 'Victim'],
        },
        "GenericCrime.GenericCrime.GenericCrime": {
            "event type": "GenericCrime.GenericCrime.GenericCrime",
            "keywords": [],
            "event description": "The event is related to generic crime generic crime generic crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Perpetrator} committed a crime against {ROLE_Victim} in {ROLE_Place}.",
            "valid roles": ['Perpetrator', 'Place', 'Victim'],
        },
        "Justice.Acquit.Unspecified": {
            "event type": "Justice.Acquit.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice acquit.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Judge court acquitted {ROLE_Defendant} of a crime.",
            "valid roles": ['Defendant'],
        },
        "Justice.ArrestJailDetain.Unspecified": {
            "event type": "Justice.ArrestJailDetain.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice arrest jail detain.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Jailer} arrested or jailed {ROLE_Detainee} for a crime in {ROLE_Place}.",
            "valid roles": ['Detainee', 'Jailer', 'Place'],
        },
        "Justice.ChargeIndict.Unspecified": {
            "event type": "Justice.ChargeIndict.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice charge indict.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Prosecutor} charged or indicted {ROLE_Defendant} before {ROLE_JudgeCourt} for a crime in {ROLE_Place}.",
            "valid roles": ['Defendant', 'JudgeCourt', 'Place', 'Prosecutor'],
        },
        "Justice.Convict.Unspecified": {
            "event type": "Justice.Convict.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice convict.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_JudgeCourt} convicted {ROLE_Defendant} of a crime.",
            "valid roles": ['Defendant', 'JudgeCourt'],
        },
        "Justice.InvestigateCrime.Unspecified": {
            "event type": "Justice.InvestigateCrime.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice investigate crime.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Investigator} investigated {ROLE_Defendant} for a crime and {ROLE_Observer} observed {ROLE_ObservedEntity} in {ROLE_Place}.",
            "valid roles": ['Defendant', 'Investigator', 'ObservedEntity', 'Observer', 'Place'],
        },
        "Justice.ReleaseParole.Unspecified": {
            "event type": "Justice.ReleaseParole.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice release parole.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_JudgeCourt} released or paroled {ROLE_Defendant} from a crime.",
            "valid roles": ['Defendant', 'JudgeCourt'],
        },
        "Justice.Sentence.Unspecified": {
            "event type": "Justice.Sentence.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice sentence.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_JudgeCourt} sentenced {ROLE_Defendant} for a crime to sentence in {ROLE_Place}.",
            "valid roles": ['Defendant', 'JudgeCourt', 'Place'],
        },
        "Justice.TrialHearing.Unspecified": {
            "event type": "Justice.TrialHearing.Unspecified",
            "keywords": [],
            "event description": "The event is related to justice trial hearing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Prosecutor} tried {ROLE_Defendant} before {ROLE_JudgeCourt} for a crime in {ROLE_Place}.",
            "valid roles": ['Defendant', 'JudgeCourt', 'Place', 'Prosecutor'],
        },
        "Life.Die.Unspecified": {
            "event type": "Life.Die.Unspecified",
            "keywords": [],
            "event description": "The event is related to life die.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Victim} was killed by {ROLE_Killer} in {ROLE_Place}.",
            "valid roles": ['Killer', 'Place', 'Victim'],
        },
        "Life.Infect.Unspecified": {
            "event type": "Life.Infect.Unspecified",
            "keywords": [],
            "event description": "The event is related to life infect.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Victim} was infected.",
            "valid roles": ['Victim'],
        },
        "Life.Injure.Unspecified": {
            "event type": "Life.Injure.Unspecified",
            "keywords": [],
            "event description": "The event is related to life injure.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Victim} was injured regarding {ROLE_BodyPart} by {ROLE_Injurer} by using {ROLE_Instrument}.",
            "valid roles": ['BodyPart', 'Injurer', 'Instrument', 'Victim'],
        },
        "Medical.Intervention.Unspecified": {
            "event type": "Medical.Intervention.Unspecified",
            "keywords": [],
            "event description": "The event is related to medical intervention.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Treater} treated {ROLE_Patient} in {ROLE_Place}.",
            "valid roles": ['Patient', 'Place', 'Treater'],
        },
        "Movement.Transportation.Evacuation": {
            "event type": "Movement.Transportation.Evacuation",
            "keywords": [],
            "event description": "The event is related to movement transportation evacuation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Transporter} evacuated with {ROLE_PassengerArtifact} from {ROLE_Origin} to {ROLE_Destination}.",
            "valid roles": ['Destination', 'Origin', 'PassengerArtifact', 'Transporter'],
        },
        "Movement.Transportation.IllegalTransportation": {
            "event type": "Movement.Transportation.IllegalTransportation",
            "keywords": [],
            "event description": "The event is related to movement transportation illegal transportation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Transporter} illegally transported {ROLE_PassengerArtifact} with {ROLE_Vehicle} to {ROLE_Destination}.",
            "valid roles": ['Destination', 'PassengerArtifact', 'Transporter', 'Vehicle'],
        },
        "Movement.Transportation.PreventPassage": {
            "event type": "Movement.Transportation.PreventPassage",
            "keywords": [],
            "event description": "The event is related to movement transportation prevent passage.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Preventer} prevented {ROLE_Transporter} from entering {ROLE_Destination} from {ROLE_Origin} to transport {ROLE_PassengerArtifact} with {ROLE_Vehicle}.",
            "valid roles": ['Destination', 'Origin', 'PassengerArtifact', 'Preventer', 'Transporter', 'Vehicle'],
        },
        "Movement.Transportation.Unspecified": {
            "event type": "Movement.Transportation.Unspecified",
            "keywords": [],
            "event description": "The event is related to movement transportation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Transporter} transported {ROLE_PassengerArtifact} with {ROLE_Vehicle} from {ROLE_Origin} to {ROLE_Destination}.",
            "valid roles": ['Destination', 'Origin', 'PassengerArtifact', 'Transporter', 'Vehicle'],
        },
        "Personnel.EndPosition.Unspecified": {
            "event type": "Personnel.EndPosition.Unspecified",
            "keywords": [],
            "event description": "The event is related to personnel end position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Employee} stopped working at {ROLE_PlaceOfEmployment}.",
            "valid roles": ['Employee', 'PlaceOfEmployment'],
        },
        "Personnel.StartPosition.Unspecified": {
            "event type": "Personnel.StartPosition.Unspecified",
            "keywords": [],
            "event description": "The event is related to personnel start position.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Employee} started working in {ROLE_Position} at {ROLE_PlaceOfEmployment} in {ROLE_Place}.",
            "valid roles": ['Employee', 'Place', 'PlaceOfEmployment', 'Position'],
        },
        "Transaction.Donation.Unspecified": {
            "event type": "Transaction.Donation.Unspecified",
            "keywords": [],
            "event description": "The event is related to transaction donation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} gave {ROLE_ArtifactMoney} to {ROLE_Recipient}.",
            "valid roles": ['ArtifactMoney', 'Giver', 'Recipient'],
        },
        "Transaction.ExchangeBuySell.Unspecified": {
            "event type": "Transaction.ExchangeBuySell.Unspecified",
            "keywords": [],
            "event description": "The event is related to transaction exchange buy sell.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "{ROLE_Giver} sold or traded {ROLE_AcquiredEntity} to {ROLE_Recipient} in exchange for {ROLE_PaymentBarter}.",
            "valid roles": ['AcquiredEntity', 'Giver', 'PaymentBarter', 'Recipient'],
        },
    },
    "fewevent": {
        "Business.Collaboration": {
            "event description": "The event is related to business collaboration.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Declare-Bankruptcy": {
            "event description": "The event is related to business declare bankruptcy.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Employment": {
            "event description": "The event is related to business employment.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Employment-Tenure": {
            "event description": "The event is related to business employment tenure.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.End-Org": {
            "event description": "The event is related to business end organization.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Financing": {
            "event description": "The event is related to business financing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Investment": {
            "event description": "The event is related to business investment.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Layoff": {
            "event description": "The event is related to business layoff.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Merge-Org": {
            "event description": "The event is related to business merge organization.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Sponsorship": {
            "event description": "The event is related to business sponsorship.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Start-Org": {
            "event description": "The event is related to business start organization.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Business.Start-Subsidiary": {
            "event description": "The event is related to business start subsidiary.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Conflict.Attack": {
            "event description": "The event is related to conflict attack.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Conflict.Demonstrate": {
            "event description": "The event is related to conflict demonstrate.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Conflict.Riot": {
            "event description": "The event is related to conflict riot.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Conflict.Self-Immolation": {
            "event description": "The event is related to conflict self immolation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Broadcast": {
            "event description": "The event is related to contact broadcast.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Contact": {
            "event description": "The event is related to contact contact.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Correspondence": {
            "event description": "The event is related to contact correspondence.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.E-Mail": {
            "event description": "The event is related to contact e mail.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Letter-Communication": {
            "event description": "The event is related to contact letter communication.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Meet": {
            "event description": "The event is related to contact meet.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Online-Chat": {
            "event description": "The event is related to contact online chat.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Phone-Write": {
            "event description": "The event is related to contact phone write.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Video-Chat": {
            "event description": "The event is related to contact video chat.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Contact.Voice-Mail": {
            "event description": "The event is related to contact voice mail.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Education.Education": {
            "event description": "The event is related to education education.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Film.Dubbing-Performance": {
            "event description": "The event is related to film dubbing performance.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Film.Film-Crew-Gig": {
            "event description": "The event is related to film film crew gig.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Film.Film-Distribution": {
            "event description": "The event is related to film film distribution.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Film.Film-Festival": {
            "event description": "The event is related to film film festival.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Film.Film-Production": {
            "event description": "The event is related to film film production.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Acquit": {
            "event description": "The event is related to justice acquit.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Appeal": {
            "event description": "The event is related to justice appeal.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Arrest-Jail": {
            "event description": "The event is related to justice arrest jail.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Charge-Indict": {
            "event description": "The event is related to justice charge indict.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Convict": {
            "event description": "The event is related to justice convict.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Execute": {
            "event description": "The event is related to justice execute.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Extradite": {
            "event description": "The event is related to justice extradite.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Fine": {
            "event description": "The event is related to justice fine.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Pardon": {
            "event description": "The event is related to justice pardon.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Release-Parole": {
            "event description": "The event is related to justice release parole.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Sentence": {
            "event description": "The event is related to justice sentence.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Sue": {
            "event description": "The event is related to justice sue.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Justice.Trial-Hearing": {
            "event description": "The event is related to justice trial hearing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Abortion": {
            "event description": "The event is related to life abortion.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Be-Born": {
            "event description": "The event is related to life be born.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Die": {
            "event description": "The event is related to life die.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Divorce": {
            "event description": "The event is related to life divorce.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Homesick": {
            "event description": "The event is related to life homesick.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Injure": {
            "event description": "The event is related to life injure.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Marry": {
            "event description": "The event is related to life marry.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Pregnancy": {
            "event description": "The event is related to life pregnancy.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Sick": {
            "event description": "The event is related to life sick.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Life.Travel": {
            "event description": "The event is related to life travel.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Manufacture.Artifact": {
            "event description": "The event is related to manufacture artifact.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Manufacture.Lean-Manufacturing": {
            "event description": "The event is related to manufacture lean manufacturing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Military.Military-Command": {
            "event description": "The event is related to military military command.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Military.Military-Service": {
            "event description": "The event is related to military military service.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Military.Recruit-Training": {
            "event description": "The event is related to military recruit training.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Military.Recruitment": {
            "event description": "The event is related to military recruitment.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Movement.Driving": {
            "event description": "The event is related to movement driving.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Movement.Parking": {
            "event description": "The event is related to movement parking.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Movement.Transport": {
            "event description": "The event is related to movement transport.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Movement.Transport-Artifact": {
            "event description": "The event is related to movement transport artifact.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Movement.Transportperson": {
            "event description": "The event is related to movement transportperson.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Music.Compose": {
            "event description": "The event is related to music compose.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Music.Dance": {
            "event description": "The event is related to music dance.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Music.Group-Membership": {
            "event description": "The event is related to music group membership.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Music.Sing": {
            "event description": "The event is related to music sing.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Music.Track-Contribution": {
            "event description": "The event is related to music track contribution.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Olympics.Closing-Ceremony": {
            "event description": "The event is related to olympics closing ceremony.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Olympics.Olympic-Athlete-Affiliation": {
            "event description": "The event is related to olympics olympic athlete affiliation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Olympics.Olympic-Medal-Honor": {
            "event description": "The event is related to olympics olympic medal honor.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Olympics.Opening-Ceremony": {
            "event description": "The event is related to olympics opening ceremony.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Organization.Division-Of-Labour": {
            "event description": "The event is related to organization division of labour.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Organization.Leadership": {
            "event description": "The event is related to organization leadership.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Organization.Org-Communication": {
            "event description": "The event is related to organization org communication.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Organization.Organization-Board-Membership": {
            "event description": "The event is related to organization organization board membership.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "People.Appointment": {
            "event description": "The event is related to people appointment.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "People.Place-Lived": {
            "event description": "The event is related to people place lived.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Personnel.Demotion": {
            "event description": "The event is related to personnel demotion.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Personnel.Elect": {
            "event description": "The event is related to personnel elect.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Personnel.End-Position": {
            "event description": "The event is related to personnel end position.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Personnel.Nominate": {
            "event description": "The event is related to personnel nominate.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Personnel.Performance-Appraisal": {
            "event description": "The event is related to personnel performance appraisal.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Personnel.Promotion": {
            "event description": "The event is related to personnel promotion.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Personnel.Resignation": {
            "event description": "The event is related to personnel resignation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Personnel.Start-Position": {
            "event description": "The event is related to personnel start position.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Projects.Project-Participation": {
            "event description": "The event is related to projects project participation.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Sports.Fair-Play": {
            "event description": "The event is related to sports fair play.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Sports.Sports-Team-Roster": {
            "event description": "The event is related to sports sports team roster.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Sports.Sports-Team-Season-Record": {
            "event description": "The event is related to sports sports team season record.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Sports.Tournament": {
            "event description": "The event is related to sports tournament.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Transaction.Deposit": {
            "event description": "The event is related to transaction deposit.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Transaction.Money-Laundering": {
            "event description": "The event is related to transaction money laundering.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Transaction.Transaction": {
            "event description": "The event is related to transaction transaction.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Transaction.Transfer-Money": {
            "event description": "The event is related to transaction transfer money.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Transaction.Transfer-Ownership": {
            "event description": "The event is related to transaction transfer ownership.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
        "Wine.Grape-Variety-Composition": {
            "event description": "The event is related to wine grape variety composition.", 
            "ED template": "Event trigger is {Trigger}.", 
            "valid roles": [], 
        },
    },
    "phee": {
        "Adverse_event": {
            "event type": "Adverse_event",
            "keywords": [],
            "event description": "The event is related to adverse event.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Combination Drug {ROLE_Combination_Drug} Effect {ROLE_Effect} Subject {ROLE_Subject} Subject Age {ROLE_Subject_Age} Subject Disorder {ROLE_Subject_Disorder} Subject Gender {ROLE_Subject_Gender} Subject Population {ROLE_Subject_Population} Subject Race {ROLE_Subject_Race} Treatment {ROLE_Treatment} Treatment Disorder {ROLE_Treatment_Disorder} Treatment Dosage {ROLE_Treatment_Dosage} Treatment Drug {ROLE_Treatment_Drug} Treatment Duration {ROLE_Treatment_Duration} Treatment Frequency {ROLE_Treatment_Freq} Treatment Route {ROLE_Treatment_Route} Treatment Time Elapsed {ROLE_Treatment_Time_elapsed}.",
            "valid roles": [
                "Combination_Drug",
                "Effect",
                "Subject",
                "Subject_Age",
                "Subject_Disorder",
                "Subject_Gender",
                "Subject_Population",
                "Subject_Race",
                "Treatment",
                "Treatment_Disorder",
                "Treatment_Dosage",
                "Treatment_Drug",
                "Treatment_Duration",
                "Treatment_Freq",
                "Treatment_Route",
                "Treatment_Time_elapsed",
            ],
        },
        "Potential_therapeutic_event": {
            "event type": "Potential_therapeutic_event",
            "keywords": [],
            "event description": "The event is related to potential therapeutic event.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Combination Drug {ROLE_Combination_Drug} Effect {ROLE_Effect} Subject {ROLE_Subject} Subject Age {ROLE_Subject_Age} Subject Disorder {ROLE_Subject_Disorder} Subject Gender {ROLE_Subject_Gender} Subject Population {ROLE_Subject_Population} Subject Race {ROLE_Subject_Race} Treatment {ROLE_Treatment} Treatment Disorder {ROLE_Treatment_Disorder} Treatment Dosage {ROLE_Treatment_Dosage} Treatment Drug {ROLE_Treatment_Drug} Treatment Duration {ROLE_Treatment_Duration} Treatment Frequency {ROLE_Treatment_Freq} Treatment Route {ROLE_Treatment_Route} Treatment Time Elapsed {ROLE_Treatment_Time_elapsed}.",
            "valid roles": [
                "Combination_Drug",
                "Effect",
                "Subject",
                "Subject_Age",
                "Subject_Disorder",
                "Subject_Gender",
                "Subject_Population",
                "Subject_Race",
                "Treatment",
                "Treatment_Disorder",
                "Treatment_Dosage",
                "Treatment_Drug",
                "Treatment_Duration",
                "Treatment_Freq",
                "Treatment_Route",
                "Treatment_Time_elapsed",
            ],
        },
    },
    "casie": {
        "Attack:Databreach": {
            "event type": "Attack:Databreach",
            "keywords": [],
            "event description": "The event is related to attack databreach.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Attack Pattern {ROLE_Attack-Pattern} Attacker {ROLE_Attacker} Compromised Data {ROLE_Compromised-Data} Damage Amount {ROLE_Damage-Amount} Number of Data {ROLE_Number-of-Data} Number of Victim {ROLE_Number-of-Victim} Place {ROLE_Place} Purpose {ROLE_Purpose} Time {ROLE_Time} Tool {ROLE_Tool} Victim {ROLE_Victim}",
            "valid roles": ['Attack-Pattern', 'Attacker', 'Compromised-Data', 'Damage-Amount', 'Number-of-Data', 'Number-of-Victim', 'Place', 'Purpose', 'Time', 'Tool', 'Victim'],
        },
        "Attack:Phishing": {
            "event type": "Attack:Phishing",
            "keywords": [],
            "event description": "The event is related to attack phishing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Attack Pattern {ROLE_Attack-Pattern} Attacker {ROLE_Attacker} Damage Amount {ROLE_Damage-Amount} Place {ROLE_Place} Purpose {ROLE_Purpose} Time {ROLE_Time} Tool {ROLE_Tool} Trusted Entity {ROLE_Trusted-Entity} Victim {ROLE_Victim}",
            "valid roles": ['Attack-Pattern', 'Attacker', 'Damage-Amount', 'Place', 'Purpose', 'Time', 'Tool', 'Trusted-Entity', 'Victim'],
        },
        "Attack:Ransom": {
            "event type": "Attack:Ransom",
            "keywords": [],
            "event description": "The event is related to attack ransom.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Attack Pattern {ROLE_Attack-Pattern} Attacker {ROLE_Attacker} Damage Amount {ROLE_Damage-Amount} Payment Method {ROLE_Payment-Method} Place {ROLE_Place} Price {ROLE_Price} Time {ROLE_Time} Tool {ROLE_Tool} Victim {ROLE_Victim}",
            "valid roles": ['Attack-Pattern', 'Attacker', 'Damage-Amount', 'Payment-Method', 'Place', 'Price', 'Time', 'Tool', 'Victim'],
        },
        "Vulnerability-related:DiscoverVulnerability": {
            "event type": "Vulnerability-related:DiscoverVulnerability",
            "keywords": [],
            "event description": "The event is related to vulnerability-related discover vulnerability.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CVE {ROLE_CVE} Capabilities {ROLE_Capabilities} Discoverer {ROLE_Discoverer} Supported Platform {ROLE_Supported_Platform} Time {ROLE_Time} Vulnerability {ROLE_Vulnerability} Vulnerable System {ROLE_Vulnerable_System} Vulnerable System Owner {ROLE_Vulnerable_System_Owner} Vulnerable System Version {ROLE_Vulnerable_System_Version}",
            "valid roles": ['CVE', 'Capabilities', 'Discoverer', 'Supported_Platform', 'Time', 'Vulnerability', 'Vulnerable_System', 'Vulnerable_System_Owner', 'Vulnerable_System_Version'],
        },
        "Vulnerability-related:PatchVulnerability": {
            "event type": "Vulnerability-related:PatchVulnerability",
            "keywords": [],
            "event description": "The event is related to vulnerability-related patch vulnerability.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CVE {ROLE_CVE} Issues Addressed {ROLE_Issues-Addressed} Patch {ROLE_Patch} Patch Number {ROLE_Patch-Number} Releaser {ROLE_Releaser} Supported Platform {ROLE_Supported_Platform} Time {ROLE_Time} Vulnerability {ROLE_Vulnerability} Vulnerable System {ROLE_Vulnerable_System} Vulnerable System Version {ROLE_Vulnerable_System_Version}",
            "valid roles": ['CVE', 'Issues-Addressed', 'Patch', 'Patch-Number', 'Releaser', 'Supported_Platform', 'Time', 'Vulnerability', 'Vulnerable_System', 'Vulnerable_System_Version'],
        },
    },
    "mlee": {
        "Acetylation": {
            "event type": "Acetylation",
            "keywords": [],
            "event description": "The event is related to acetylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Binding": {
            "event type": "Binding",
            "keywords": [],
            "event description": "The event is related to binding.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2}",
            "valid roles": ['Site', 'Theme', 'Theme2'],
        },
        "Blood_vessel_development": {
            "event type": "Blood_vessel_development",
            "keywords": [],
            "event description": "The event is related to blood vessel development.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "At Loc {ROLE_AtLoc} From Loc {ROLE_FromLoc} Theme {ROLE_Theme}",
            "valid roles": ['AtLoc', 'FromLoc', 'Theme'],
        },
        "Breakdown": {
            "event type": "Breakdown",
            "keywords": [],
            "event description": "The event is related to breakdown.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Catabolism": {
            "event type": "Catabolism",
            "keywords": [],
            "event description": "The event is related to catabolism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Cell_division": {
            "event type": "Cell_division",
            "keywords": [],
            "event description": "The event is related to cell division.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Cell_proliferation": {
            "event type": "Cell_proliferation",
            "keywords": [],
            "event description": "The event is related to cell proliferation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "DNA_methylation": {
            "event type": "DNA_methylation",
            "keywords": [],
            "event description": "The event is related to dna methylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['Site', 'Theme'],
        },
        "Death": {
            "event type": "Death",
            "keywords": [],
            "event description": "The event is related to death.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Dephosphorylation": {
            "event type": "Dephosphorylation",
            "keywords": [],
            "event description": "The event is related to dephosphorylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['Site', 'Theme'],
        },
        "Development": {
            "event type": "Development",
            "keywords": [],
            "event description": "The event is related to development.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Dissociation": {
            "event type": "Dissociation",
            "keywords": [],
            "event description": "The event is related to dissociation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Gene_expression": {
            "event type": "Gene_expression",
            "keywords": [],
            "event description": "The event is related to gene expression.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Growth": {
            "event type": "Growth",
            "keywords": [],
            "event description": "The event is related to growth.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Localization": {
            "event type": "Localization",
            "keywords": [],
            "event description": "The event is related to localization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "At Loc {ROLE_AtLoc} From Loc {ROLE_FromLoc} Theme {ROLE_Theme} To Loc {ROLE_ToLoc}",
            "valid roles": ['AtLoc', 'FromLoc', 'Theme', 'ToLoc'],
        },
        "Metabolism": {
            "event type": "Metabolism",
            "keywords": [],
            "event description": "The event is related to metabolism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Negative_regulation": {
            "event type": "Negative_regulation",
            "keywords": [],
            "event description": "The event is related to negative regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme'],
        },
        "Pathway": {
            "event type": "Pathway",
            "keywords": [],
            "event description": "The event is related to pathway.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Participant {ROLE_Participant} Participant 2 {ROLE_Participant2} Participant 3 {ROLE_Participant3} Participant 4 {ROLE_Participant4}",
            "valid roles": ['Participant', 'Participant2', 'Participant3', 'Participant4'],
        },
        "Phosphorylation": {
            "event type": "Phosphorylation",
            "keywords": [],
            "event description": "The event is related to phosphorylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['Site', 'Theme'],
        },
        "Planned_process": {
            "event type": "Planned_process",
            "keywords": [],
            "event description": "The event is related to planned process.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Instrument {ROLE_Instrument} Instrument 2 {ROLE_Instrument2} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2}",
            "valid roles": ['Instrument', 'Instrument2', 'Theme', 'Theme2'],
        },
        "Positive_regulation": {
            "event type": "Positive_regulation",
            "keywords": [],
            "event description": "The event is related to positive regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme', 'Theme2'],
        },
        "Protein_processing": {
            "event type": "Protein_processing",
            "keywords": [],
            "event description": "The event is related to protein processing.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Regulation": {
            "event type": "Regulation",
            "keywords": [],
            "event description": "The event is related to regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme'],
        },
        "Remodeling": {
            "event type": "Remodeling",
            "keywords": [],
            "event description": "The event is related to remodeling.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Reproduction": {
            "event type": "Reproduction",
            "keywords": [],
            "event description": "The event is related to reproduction.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Synthesis": {
            "event type": "Synthesis",
            "keywords": [],
            "event description": "The event is related to synthesis.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Transcription": {
            "event type": "Transcription",
            "keywords": [],
            "event description": "The event is related to transcription.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Translation": {
            "event type": "Translation",
            "keywords": [],
            "event description": "The event is related to translation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Ubiquitination": {
            "event type": "Ubiquitination",
            "keywords": [],
            "event description": "The event is related to ubiquitination.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
    },
    "genia2011": {
        "Binding": {
            "event type": "Binding",
            "keywords": [],
            "event description": "The event is related to binding.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Site 2 {ROLE_Site2} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2} Theme 3 {ROLE_Theme3} Theme 4 {ROLE_Theme4}",
            "valid roles": ['Site', 'Site2', 'Theme', 'Theme2', 'Theme3', 'Theme4'],
        },
        "Gene_expression": {
            "event type": "Gene_expression",
            "keywords": [],
            "event description": "The event is related to gene expression.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Localization": {
            "event type": "Localization",
            "keywords": [],
            "event description": "The event is related to localization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "At Loc {ROLE_AtLoc} Theme {ROLE_Theme} To Loc {ROLE_ToLoc}",
            "valid roles": ['AtLoc', 'Theme', 'ToLoc'],
        },
        "Negative_regulation": {
            "event type": "Negative_regulation",
            "keywords": [],
            "event description": "The event is related to negative regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme'],
        },
        "Phosphorylation": {
            "event type": "Phosphorylation",
            "keywords": [],
            "event description": "The event is related to phosphorylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['Site', 'Theme'],
        },
        "Positive_regulation": {
            "event type": "Positive_regulation",
            "keywords": [],
            "event description": "The event is related to positive regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme'],
        },
        "Protein_catabolism": {
            "event type": "Protein_catabolism",
            "keywords": [],
            "event description": "The event is related to protein catabolism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Regulation": {
            "event type": "Regulation",
            "keywords": [],
            "event description": "The event is related to regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme'],
        },
        "Transcription": {
            "event type": "Transcription",
            "keywords": [],
            "event description": "The event is related to transcription.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
    },
    "genia2013": {
        "Acetylation": {
            "event type": "Acetylation",
            "keywords": [],
            "event description": "The event is related to acetylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['Site', 'Theme'],
        },
        "Binding": {
            "event type": "Binding",
            "keywords": [],
            "event description": "The event is related to binding.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Site {ROLE_Site} Site 2 {ROLE_Site2} Theme {ROLE_Theme} Theme 2 {ROLE_Theme2}",
            "valid roles": ['Site', 'Site2', 'Theme', 'Theme2'],
        },
        "Deacetylation": {
            "event type": "Deacetylation",
            "keywords": [],
            "event description": "The event is related to deacetylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['Cause', 'Site', 'Theme'],
        },
        "Gene_expression": {
            "event type": "Gene_expression",
            "keywords": [],
            "event description": "The event is related to gene expression.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Localization": {
            "event type": "Localization",
            "keywords": [],
            "event description": "The event is related to localization.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme} To Loc {ROLE_ToLoc}",
            "valid roles": ['Theme', 'ToLoc'],
        },
        "Negative_regulation": {
            "event type": "Negative_regulation",
            "keywords": [],
            "event description": "The event is related to negative regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme'],
        },
        "Phosphorylation": {
            "event type": "Phosphorylation",
            "keywords": [],
            "event description": "The event is related to phosphorylation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['Cause', 'Site', 'Theme'],
        },
        "Positive_regulation": {
            "event type": "Positive_regulation",
            "keywords": [],
            "event description": "The event is related to positive regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme'],
        },
        "Protein_catabolism": {
            "event type": "Protein_catabolism",
            "keywords": [],
            "event description": "The event is related to protein catabolism.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Protein_modification": {
            "event type": "Protein_modification",
            "keywords": [],
            "event description": "The event is related to protein modification.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Regulation": {
            "event type": "Regulation",
            "keywords": [],
            "event description": "The event is related to regulation.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "CSite {ROLE_CSite} Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['CSite', 'Cause', 'Site', 'Theme'],
        },
        "Transcription": {
            "event type": "Transcription",
            "keywords": [],
            "event description": "The event is related to transcription.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Theme {ROLE_Theme}",
            "valid roles": ['Theme'],
        },
        "Ubiquitination": {
            "event type": "Ubiquitination",
            "keywords": [],
            "event description": "The event is related to ubiquitination.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "Cause {ROLE_Cause} Site {ROLE_Site} Theme {ROLE_Theme}",
            "valid roles": ['Cause', 'Site', 'Theme'],
        },
    },
    "speed": {
        "control": {
            "event type": "Control",
            "keywords": [],
            "event description": "The event is related to control.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "cure": {
            "event type": "Cure",
            "keywords": [],
            "event description": "The event is related to cure.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "death": {
            "event type": "Death",
            "keywords": [],
            "event description": "The event is related to death.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "infect": {
            "event type": "Infect",
            "keywords": [],
            "event description": "The event is related to infect.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "prevent": {
            "event type": "Prevent",
            "keywords": [],
            "event description": "The event is related to prevent.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "spread": {
            "event type": "Spread",
            "keywords": [],
            "event description": "The event is related to spread.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
        "symptom": {
            "event type": "Symptom",
            "keywords": [],
            "event description": "The event is related to symptom.",
            "ED template": "Event trigger is {Trigger}.",
            "valid roles": [],
        },
    },
    "muc4": {
        "Dummy": {
            "event type": "Dummy",
            "keywords": [],
            "event description": "This is a event.",
            "ED template": "Event trigger is {Trigger}.",
            "EAE template": "PerpInd {ROLE_PerpInd} PerpOrg {ROLE_PerpOrg} Target {ROLE_Target} Victim {ROLE_Victim} Weapon {ROLE_Weapon}",
            "valid roles": ['PerpInd', 'PerpOrg', 'Target', 'Victim', 'Weapon'],
        },
    },
}

ROLE_PH_MAP = {
    "ace05-en": {
        'ROLE_Person': 'somebody',
        'ROLE_Entity': 'some people or some organization',
        'ROLE_Defendant': 'somebody',
        'ROLE_Prosecutor': 'some other',
        'ROLE_Plaintiff': 'some other',
        'ROLE_Buyer': 'someone',
        'ROLE_Artifact': 'something',
        'ROLE_Seller': 'some seller',
        'ROLE_Destination': 'somewhere',
        'ROLE_Origin': 'some place',
        'ROLE_Vehicle': 'some vehicle',
        'ROLE_Agent': 'somebody or some organization',
        'ROLE_Attacker': 'some attacker',
        'ROLE_Target': 'some facility, someone, or some organization',
        'ROLE_Victim': 'some victim',
        'ROLE_Instrument': 'some way',
        'ROLE_Giver': 'someone',
        'ROLE_Recipient': 'some other',
        'ROLE_Org': 'some organization',
        'ROLE_Place': 'somewhere',
        'ROLE_Adjudicator': 'some adjudicator',
    },
    "richere-en": {
        'ROLE_Person': 'somebody',
        'ROLE_Entity': 'some people or some organization',
        'ROLE_Defendant': 'somebody',
        'ROLE_Prosecutor': 'some other',
        'ROLE_Plaintiff': 'some other',
        'ROLE_Buyer': 'someone',
        'ROLE_Artifact': 'something',
        'ROLE_Seller': 'some seller',
        'ROLE_Destination': 'somewhere',
        'ROLE_Origin': 'some place',
        'ROLE_Vehicle': 'some vehicle',
        'ROLE_Agent': 'somebody or some organization',
        'ROLE_Attacker': 'some attacker',
        'ROLE_Target': 'some facility, someone, or some organization',
        'ROLE_Victim': 'some victim',
        'ROLE_Instrument': 'some way',
        'ROLE_Giver': 'someone',
        'ROLE_Recipient': 'some other',
        'ROLE_Org': 'some organization',
        'ROLE_Place': 'somewhere',
        'ROLE_Adjudicator': 'some adjudicator',
        'ROLE_Thing': 'something',
        'ROLE_Audience': 'some publicity',
    },
    "m2e2": {
        'ROLE_Person': 'somebody',
        'ROLE_Entity': 'some people or some organization',
        'ROLE_Artifact': 'something',
        'ROLE_Destination': 'somewhere',
        'ROLE_Origin': 'some place',
        'ROLE_Vehicle': 'some vehicle',
        'ROLE_Agent': 'somebody or some organization',
        'ROLE_Attacker': 'some attacker',
        'ROLE_Target': 'some facility, someone, or some organization',
        'ROLE_Victim': 'some victim',
        'ROLE_Instrument': 'some way',
        'ROLE_Giver': 'someone',
        'ROLE_Recipient': 'some other',
        'ROLE_Place': 'somewhere',
        'ROLE_Police': 'some police',
    },
    "geneva": {
        "ROLE_Act": "some act",
        "ROLE_Action": "some action",
        "ROLE_Activity": "some activity",
        "ROLE_Actor": "some actor",
        "ROLE_Addressee": "some addressee",
        "ROLE_Affected": "some affected",
        "ROLE_Affliction": "some affliction",
        "ROLE_Agent": "some agent",
        "ROLE_Agreement": "some agreement",
        "ROLE_Area": "some area",
        "ROLE_Arguer": "some arguer",
        "ROLE_Arguer2": "some arguer2",
        "ROLE_Arguers": "some arguers",
        "ROLE_Assailant": "some assailant",
        "ROLE_Asset": "some asset",
        "ROLE_Attendees": "some attendees",
        "ROLE_Attribute": "some attribute",
        "ROLE_Author": "some author",
        "ROLE_Authorities": "some authorities",
        "ROLE_Avenger": "some avenger",
        "ROLE_Barrier": "some barrier",
        "ROLE_Behavior": "some behavior",
        "ROLE_Beneficiary": "some beneficiary",
        "ROLE_Benefited_party": "some benefited party",
        "ROLE_Body": "some body",
        "ROLE_Body_location": "some body location",
        "ROLE_Body_part": "some body part",
        "ROLE_Buyer": "some buyer",
        "ROLE_Carrier": "some carrier",
        "ROLE_Cause": "some cause",
        "ROLE_Charges": "some charges",
        "ROLE_Chosen": "some chosen",
        "ROLE_Circumstances": "some circumstances",
        "ROLE_Clothing": "some clothing",
        "ROLE_Cognizer": "some cognizer",
        "ROLE_Communicator": "some communicator",
        "ROLE_Competition": "some competition",
        "ROLE_Components": "some components",
        "ROLE_Configuration": "some configuration",
        "ROLE_Conqueror": "some conqueror",
        "ROLE_Container": "some container",
        "ROLE_Content": "some content",
        "ROLE_Contents": "some contents",
        "ROLE_Controlling_variable": "some controlling variable",
        "ROLE_Course": "some course",
        "ROLE_Created_entity": "some created entity",
        "ROLE_Creator": "some creator",
        "ROLE_Crime": "some crime",
        "ROLE_Culture": "some culture",
        "ROLE_Deceased": "some deceased",
        "ROLE_Decision": "some decision",
        "ROLE_Defender": "some defender",
        "ROLE_Dependent_variable": "some dependent variable",
        "ROLE_Destroyer": "some destroyer",
        "ROLE_Difference": "some difference",
        "ROLE_Dimension": "some dimension",
        "ROLE_Direction": "some direction",
        "ROLE_Distance": "some distance",
        "ROLE_Domain": "some domain",
        "ROLE_Donor": "some donor",
        "ROLE_Duration": "some duration",
        "ROLE_Earner": "some earner",
        "ROLE_Earnings": "some earnings",
        "ROLE_Effect": "some effect",
        "ROLE_Employee": "some employee",
        "ROLE_Employer": "some employer",
        "ROLE_Entity": "some entity",
        "ROLE_Evaluee": "some evaluee",
        "ROLE_Event": "some event",
        "ROLE_Evidence": "some evidence",
        "ROLE_Exchanger_1": "some exchanger 1",
        "ROLE_Exchanger_2": "some exchanger 2",
        "ROLE_Exchangers": "some exchangers",
        "ROLE_Experiencer": "some experiencer",
        "ROLE_Fact": "some fact",
        "ROLE_Factory": "some factory",
        "ROLE_Field": "some field",
        "ROLE_Figures": "some figures",
        "ROLE_Final_category": "some final category",
        "ROLE_Final_quality": "some final quality",
        "ROLE_Final_subevent": "some final subevent",
        "ROLE_Final_value": "some final value",
        "ROLE_Focal_entity": "some focal entity",
        "ROLE_Goal": "some goal",
        "ROLE_Goal_area": "some goal area",
        "ROLE_Goods": "some goods",
        "ROLE_Ground": "some ground",
        "ROLE_Group": "some group",
        "ROLE_Helper": "some helper",
        "ROLE_Hindrance": "some hindrance",
        "ROLE_Host": "some host",
        "ROLE_Imposed_purpose": "some imposed purpose",
        "ROLE_Incident": "some incident",
        "ROLE_Individuals": "some individuals",
        "ROLE_Information": "some information",
        "ROLE_Ingestibles": "some ingestibles",
        "ROLE_Ingestor": "some ingestor",
        "ROLE_Inherent_purpose": "some inherent purpose",
        "ROLE_Initial_category": "some initial category",
        "ROLE_Initial_size": "some initial size",
        "ROLE_Initial_subevent": "some initial subevent",
        "ROLE_Injured_party": "some injured party",
        "ROLE_Injury": "some injury",
        "ROLE_Inspector": "some inspector",
        "ROLE_Instrument": "some instrument",
        "ROLE_Intended_event": "some intended event",
        "ROLE_Interlocutors": "some interlocutors",
        "ROLE_Investigator": "some investigator",
        "ROLE_Issue": "some issue",
        "ROLE_Item": "some item",
        "ROLE_Killer": "some killer",
        "ROLE_Label": "some label",
        "ROLE_Location": "some location",
        "ROLE_Manipulator": "some manipulator",
        "ROLE_Manner": "some manner",
        "ROLE_Means": "some means",
        "ROLE_Medication": "some medication",
        "ROLE_Medium": "some medium",
        "ROLE_Member": "some member",
        "ROLE_Message": "some message",
        "ROLE_Money": "some money",
        "ROLE_New_leader": "some new leader",
        "ROLE_New_member": "some new member",
        "ROLE_Object": "some object",
        "ROLE_Occasion": "some occasion",
        "ROLE_Offender": "some offender",
        "ROLE_Offense": "some offense",
        "ROLE_Offerer": "some offerer",
        "ROLE_Old_leader": "some old leader",
        "ROLE_Old_order": "some old order",
        "ROLE_Part_1": "some part 1",
        "ROLE_Part_2": "some part 2",
        "ROLE_Participants": "some participants",
        "ROLE_Partners": "some partners",
        "ROLE_Parts": "some parts",
        "ROLE_Path": "some path",
        "ROLE_Patient": "some patient",
        "ROLE_Payer": "some payer",
        "ROLE_Perceiver_agentive": "some perceiver agentive",
        "ROLE_Perpetrator": "some perpetrator",
        "ROLE_Phenomenon": "some phenomenon",
        "ROLE_Place": "some place",
        "ROLE_Place_of_employment": "some place of employment",
        "ROLE_Position": "some position",
        "ROLE_Possibilities": "some possibilities",
        "ROLE_Potential_hindrance": "some potential hindrance",
        "ROLE_Problem": "some problem",
        "ROLE_Process": "some process",
        "ROLE_Producer": "some producer",
        "ROLE_Product": "some product",
        "ROLE_Project": "some project",
        "ROLE_Proposal": "some proposal",
        "ROLE_Proposed_action": "some proposed action",
        "ROLE_Protagonist": "some protagonist",
        "ROLE_Punishment": "some punishment",
        "ROLE_Purpose": "some purpose",
        "ROLE_Rate": "some rate",
        "ROLE_Ratifier": "some ratifier",
        "ROLE_Reason": "some reason",
        "ROLE_Recipient": "some recipient",
        "ROLE_Researcher": "some researcher",
        "ROLE_Resource": "some resource",
        "ROLE_Responding_entity": "some responding entity",
        "ROLE_Response": "some response",
        "ROLE_Result": "some result",
        "ROLE_Result_size": "some result size",
        "ROLE_Role": "some role",
        "ROLE_Selector": "some selector",
        "ROLE_Self_mover": "some self mover",
        "ROLE_Seller": "some seller",
        "ROLE_Sender": "some sender",
        "ROLE_Side_1": "some side 1",
        "ROLE_Side_2": "some side 2",
        "ROLE_Sides": "some sides",
        "ROLE_Signatory": "some signatory",
        "ROLE_Situation": "some situation",
        "ROLE_Skill": "some skill",
        "ROLE_Social_event": "some social event",
        "ROLE_Source": "some source",
        "ROLE_Speaker": "some speaker",
        "ROLE_Specified_entity": "some specified entity",
        "ROLE_Speed": "some speed",
        "ROLE_State": "some state",
        "ROLE_Student": "some student",
        "ROLE_Subject": "some subject",
        "ROLE_Supplier": "some supplier",
        "ROLE_Supported": "some supported",
        "ROLE_Supporter": "some supporter",
        "ROLE_Suspect": "some suspect",
        "ROLE_Task": "some task",
        "ROLE_Teacher": "some teacher",
        "ROLE_Terrorist": "some terrorist",
        "ROLE_Tested_property": "some tested property",
        "ROLE_Tester": "some tester",
        "ROLE_Text": "some text",
        "ROLE_Theme": "some theme",
        "ROLE_Theme_1": "some theme 1",
        "ROLE_Theme_2": "some theme 2",
        "ROLE_Themes": "some themes",
        "ROLE_Time": "some time",
        "ROLE_Topic": "some topic",
        "ROLE_Transferors": "some transferors",
        "ROLE_Traveler": "some traveler",
        "ROLE_Traveller": "some traveller",
        "ROLE_Treatment": "some treatment",
        "ROLE_Trigger": "some trigger",
        "ROLE_Type": "some type",
        "ROLE_Unconfirmed_content": "some unconfirmed content",
        "ROLE_Undertaking": "some undertaking",
        "ROLE_Undesirable_event": "some undesirable event",
        "ROLE_Unwanted_entity": "some unwanted entity",
        "ROLE_Useful_location": "some useful location",
        "ROLE_Value_1": "some value 1",
        "ROLE_Value_2": "some value 2",
        "ROLE_Vehicle": "some vehicle",
        "ROLE_Venue": "some venue",
        "ROLE_Victim": "some victim",
        "ROLE_Weapon": "some weapon",
        "ROLE_Wearer": "some wearer",
        "ROLE_Whole": "some whole",
    },
    "maven": {
    },
    "mee-en": {
    },
    "fewevent": {
    },
    "rams": {
        "ROLE_artifact": "some artifact",
        "ROLE_artifactmoney": "some artifact money",
        "ROLE_attacker": "some attacker",
        "ROLE_ballot": "some ballot",
        "ROLE_beneficiary": "some beneficiary",
        "ROLE_candidate": "some candidate",
        "ROLE_communicator": "some communicator",
        "ROLE_crashobject": "some crash object",
        "ROLE_crime": "some crime",
        "ROLE_damager": "some damager",
        "ROLE_damagerdestroyer": "some damager destroyer",
        "ROLE_deceased": "some deceased",
        "ROLE_defendant": "some defendant",
        "ROLE_demonstrator": "some demonstrator",
        "ROLE_destination": "some destination",
        "ROLE_destroyer": "some destroyer",
        "ROLE_detainee": "some detainee",
        "ROLE_driverpassenger": "some driver passenger",
        "ROLE_employee": "some employee",
        "ROLE_executioner": "some executioner",
        "ROLE_extraditer": "some extraditer",
        "ROLE_fireexplosionobject": "some fire explosion object",
        "ROLE_founder": "some founder",
        "ROLE_giver": "some giver",
        "ROLE_governmentbody": "some government body",
        "ROLE_gpe": "some gpe",
        "ROLE_granter": "some granter",
        "ROLE_hidingplace": "some hiding place",
        "ROLE_injurer": "some injurer",
        "ROLE_inspectedentity": "some inspected entity",
        "ROLE_inspector": "some inspector",
        "ROLE_instrument": "some instrument",
        "ROLE_investigator": "some investigator",
        "ROLE_jailer": "some jailer",
        "ROLE_judgecourt": "some judge court",
        "ROLE_killer": "some killer",
        "ROLE_law": "some law",
        "ROLE_manufacturer": "some manufacturer",
        "ROLE_money": "some money",
        "ROLE_monitor": "some monitor",
        "ROLE_monitoredentity": "some monitored entity",
        "ROLE_observedentity": "some observed entity",
        "ROLE_observer": "some observer",
        "ROLE_origin": "some origin",
        "ROLE_otherparticipant": "some other participant",
        "ROLE_participant": "some participant",
        "ROLE_passenger": "some passenger",
        "ROLE_place": "some place",
        "ROLE_placeofemployment": "some place of employment",
        "ROLE_preventer": "some preventer",
        "ROLE_prosecutor": "some prosecutor",
        "ROLE_recipient": "some recipient",
        "ROLE_rejecternullifier": "some rejecter nullifier",
        "ROLE_result": "some result",
        "ROLE_retreater": "some retreater",
        "ROLE_spy": "some spy",
        "ROLE_surrenderer": "some surrenderer",
        "ROLE_target": "some target",
        "ROLE_territoryorfacility": "some territoryor facility",
        "ROLE_transporter": "some transporter",
        "ROLE_vehicle": "some vehicle",
        "ROLE_victim": "some victim",
        "ROLE_violator": "some violator",
        "ROLE_voter": "some voter",
        "ROLE_yielder": "some yielder",  
    },
    "wikievents": {
        'ROLE_AcquiredEntity': 'some acquired entity',
        'ROLE_Artifact': 'some artifact',
        'ROLE_ArtifactMoney': 'some artifact money',
        'ROLE_Attacker': 'some attacker',
        'ROLE_BodyPart': 'some body part',
        'ROLE_Communicator': 'some communicator',
        'ROLE_Components': 'some components',
        'ROLE_CrashObject': 'some crash object',
        'ROLE_Damager': 'some damager',
        'ROLE_DamagerDestroyer': 'some damager destroyer',
        'ROLE_Defeated': 'some defeated',
        'ROLE_Defendant': 'some defendant',
        'ROLE_Demonstrator': 'some demonstrator',
        'ROLE_Destination': 'some destination',
        'ROLE_Destroyer': 'some destroyer',
        'ROLE_Detainee': 'some detainee',
        'ROLE_Disabler': 'some disabler',
        'ROLE_Dismantler': 'some dismantler',
        'ROLE_Employee': 'some employee',
        'ROLE_ExplosiveDevice': 'some explosive device',
        'ROLE_Giver': 'some giver',
        'ROLE_IdentifiedObject': 'some identified object',
        'ROLE_IdentifiedRole': 'some identified role',
        'ROLE_Identifier': 'some identifier',
        'ROLE_Impeder': 'some impeder',
        'ROLE_Injurer': 'some injurer',
        'ROLE_Instrument': 'some instrument',
        'ROLE_Investigator': 'some investigator',
        'ROLE_Jailer': 'some jailer',
        'ROLE_JudgeCourt': 'some judge court',
        'ROLE_Killer': 'some killer',
        'ROLE_Learner': 'some learner',
        'ROLE_ManufacturerAssembler': 'some manufacturer assembler',
        'ROLE_ObservedEntity': 'some observed entity',
        'ROLE_Observer': 'some observer',
        'ROLE_Origin': 'some origin',
        'ROLE_Participant': 'some participant',
        'ROLE_PassengerArtifact': 'some passenger artifact',
        'ROLE_Patient': 'some patient',
        'ROLE_PaymentBarter': 'some payment barter',
        'ROLE_Perpetrator': 'some perpetrator',
        'ROLE_Place': 'some place',
        'ROLE_PlaceOfEmployment': 'some place of employment',
        'ROLE_Position': 'some position',
        'ROLE_Preventer': 'some preventer',
        'ROLE_Prosecutor': 'some prosecutor',
        'ROLE_Recipient': 'some recipient',
        'ROLE_Regulator': 'some regulator',
        'ROLE_Researcher': 'some researcher',
        'ROLE_Subject': 'some subject',
        'ROLE_Target': 'some target',
        'ROLE_TeacherTrainer': 'some teacher trainer',
        'ROLE_Topic': 'some topic',
        'ROLE_Transporter': 'some transporter',
        'ROLE_Treater': 'some treater',
        'ROLE_Vehicle': 'some vehicle',
        'ROLE_Victim': 'some victim',
        'ROLE_Victor': 'some victor',
    },
    "phee": {
        "ROLE_Combination_Drug": "some combination drug",
        "ROLE_Effect": "some effect",
        "ROLE_Subject": "some subject",
        "ROLE_Subject_Age": "some subject age",
        "ROLE_Subject_Disorder": "some subject disorder",
        "ROLE_Subject_Gender": "some subject gender",
        "ROLE_Subject_Population": "some subject population",
        "ROLE_Subject_Race": "some subject race",
        "ROLE_Treatment": "some treatment",
        "ROLE_Treatment_Disorder": "some treatment disorder",
        "ROLE_Treatment_Dosage": "some treatment dosage",
        "ROLE_Treatment_Drug": "some treatment drug",
        "ROLE_Treatment_Duration": "some treatment duration",
        "ROLE_Treatment_Freq": "some treatment frequency",
        "ROLE_Treatment_Route": "some treatment route",
        "ROLE_Treatment_Time_elapsed": "some treatment time elapsed",
    },
    "casie": {
        "ROLE_Attack-Pattern": "some attack pattern",
        "ROLE_Attacker": "some attacker",
        "ROLE_CVE": "some cve",
        "ROLE_Capabilities": "some capabilities",
        "ROLE_Compromised-Data": "some compromised data",
        "ROLE_Damage-Amount": "some damage amount",
        "ROLE_Discoverer": "some discoverer",
        "ROLE_Issues-Addressed": "some issues addressed",
        "ROLE_Number-of-Data": "some number of data",
        "ROLE_Number-of-Victim": "some number of victim",
        "ROLE_Patch": "some patch",
        "ROLE_Patch-Number": "some patch number",
        "ROLE_Payment-Method": "some payment method",
        "ROLE_Place": "some place",
        "ROLE_Price": "some price",
        "ROLE_Purpose": "some purpose",
        "ROLE_Releaser": "some releaser",
        "ROLE_Supported_Platform": "some supported platform",
        "ROLE_Time": "some time",
        "ROLE_Tool": "some tool",
        "ROLE_Trusted-Entity": "some trusted entity",
        "ROLE_Victim": "some victim",
        "ROLE_Vulnerability": "some vulnerability",
        "ROLE_Vulnerable_System": "some vulnerable system",
        "ROLE_Vulnerable_System_Owner": "some vulnerable system owner",
        "ROLE_Vulnerable_System_Version": "some vulnerable system version",
    },
    "mlee": {
        "ROLE_AtLoc": "some at loc",
        "ROLE_CSite": "some csite",
        "ROLE_Cause": "some cause",
        "ROLE_FromLoc": "some from loc",
        "ROLE_Instrument": "some instrument",
        "ROLE_Instrument2": "some instrument 2",
        "ROLE_Participant": "some participant",
        "ROLE_Participant2": "some participant 2",
        "ROLE_Participant3": "some participant 3",
        "ROLE_Participant4": "some participant 4",
        "ROLE_Site": "some site",
        "ROLE_Theme": "some theme",
        "ROLE_Theme2": "some theme 2",
        "ROLE_ToLoc": "some to loc",
    },
    "genia2011": {
        "ROLE_AtLoc": "some at loc",
        "ROLE_CSite": "some csite",
        "ROLE_Cause": "some cause",
        "ROLE_Site": "some site",
        "ROLE_Site2": "some site 2",
        "ROLE_Theme": "some theme",
        "ROLE_Theme2": "some theme 2",
        "ROLE_Theme3": "some theme 3",
        "ROLE_Theme4": "some theme 4",
        "ROLE_ToLoc": "some to loc",

    },
    "genia2013": {
        "ROLE_CSite": "some csite",
        "ROLE_Cause": "some cause",
        "ROLE_Site": "some site",
        "ROLE_Site2": "some site 2",
        "ROLE_Theme": "some theme",
        "ROLE_Theme2": "some theme 2",
        "ROLE_ToLoc": "some to loc",
    },
    "speed": {
    },
    "muc4": {
        "ROLE_PerpInd": "some person",
        "ROLE_PerpOrg": "some organization", 
        "ROLE_Target": "some target",
        "ROLE_Victim": "some victim", 
        "ROLE_Weapon": "some weapon",
    }, 
}