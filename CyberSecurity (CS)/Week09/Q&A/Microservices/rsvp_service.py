from flask import Flask, jsonify, request

app = Flask(__name__)

rsvps = {}

@app.route('/rsvps', methods=['GET'])
def get_rsvps():
    return jsonify(rsvps)

@app.route('/rsvp', methods=['POST'])
def add_rsvp():
    data = request.json
    event_id = data["event_id"]
    if event_id not in rsvps:
        rsvps[event_id] = []
    rsvps[event_id].append({"user": data["user"], "response": data["response"]})
    return jsonify({"message": "RSVP Added"}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5002)
