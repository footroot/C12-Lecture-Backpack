from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

EVENT_SERVICE_URL = "http://127.0.0.1:5001"
RSVP_SERVICE_URL = "http://127.0.0.1:5002"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        event_data = {
            "name": request.form['name'],
            "date": request.form['date'],
            "description": request.form['description']
        }
        requests.post(f"{EVENT_SERVICE_URL}/events", json=event_data)
        return redirect(url_for('list_events'))
    return render_template("create_event.html")

@app.route('/events')
def list_events():
    events = requests.get(f"{EVENT_SERVICE_URL}/events").json()
    rsvps = requests.get(f"{RSVP_SERVICE_URL}/rsvps").json()
    return render_template("events.html", events=events, rsvps=rsvps)

@app.route('/rsvp/<int:event_id>', methods=['GET', 'POST'])
def rsvp(event_id):
    if request.method == 'POST':
        rsvp_data = {
            "user": request.form['user'],
            "response": request.form['response'],
            "event_id": event_id
        }
        requests.post(f"{RSVP_SERVICE_URL}/rsvp", json=rsvp_data)
        return redirect(url_for('list_events'))

    event = requests.get(f"{EVENT_SERVICE_URL}/events/{event_id}").json()
    rsvps = requests.get(f"{RSVP_SERVICE_URL}/rsvps").json()
    return render_template("rsvp.html", event=event, event_id=event_id, rsvps=rsvps)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
