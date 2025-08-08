from langchain.llms import Ollama

def get_llm():
    return Ollama(model="gpt-oss:20b")  # 또는 llama3 등