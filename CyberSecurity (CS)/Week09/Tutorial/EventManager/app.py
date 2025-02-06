from flask import Flask, render_template, request, redirect, url_for
import service

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        description = request.form['description']
        service.create_event(name, date, description)
        return redirect(url_for('list_events'))
    return render_template("create_event.html")

@app.route('/events')
def list_events():
    events = service.get_all_events()
    rsvps = service.get_all_rsvps()
    return render_template('events.html', events=events, rsvps=rsvps)

@app.route('/rsvp/<int:event_id>', methods=['GET', 'POST'])
def rsvp(event_id):
    if request.method == 'POST':
        user = request.form['user']
        response = request.form['response']
        service.rsvp_event(event_id, user, response)
        return redirect(url_for('list_events'))
    event = service.get_event(event_id)
    return render_template("rsvp.html", event=event, event_id=event_id)


if __name__ == "__main__":
    app.run(debug=True)