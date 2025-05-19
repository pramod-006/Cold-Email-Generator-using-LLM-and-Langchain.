import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
    # Convert dict or list to string
     if isinstance(skills, dict):
        query_text = f"Mandatory: {', '.join(skills.get('mandatory', []))}. Preferred: {', '.join(skills.get('preferred', []))}."
     elif isinstance(skills, list):
        query_text = ', '.join(skills)
     else:
        query_text = str(skills)

     results = self.collection.query(query_texts=[query_text], n_results=2)
     return results.get('metadatas', [])