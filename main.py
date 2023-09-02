import chromadb

client = chromadb.Client()
collection = client.create_collection("yt_demo")

collection.add(
    documents=["This is a document about cat", "This is a document about car"],
    metadatas=[{"category": "animal"}, {"category": "vehicle"}],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["vehicle"],
    n_results=1
)
print(results)

import os

def read_files_from_folder(folder_path):
    file_data = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                content = file.read()
                file_data.append({"file_name": file_name, "content": content})

    return file_data

folder_path = "pets"
file_data = read_files_from_folder(folder_path)

documents = []
metadatas = []
ids = []

for index, data in enumerate(file_data):
    documents.append(data['content'])
    metadatas.append({'source': data['file_name']})
    ids.append(str(index + 1))

pet_collection = client.create_collection("pet_collection")

pet_collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)
