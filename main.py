from langchain_ollama import OllamaLLM
from database.connectionMongo import get_database
from templates.userTemplate import user_chain
def main():
    db = get_database()
    
    llm = OllamaLLM(model="mistral", base_url="http://localhost:11434")
    userChainInstance = user_chain(llm, question="Cuantos usuarios hay en la base de datos?", knowledge_base="usercount: 1500")
    print("Ejecutando la cadena de usuario...")
    print(userChainInstance)

if __name__ == "__main__":
    main()