import os
from loaders.load_generic import load_document
from chunkers.text_chunker import chunk_documents
from embeddings.embedder import embed_chunks
from pathlib import Path
import nltk

resources = [
    "punkt",
    "punkt_tab",
    "averaged_perceptron_tagger_eng"
]

for r in resources:
    try:
        # Different paths for punkt vs taggers
        path = f"tokenizers/{r}" if "punkt" in r else f"taggers/{r}"
        nltk.data.find(path)
    except LookupError:
        nltk.download(r) 

def ingest_folder(folder: str):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        print(f"Processing: {filename}")

        docs = load_document(path)

        chunks = chunk_documents(docs)

        embedded_chunks = embed_chunks(chunks)

        print(embedded_chunks)



    

if __name__ == "__main__":
    base_path = Path(__file__).resolve().parents[3] / "Documents"
    ingest_folder(base_path)
    # docs = ingest_folder(base_path)
    # print(f"Loaded {len(docs)} structured elements.")