import chromadb
import uuid  # Import the UUID module to generate unique IDs

def create_database():
  db = chromadb.Client()
  return db

def add_entry(db, title, content):
  collection = db.get_collection("entries")

  # Generate a unique ID using UUID
  unique_id = str(uuid.uuid4())

  document = {
    "title": title,
    "content": content,
    "id": unique_id  # Use the generated unique ID as a string
  }

  collection.upsert(document)

def get_entries(db):
  collection = db.get_collection("entries")

  return collection.select()

def main():
  db = create_database()

  db.create_collection("entries")

  title = input("Enter title: ")
  content = input("Enter content: ")

  add_entry(db, title, content)

  entries = get_entries(db)

  for entry in entries:
    print(entry)

if __name__ == "__main__":
  main()
