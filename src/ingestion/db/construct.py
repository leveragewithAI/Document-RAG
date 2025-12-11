def flatten_metadata(metadata):
    return {
        "source": str(metadata.get("source", "")),
        "page_number": str(metadata.get("page_number", ""))
    }

def insert_into_pinecone(chunks, index, batch_size=50):
    to_upsert = []
    for idx, chunk in enumerate(chunks):
        chunk_id = f"{chunk['metadata']['source']}_{chunk['metadata'].get('page_number', idx)}"
        to_upsert.append({
            "id": chunk_id,
            "values": chunk["embedding"],
            "metadata": flatten_metadata(chunk["metadata"])
        })
    
    print(f"Upserting {len(to_upsert)} vectors...")

    for i in range(0, len(to_upsert), batch_size):
        batch = to_upsert[i:i + batch_size]
        print(f"Upserting batch {i // batch_size + 1} with {len(batch)} vectors...")
        index.upsert(vectors=batch)
