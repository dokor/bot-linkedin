from celery import Celery
from linkedin_scraper import get_linkedin_feed
from ai_engine import summarize_post, generate_comments
from slack_bot import send_post_to_slack
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery("tasks", broker=REDIS_URL)


@celery_app.task
def summarize_and_suggest():
    posts = get_linkedin_feed()

    for post in posts:
        try:
            summary = summarize_post(post["text"])
            comments = generate_comments(summary)
            send_post_to_slack(post["url"], summary, comments)
        except Exception as e:
            print(f"Erreur sur post {post['url']}: {e}")
