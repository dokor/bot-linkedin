# 🤖 LinkedIn Comment Bot via Slack

Ce projet est un bot IA qui automatise la lecture de ton fil LinkedIn, génère des résumés de posts, propose des commentaires pertinents, et les envoie dans un canal Slack pour validation avant publication (optionnelle) sur LinkedIn.

---

## 🧠 Fonctionnalités

- 🔍 Scraping du feed LinkedIn (via Playwright)
- ✍️ Résumé des posts avec OpenAI
- 💬 Génération de commentaires professionnels et engageants
- 📲 Envoi automatique sur Slack avec validation par boutons
- 🧾 Traitement asynchrone avec Celery + Redis

---

## ⚙️ Stack technique

- Python 3.11
- FastAPI (API REST)
- Celery + Redis (orchestration)
- Slack SDK (interaction utilisateur)
- Playwright (scraping LinkedIn)
- OpenAI GPT-4 (NLP)
- Docker + Docker Compose

---

## 🚀 Lancement rapide

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/linkedin-comment-bot.git
cd linkedin-comment-bot
