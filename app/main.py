from fastapi import FastAPI
from celery_tasks import summarize_and_suggest

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI LinkedIn Bot is running"}

@app.post("/process-posts/")
def process_posts():
    summarize_and_suggest.delay()
    return {"status": "Processing started"}
