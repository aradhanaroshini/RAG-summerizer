from dataset import load_document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
BATCH_SIZE = 100
def fun(path):
    # Load document
    data = load_document(path)
    # Debug check
    print("Loaded Data:")
    print(data[:500])
    # Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    texts = text_splitter.create_documents([data])
    text_contents = [
        x.page_content.strip()
        for x in texts
        if x.page_content.strip()
    ]
    print("First Chunk:")
    print(text_contents[0])
    # Embeddings
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    embeddings = embedding_model.embed_documents(text_contents)
    # Persistent DB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    # Delete old collection if exists
    try:
        chroma_client.delete_collection("my_collection")
    except:
        pass
    collection = chroma_client.get_or_create_collection(
        name="my_collection"
    )
    # Batch insert
    for i in range(0, len(text_contents), BATCH_SIZE):
        batch = text_contents[i:i+BATCH_SIZE]
        batch_embeddings = embeddings[i:i+BATCH_SIZE]
        batch_ids = [
            str(j)
            for j in range(i, i + len(batch))
        ]
        collection.add(
            documents=batch,
            embeddings=batch_embeddings,
            ids=batch_ids
        )
    # Retrieve relevant chunks
    results = collection.query(
        query_texts=["main topics in the document"],
        n_results=10
    )
    context = "\n".join(results["documents"][0])
    print("Retrieved Context:")
    print(context[:1000])
    return context