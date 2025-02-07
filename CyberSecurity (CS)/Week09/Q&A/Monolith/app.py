from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

events = {} 
rsvps = {} 

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        event_id = len(events) + 1
        name = request.form['name']
        date = request.form['date']
        description = request.form['description']

        events[event_id] = {"name": name, "date": date, "description": description}
        return redirect(url_for('list_events'))

    return render_template("create_event.html")

@app.route('/events')
def list_events():
    return render_template("events.html", events=events, rsvps=rsvps)

@app.route('/rsvp/<int:event_id>', methods=['GET', 'POST'])
def rsvp(event_id):
    if event_id not in events:
        return "Event not found", 404

    if request.method == 'POST':
        user = request.form['user']
        response = request.form['response']

        if event_id not in rsvps:
            rsvps[event_id] = []

        rsvps[event_id].append({"user": user, "response": response})
        return redirect(url_for('list_events'))

    return render_template("rsvp.html", event=events[event_id], event_id=event_id, rsvps=rsvps)

if __name__ == "__main__":
    app.run(debug=True)
