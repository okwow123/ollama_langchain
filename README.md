this document let you know how to start the execute local llm using ollama and langchain



1.install ollama local

```bash
brew install ollama
ollama pull gpt:oss-20b
ollama --version
```


2.install package
```bash
pip install langchain-community
```

3.test local llm
```python
from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage

#ollma local model connection
llm = Ollama(model="gpt-oss:20b")

#execution
response = llm.invoke("hello? my name is masterMJ")
print(response)
```

4.results


<img width="721" height="132" alt="스크린샷 2026-04-14 오후 10 34 03" src="https://github.com/user-attachments/assets/c6eacd3f-8bad-4e9a-8855-390e5009a70c" />


5.using multiturn
what is multi-turn ? 

**A structure that remembers the previous conversation and continues the answer.**


**example**

```python
#from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

#ollma local model connection
llm = ChatOllama(model="gpt-oss:20b")

#execution
#response = llm.invoke("hello? my name is masterMJ")
#print(response)
messages = [
    SystemMessage("You are a counselor who helps users.")
]
while True:
    user_input = input("user : ") #input the client message

    if user_input == "exit":
        break
    messages.append(
        HumanMessage(user_input)
    )
    ai_response = llm.invoke(messages)

    messages.append(
        ai_response
    )

    print("AI : "+ai_response.content)
```


this code let you know how yo use memory history using multi-turn

**results**

<img width="1125" height="282" alt="스크린샷 2026-04-14 오후 10 47 43" src="https://github.com/user-attachments/assets/83b3d783-a856-4c25-9227-bbd3dd55314d" />


