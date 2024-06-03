from pymilvus import connections, CollectionSchema, Collection, FieldSchema, utility, DataType
from services.embedding import get_embeddings, split_string
from typing import List

class MilvusManager:
    collection: Collection

    def __init__(self, collection_name):
        self._connect_to_milvus()
        self.create_collection(collection_name)

    def _connect_to_milvus(self):
        try:
            connections.connect("default", host="localhost", port="19530")
            print("Connected to Milvus.")
        except Exception as e:
            print(f"Error trying to connecting to Milvus: {e}")

    def create_collection(self, name: str) -> None:
        '''
        Creates a new collection using name parameter as collection's name and select it as current collection.
        If the name is already used, then select the collection with that name.
        '''

        if utility.has_collection(name):
            print(f"Collection '{name}' already exists.")
            self.select_collection(name)
            return
        
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
            FieldSchema(name="plain_text", dtype=DataType.VARCHAR, max_length=500),
            FieldSchema(name="doc_name", dtype=DataType.VARCHAR, max_length=100)
        ]
        description = f"{name}'s collection."
        schema = CollectionSchema(fields, description, auto_id=True)
        collection = Collection(name, schema)
        self.collection = collection

        index_params = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {
                "nlist": 128
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
    
    def insert_data(self, plain_text: str, doc_name: str) -> None:
        '''
        Insert a new document in the current collection.
        '''
        texts = split_string(plain_text)

        for text in texts:
            data = {
                "embedding": get_embeddings(text),
                "plain_text": text,
                "doc_name": doc_name
            }
            insertion_result = self.collection.insert(data)
            if insertion_result.insert_count:
                print("Row inserted.")
            else:
                print("Row could not be inserted.")
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
    
    def search_collection(self, query: str, doc_name: str,top_k=3) -> List[str]:
        '''
        Gives the top_k texts that are most related to the given query.
        '''
        query_embedding = get_embeddings(query)

        search_param = {
            "data": [query_embedding],
            "anns_field": "embedding",
            "param": {
                "metric_type": "L2",
                "params": {"nprobe": 10}
            },
            "limit": top_k,
            "expr": f'doc_name == "{doc_name}"',
            "output_fields": ["plain_text"]
        }

        results = self.collection.search(**search_param)

        retrieved_texts = []
        for result in results:
            for hit in result:
                retrieved_texts.append(hit.entity.get('plain_text'))
        
        return retrieved_texts
