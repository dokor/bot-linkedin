from fastapi import FastAPI
import os
from celery_tasks import summarize_and_suggest, summarize_and_suggest_sync

app = FastAPI()
USE_CELERY = os.getenv("USE_CELERY", "False") == "True"

@app.get("/")
def root():
    return {"message": "AI LinkedIn Bot is running"}

@app.post("/process-posts/")
def process_posts():
    if USE_CELERY:
        summarize_and_suggest.delay()
        return {"status": "Traitement lancé avec Celery"}
    else:
        summarize_and_suggest_sync()
        return {"status": "Traitement effectué en mode synchrone"}