from typing import List, Dict
from persistence.milvus_manager import MilvusManager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3001",
    "http://localhost:3000"
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

class QueryResponse(BaseModel):
    results: List[Dict]

@app.post("/api/v1/{subject}/browse/")
def get_questions(subject: str, query: Query) -> QueryResponse:
    milvus_manager = MilvusManager(collection_name=subject, metric_type="COSINE")
    browse_results = milvus_manager.search_collection(query.text)
    browse_results = QueryResponse(results=browse_results)
    return browse_results
