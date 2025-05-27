# Slack Bot with Django

A Slack bot built with Django to respond to Slack events, such as replying to "hi" messages using the Slack Events API and Slack SDK.

---

## 🧰 Prerequisites

- Python 3.8 or later
- [Miniconda or Anaconda](https://docs.conda.io/en/latest/miniconda.html)
- Slack App with:
  - `SLACK_BOT_USER_TOKEN`
  - `SLACK_SIGNING_SECRET`

---

## ⚙️ Project Setup (Using Conda)

### 1. Clone the Repository
git clone https://github.com/your-username/slack-bot.git
cd slack-bot

### 2. Create and Activate Conda Environment
conda create -n slackbot python=3.10 -y
conda activate slackbot

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Create .env File
Create a .env file in the root directory and add your secrets:

SLACK_BOT_USER_TOKEN=xoxb-XXXXXXXXXXXXXXXXXXXX
SLACK_SIGNING_SECRET=your-signing-secret
⚠️ Make sure .env is listed in .gitignore to avoid pushing it to GitHub.

### 🚀 Running the Server
### 1. Apply Migrations
python manage.py migrate

### 2. Start the Django Development Server
python manage.py runserver
The server will be running at http://127.0.0.1:8000

### 🌐 Exposing Localhost for Slack (Optional for Local Testing)
Use ngrok to expose your local server:

ngrok http 8000
Copy the HTTPS URL provided and use it as the Request URL for your Slack Event Subscriptions.

### 📁 Project Structure
bash
Copy code
slack-bot/
├── Slack/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── events/
│   └── views.py
├── manage.py
├── requirements.txt
├── .env
└── .gitignore

### ✅ Features
Validates Slack requests using the signing secret

Responds to user messages like "hi"

Ignores messages from bots

Easily extensible for new Slack event types

### 🛡️ Security
Secrets are stored in a .env file (never commit this file)

GitHub push protection blocks accidental commits of API keys

Use python-decouple for secure config management







