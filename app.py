
from flask import Flask, request, render_template
from twilio.rest import Client
from dotenv import load_dotenv
import os
import json

# Load environment variables (useful for local dev)
load_dotenv()

app = Flask(__name__)

# Use your Twilio credentials from environment (keep them secret!)
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        order_number = request.form["order_number"]
        whatsapp_number = request.form["whatsapp_number"]
        delivery_date = request.form["delivery_date"]
        delivery_time = request.form["delivery_time"]

        try:
            client.messages.create(
                from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
                to=f"whatsapp:{whatsapp_number}",
                content_sid="HXb2e40cf432b16672fe405c96af2ed4c1",  # Your approved template SID
                content_variables=json.dumps({
                    "1": delivery_date,
                    "2": delivery_time
                })
            )
            return render_template("index.html", success=True)
        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")
