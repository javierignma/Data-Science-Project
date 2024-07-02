from typing import List
from persistence.milvus_manager import MilvusManager
from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3001", "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

class Query(BaseModel):
    text: str

@app.post("/api/v1/{subject}/browse/")
def get_questions(subject: str, query: Query):
    milvus_manager = MilvusManager(collection_name=subject, metric_type="COSINE")
    browse_results = milvus_manager.search_collection(query.text)
    print(browse_results)
    return {"results": browse_results}
