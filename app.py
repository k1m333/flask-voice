from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse, Stream

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    
    # Start the Media Stream
    start = Start()
    stream = Stream(url="wss://auto-ai-receptionist-websocket.onrender.com")
    start.append(stream)
    resp.append(start)
    
    # Add a message to confirm the stream is starting
    resp.say("Media stream started.")
    
    return Response(str(resp), mimetype="text/xml")

@app.route("/")
def home():
    return "Flask Route A is running. Use /voice for Twilio webhook."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)