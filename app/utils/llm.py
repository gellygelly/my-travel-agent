from langchain.llms import Ollama

def get_llm():
    return Ollama(model="gpt-oss:20b")