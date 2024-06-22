from typing import List
from persistence.milvus_manager import MilvusManager
from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    text: str

@app.post("/api/v1/{subject}/browse/")
def get_questions(subject: str, query: Query):
    milvus_manager = MilvusManager(collection_name=subject, metric_type="COSINE")
    browse_results = milvus_manager.search_collection(query.text)
    print(browse_results)
    return {"results": browse_results}
