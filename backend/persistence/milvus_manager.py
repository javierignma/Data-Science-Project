from pymilvus import connections, CollectionSchema, Collection, FieldSchema, utility, DataType
from services.embedding import get_embeddings
from typing import List
from dotenv import load_dotenv
import os

class MilvusManager:
    collection: Collection
    metric_type: str

    def __init__(self, collection_name: str, metric_type: str):
        self._connect_to_milvus()
        self.metric_type = metric_type
        self.create_collection(collection_name, self.metric_type)

    def _connect_to_milvus(self):
        load_dotenv()
        try:
            URI = os.getenv("ZILLIZ_URI")
            TOKEN = os.getenv("ZILLIZ_TOKEN")
            connections.connect("default", uri=URI, token=TOKEN)
            print("Connected to Milvus.")
        except Exception as e:
            print(f"Error trying to connecting to Milvus: {e}")

    def create_collection(self, name: str, metric_type: str) -> None:
        '''
        Creates a new collection using name parameter as collection's name and select it as current collection.
        If the name is already used, then select the collection with that name.
        Metric types:
        - "L2"
        - "IP"
        - "JACCARD"
        '''

        if utility.has_collection(name):
            print(f"Collection '{name}' already exists.")
            self.select_collection(name)
            return
        
        fields = [
            FieldSchema(name="doc_name", dtype=DataType.VARCHAR, max_length=200, is_primary=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
            FieldSchema(name="link_ref", dtype=DataType.VARCHAR, max_length=500)
        ]
        description = f"{name}'s collection."
        schema = CollectionSchema(fields, description)
        collection = Collection(name, schema)
        self.collection = collection

        index_params = {
            "index_type": "IVF_FLAT",
            "metric_type": metric_type,
            "params": {
                "nlist": 4096
            }
        }
        collection.create_index(field_name='embedding', index_params=index_params)
        collection.load()
    
    def select_collection(self, name: str) -> None:
        '''
        Select a collection by its name.
        '''
        if utility.has_collection(name):
            self.collection = Collection(name)
        else:
            print(f"Collection '{name}' does not exist.")
    
    def insert_data(self, data: List[dict]) -> None:
        '''
        Insert new documents in the current collection.
        '''

        for row in data:
            row = {
                "doc_name": row["doc_name"],
                "embedding": get_embeddings(row["content"]),
                "link_ref": row["link_ref"]
            }
            insertion_result = self.collection.insert(row)
            if insertion_result.insert_count:
                print(f"{row["doc_name"]} inserted in {self.collection.name}.")
            else:
                print(f"{row["doc_name"]} could not be inserted in {self.collection.name}.")
            self.collection.flush()
            
        self.collection.load()
    
    def delete_data(self, doc_name: str):
        '''
        Delete all data associated with the document.
        '''
        self.collection.delete(expr=f'doc_name == "{doc_name}"')
        self.collection.flush()
    
    def delete_collection(self):
        '''
        Delete current collection.
        '''
        collection_name = self.collection.name
        self.collection.drop()
        print(f"Collection '{collection_name}' has been deleted.")
    
    def search_collection(self, query: str, top_k=30) -> List[dict]:
        '''
        Gives the top_k texts that are most related to the given query.
        '''
        query_embedding = get_embeddings(query)

        search_param = {
            "data": [query_embedding],
            "anns_field": "embedding",
            "param": {
                "metric_type": self.metric_type,
                "params": {"nprobe": 128}
            },
            "limit": top_k,
            "output_fields": ["doc_name", "link_ref"]
        }

        results = self.collection.search(**search_param)

        retrieved_texts = []
        for result in results:
            for hit in result:
                similarity_percentage = round((1 + hit.distance) / 2 * 100, 2)
                row = {
                    "doc_name": hit.entity.get('doc_name'),
                    "link_ref": hit.entity.get('link_ref'),
                    "similarity_percentage": similarity_percentage
                }
                retrieved_texts.append(row)
        
        return retrieved_texts
