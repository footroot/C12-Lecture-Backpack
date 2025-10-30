import data

def create_event(name, date, description):
    # Process input
    data.add_event(name, date, description)

def get_all_events():
    return data.events

def get_all_rsvps():
    return data.rsvps

def get_event(event_id):
    return data.events.get(event_id, None)

def rsvp_event(event_id, user, response):
    data.add_rsvp(event_id, user, response)
