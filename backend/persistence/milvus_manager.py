from pymilvus import connections, CollectionSchema, Collection, FieldSchema
from typing import List

def connect_to_milvus():
    try:
        connections.connect("default", host="localhost", port="19530")
        print("Connected to Milvus.")
    except Exception as e:
        print(f"Error trying to connecting to Milvus: {e}")

def create_collection(name: str, fields: List[FieldSchema], description: str):
    schema = CollectionSchema(fields, description)
    collection = Collection(name, schema, consistency_level="Strong")
    return collection