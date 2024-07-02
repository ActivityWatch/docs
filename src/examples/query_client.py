#!/usr/bin/env python3

from datetime import datetime, timedelta, timezone

from aw_core.models import Event
from aw_client import ActivityWatchClient

# We'll run with testing=True so we don't mess up any production instance.
# Make sure you've started aw-server with the `--testing` flag as well.
client = ActivityWatchClient("test-client", testing=True)

now = datetime.now(timezone.utc)
start = now

query = "RETURN=0;"
res = client.query(query, "1970-01-01", "2100-01-01")
print(res) # Should print 0

bucket_id = "{}_{}".format("test-client-bucket", client.client_hostname)
event_type = "dummydata"
client.create_bucket(bucket_id, event_type="test")

def insert_events(label: str, count: int):
    global now
    events = []
    for i in range(count):
        e = Event(timestamp=now,
                   duration=timedelta(seconds=1),
                   data={"label": label})
        events.append(e)
        now = now + timedelta(seconds=1)
    client.insert_events(bucket_id, events)

insert_events("a", 5)

query = "RETURN = query_bucket('{}');".format(bucket_id)

res = client.query(query, "1970", "2100")
print(res) # Should print the last 5 events

res = client.query(query, start + timedelta(seconds=1), now - timedelta(seconds=2))
print(res) # Should print three events

insert_events("b", 10)

query = """
events = query_bucket('{}');
merged_events = merge_events_by_keys(events, 'label');
RETURN=merged_events;
""".format(bucket_id)
res = client.query(query, "1970", "2100")
# Should print two merged events
# Event "a" with a duration of 5s and event "b" with a duration of 10s
print(res)

client.delete_bucket(bucket_id)
