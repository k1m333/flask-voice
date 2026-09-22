from flask import Flask, Response, request, jsonify
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream

app = Flask(__name__)


# ===========================
# 1. Twilio Voice Webhook (Route A)
# ===========================
@app.route("/voice", methods=["POST"])
def voice():
    """
    Twilio webhook for incoming calls.
    Returns TwiML that connects the call to the WebSocket server.
    """
    resp = VoiceResponse()
    connect = Connect()
    stream = Stream(url="wss://auto-ai-receptionist-websocket.onrender.com")
    connect.append(stream)
    resp.append(connect)
    return Response(str(resp), mimetype="text/xml")


# ===========================
# 2. Health Check
# ===========================
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


# ===========================
# 4. Home Route
# ===========================
@app.route("/", methods=["GET"])
def home():
    return "Flask Voice Route A is running."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)