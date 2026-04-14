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
