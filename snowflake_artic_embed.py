from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama

# 1. Initialize Embeddings with the Arctic Model
# Note: Snowflake models perform best when queries are prefixed.
embeddings = OllamaEmbeddings(
    model="snowflake-arctic-embed:m"
)

# 2. Setup your "Knowledge Base" (The Documents)
data = [
    "The project deadline is October 15th, 2026.",
    "Agile methodology emphasizes iterative development and customer feedback.",
    "The budget for the SaaS marketing campaign is $50,000."
]
vectorstore = DocArrayInMemorySearch.from_texts(data, embeddings)
retriever = vectorstore.as_retriever()

# 3. Setup the LLM (for generating the final answer)
llm = ChatOllama(model="llama3")

# 4. Create the RAG Chain
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# 5. Execute
response = chain.invoke("When is the project due?")
print(f"Response: {response.content}")