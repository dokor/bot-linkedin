import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID", "#general")  # à adapter
slack_client = WebClient(token=SLACK_TOKEN)

def send_post_to_slack(post_url, summary, comments):
    blocks = [
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*Post LinkedIn:*\n<{post_url}>"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*Résumé:* {summary}"}},
        {"type": "divider"},
    ]

    for i, comment in enumerate(comments):
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"> {comment}"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Valider"},
                "value": comment,
                "action_id": f"approve_comment_{i}"
            }
        })

    try:
        slack_client.chat_postMessage(channel=CHANNEL_ID, blocks=blocks, text="Suggestions de commentaires LinkedIn")
    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}")
