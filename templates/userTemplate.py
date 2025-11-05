from langchain_core.prompts import PromptTemplate

def create_user_template(question: str, knowledge_base: str) -> PromptTemplate:
    userTemplate = PromptTemplate(
    input_variables=["question", "knowledge_base"],
    template="""Eres un modelo que ayuda a usuario a responder preguntas
    sencillas con limitaciones del:\n\n{question}\n\n
    Con la siguiente información:\n\n{knowledge_base}, si no sabes la respuesta,
    di "No lo sé". """,
    )
    return userTemplate

def user_chain(llm, question: str, knowledge_base: str) -> any:
    prompt = create_user_template(question, knowledge_base)
    chain = prompt | llm
    response = chain.invoke({"question": question, "knowledge_base": knowledge_base})
    return response