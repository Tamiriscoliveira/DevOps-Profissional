from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    msg = request.form.get("Body")
    resp = MessagingResponse()
    resp.message(f"Olá! Recebi a sua mensagem: {msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

