
from flask import Flask, request, render_template
from twilio.rest import Client
import os

app = Flask(__name__)

# Load from environment variables
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        order_number = request.form["order_number"]
        whatsapp_number = request.form["whatsapp_number"]

        message_body = f"Your order with Delgado Ópticas (Order #{order_number}) is ready, please pick them up today! Thanks for your business."

        try:
            client.messages.create(
                body=message_body,
                from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
                to=f"whatsapp:{whatsapp_number}"
            )
            return render_template("index.html", success=True)
        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")
