from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

BATCH_SIZE = 100

def embed_chunks(chunks):

    for chunk in chunks:
        chunk["embedding"] = None

    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i+BATCH_SIZE]
        texts = [c["text"] for c in batch]

        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=texts
        )
        
        for chunk, emb in zip(batch, response.data):
            chunk["embedding"] = emb.embedding
    
    return chunks