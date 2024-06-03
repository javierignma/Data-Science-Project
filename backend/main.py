from typing import List
from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()

@app.get("/api/v1/questions")
def get_questions(topic: str, num_questions: int = 5):
    questions = get_questions(topic, num_questions)
    return {"questions": questions}

@app.post("/api/v1/answer")
def send_answer(question: str = Form(...), answer: str = Form(...)):
    is_correct = send_answer(question, answer)
    return {"is_correct": is_correct}

@app.post("/api/v1/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    success = upload_file(file_path)
    return {"success": success}