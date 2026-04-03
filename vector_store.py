import chromadb

client = chromadb.Client()

# try to load collection, otherwise create it
try:
    collection = client.get_collection("notes")
except:
    collection = client.create_collection("notes")


def store_chunks(chunks, embeddings):

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i]],
            ids=[str(i)],
            metadatas=[{"source": f"chunk {i}"}]
        )


def search_chunks(query_embedding):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results["documents"][0]
    sources = results["metadatas"][0]

    return docs, sources