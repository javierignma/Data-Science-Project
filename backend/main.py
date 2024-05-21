from fastapi import FastAPI

app = FastAPI()

@app.get(path='/')
def hello_world():
    return 'Hello World'