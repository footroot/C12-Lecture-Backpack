from flask import Flask, jsonify, request

app = Flask(__name__)

events = {}

@app.route('/events', methods=['GET', 'POST'])
def handle_events():
    if request.method == 'POST':
        event_id = len(events) + 1
        data = request.json
        events[event_id] = {"name": data["name"], "date": data["date"], "description": data["description"]}
        return jsonify({"message": "Event Created"}), 201
    return jsonify(events)

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    return jsonify(events.get(event_id, {}))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
