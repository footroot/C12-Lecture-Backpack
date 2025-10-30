events = {}
rsvps = {}

def add_event(name, date, description):
    event_id = len(events) + 1
    events[event_id] = {"name": name, "date": date, "description": description}

def add_rsvp(event_id, user, response):
    if event_id not in rsvps:
        rsvps[event_id] = []
    rsvps[event_id].append({"user": user, "response": response})
