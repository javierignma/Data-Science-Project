from typing import List
from persistence.milvus_manager import MilvusManager
from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()

@app.get("/api/v1/{subject}/browse/{query}")
def get_questions(subject: str, query: str):
    milvus_manager = MilvusManager(collection_name=subject, metric_type="IP")
    browse_results = milvus_manager.search_collection(query)
    return {"results": browse_results}