from pymilvus import connections, CollectionSchema, Collection, FieldSchema, utility, DataType
from typing import List

class MilvusManager:
    collection: Collection = None

    def __init__(self, collection_name):
        self._connect_to_milvus()
        self.select_collection(collection_name)

    def _connect_to_milvus(self):
        try:
            connections.connect("default", host="localhost", port="19530")
            print("Connected to Milvus.")
        except Exception as e:
            print(f"Error trying to connecting to Milvus: {e}")

    def create_collection(self, name: str):
        if utility.has_collection(name):
            print(f"Collection '{name}' already exists.")
            return
        
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
            FieldSchema(name="plain_text", dtype=DataType.STRING)
        ]
        description = f"{name}'s collection."
        schema = CollectionSchema(fields, description)
        collection = Collection(name, schema)
        self.collection = collection
    
    def select_collection(self, name: str):
        if utility.has_collection(name):
            self.collection = Collection(name)
        else:
            print(f"Collection '{name}' does not exist.")
    
    def insert_data(self, embeddings: List[float], plain_text: str):
        data = [[], embeddings, plain_text]
        self.collection.insert(data)
        self.collection.flush()
    
    def delete_data(self, id_to_delete: int):
        self.collection.delete(expr=f"id == {id_to_delete}")
        self.collection.flush()
    
    def search_collection(self, query_embedding: List[float], top_k=3):
        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10}
        }
        results = self.collection.search(
            query_embedding, 
            "embedding", 
            search_params, 
            limit=top_k, 
            output_fields=["plain_text"]
        )

        retrieved_texts = []
        for result in results:
            retrieved_texts.append(result.plain_text)
        
        return retrieved_texts
