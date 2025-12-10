from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(docs, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = []
    for doc in docs:
        pieces = text_splitter.split_text(doc["text"])
        for p in pieces:
            chunks.append({
                "text": p,
                "metadata": doc["metadata"]
            })
    return chunks