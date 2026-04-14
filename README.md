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
