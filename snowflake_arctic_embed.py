from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama

# 1. Load the PDF
# Place your 'document.pdf' in the same folder as this script
loader = PyPDFLoader("./genai.pmi.pdf")
docs = loader.load()

# 2. Split the PDF into chunks
# This is crucial for precise retrieval and staying within context limits
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(docs)

# 3. Initialize Embeddings
embeddings = OllamaEmbeddings(
    model="snowflake-arctic-embed:m",
)

# 4. Create Vector Store from the PDF chunks
vectorstore = DocArrayInMemorySearch.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()

# 5. Setup LLM and RAG Chain
llm = ChatOllama(model="llama3")

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

# 6. Ask a question about your PDF
print("\n--- PDF Chat Initialized ---")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    # Get the question from the terminal
    user_question = input("User > ")

    # Check if the user wants to quit
    if user_question.lower() in ["exit", "quit", "q"]:
        print("Exiting chat. Goodbye, Matthew!")
        break

    # Ensure the input isn't empty
    if not user_question.strip():
        continue

    # Process the question through the RAG chain
    print("Thinking...")
    try:
        response = chain.invoke(user_question)
        print(f"\nAI > {response.content}\n")
        print("-" * 30)
    except Exception as e:
        print(f"An error occurred: {e}")
# response = chain.invoke("What is the main conclusion of this document?")
# print(f"Response: {response.content}")