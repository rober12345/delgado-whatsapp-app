
# Delgado Ópticas - WhatsApp Notification App

Send automated WhatsApp messages to customers when their order is ready.

## Environment Variables

- TWILIO_SID
- TWILIO_AUTH_TOKEN
- TWILIO_WHATSAPP_NUMBER (e.g., +14155238886)

## Run Locally

```bash
pip install -r requirements.txt
flask run
```

## Deploy to Render

- Add environment variables
- Add build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
