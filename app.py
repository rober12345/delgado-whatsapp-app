import json
from flask import Flask, request, render_template
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Environment variables
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
                content_sid="HX077c6287218dcb0c30b7fd515a20368b",  # Your approved template SID
                content_variables=json.dumps({
                    "1": order_number,
                    "2": delivery_date,
                    "3": delivery_time
                })
            )
            return render_template("index.html", success=True)
        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")
