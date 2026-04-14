from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage

#ollma local model connection
llm = Ollama(model="gpt-oss:20b")

#execution
response = llm.invoke("hello? my name is masterMJ")
print(response)