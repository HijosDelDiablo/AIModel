from langchain_ollama import OllamaLLM

def main():
    llm = OllamaLLM(model="mistral", base_url="http://localhost:11434")
    question = "What is the capital of France?"
    response = llm.invoke(question)
    print("Response:", response)

if __name__ == "__main__":
    main()