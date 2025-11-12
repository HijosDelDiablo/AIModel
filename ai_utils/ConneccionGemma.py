# import neccesary ai

from langchain_ollama import OllamaLLM

# utils imports python
from dotenv import load_dotenv

# api imports python
import os

class ConnectionModelStandard:
    def __init__(self): # ollama 
        load_dotenv()
        self.username = os.getenv("MODEL_BASE")
        self.uri_base_model = os.getenv("URI_BASE_MODEL")
        self.llm = OllamaLLM(model=self.username, base_url=self.uri_base_model)

    def get_llm(self):
        return self.llm