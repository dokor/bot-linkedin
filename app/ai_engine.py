import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_post(text):
    prompt = f"Résume ce post LinkedIn en 2 phrases maximum :\n\n{text}\n\nRésumé :"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def generate_comments(summary):
    prompt = f"Génère 3 commentaires professionnels et engageants pour un post LinkedIn qui dit :\n\n\"{summary}\""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().split("\n")
