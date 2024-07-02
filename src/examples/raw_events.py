#!/usr/bin/env python3
from aw_client import ActivityWatchClient
from aw_core.models import Event

client = ActivityWatchClient("test-client", testing=True)

# get the buckets
buckets = client.get_buckets()

bucket_id = "{}_{}".format("aw-watcher-window", client.client_hostname)

# fetches 1000 events from the bucket
events = client.get_events(bucket_id, limit=1000)

# sum the time spent on each app
time_spent = dict()
for event in events:
    app = event.data["app"]
    if app in time_spent:
        time_spent[app] += event.duration
    else:
        time_spent[app] = event.duration

print(time_spent)

# Rename app "Code" to "VS Code" in the events 
for event in events:
    if event.data["app"] == "Code":
        event.data["app"] = "VS Code"
        new_event = Event(timestamp=event.timestamp, duration=event.duration, data=event.data, id=event.id) # Reuses the same id
        client.insert_event(bucket_id, new_event) # replace the old event with the new one 
        
