import os
from loaders.load_generic import load_document
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
    all_docs = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        docs = load_document(path)
        all_docs.extend(docs)
    
    return all_docs

if __name__ == "__main__":
    base_path = Path(__file__).resolve().parents[3] / "Documents"
    docs = ingest_folder(base_path)
    print(f"Loaded {len(docs)} structured elements.")