from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse, Stream

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    stream = Stream(url="wss://echo.websocket.org")
    resp.append(stream)
    return Response(str(resp), mimetype="text/xml")

@app.route("/")
def home():
    return "Flask Route A is running. Use /voice for Twilio webhook."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)