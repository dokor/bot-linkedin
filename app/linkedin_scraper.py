from playwright.sync_api import sync_playwright
import os

LINKEDIN_URL = "https://www.linkedin.com/feed/"
COOKIE = os.getenv("LINKEDIN_COOKIE")

def get_linkedin_feed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Injection du cookie de session pour simuler une session authentifiée
        context.add_cookies([{
            "name": "li_at",
            "value": COOKIE,
            "domain": ".linkedin.com",
            "path": "/",
            "httpOnly": True,
            "secure": True,
            "sameSite": "None"
        }])

        page = context.new_page()
        page.goto(LINKEDIN_URL, timeout=60000)
        page.wait_for_timeout(5000)

        posts = page.locator("div.feed-shared-update-v2").all()

        extracted_posts = []
        for post in posts[:5]:  # Limite à 5 posts pour la démo
            try:
                content = post.inner_text()
                post_url = post.locator("a.app-aware-link").first.get_attribute("href")
                extracted_posts.append({
                    "text": content,
                    "url": post_url
                })
            except:
                continue

        browser.close()
        return extracted_posts
