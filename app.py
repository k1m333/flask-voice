from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/book", methods=["POST"])
def book_appointment():
    data = request.json or {}
    params = data.get("message", {}).get("functionCall", {}).get("parameters", {})
    
    print(f"📅 Booking: {params}")
    
    # TODO: Add Google Calendar logic here
    
    return jsonify({
        "result": f"I've booked your {params.get('service')} for {params.get('requested_time')}."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)