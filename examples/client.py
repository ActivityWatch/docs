#!/usr/bin/env python3
from time import sleep
from datetime import datetime, timedelta, timezone

from aw_core.models import Event
from aw_client import ActivityWatchClient

# We'll run with testing=True so we don't mess up any production instance.
# Make sure you've started aw-server with the `--testing` flag as well.
client = ActivityWatchClient("test-client", testing=True)

# Make the bucket_id unique for both the client and host
# The convention is to use client-name_hostname as bucket name,
# but if you have multiple buckets in one client you can add a
# suffix such as client-name-event-type or similar
bucket_id = "{}_{}".format("test-client-bucket", client.hostname)
# A short and descriptive event type name
# Will be used by visualizers (such as aw-webui) to detect what type and format the events are in
# Can for example be "currentwindow", "afkstatus", "ping" or "currentsong"
event_type = "dummydata"

# First we need a bucket to send events/heartbeats to.
# If the bucket already exists aw-server will simply return 304 NOT MODIFIED,
# so run this every time the clients starts up to verify that the bucket exists.
# If the client was unable to connect to aw-server or something failed
# during the creation of the bucket, an exception will be raised.
client.create_bucket(bucket_id, event_type="test")

# Asynchronous loop example
with client:
    # This context manager starts the queue dispatcher thread and stops it when done, always use it when setting queued=True.

    # Create a sample event to send as heartbeat
    heartbeat_data = {"label": "heartbeat"}
    now = datetime.now(timezone.utc)
    heartbeat_event = Event(timestamp=now, data=heartbeat_data)

    # Now we can send some events via heartbeats
    # This will send one heartbeat every second 5 times
    sleeptime = 1
    for i in range(5):
        # The duration between the heartbeats will be less than pulsetime, so they will get merged.
        # TODO: Make a section with an illustration on how heartbeats work and insert a link here
        print("Sending heartbeat {}".format(i))
        client.heartbeat(bucket_id, heartbeat_event, pulsetime=sleeptime+1, queued=True)

        # Sleep a second until next heartbeat
        sleep(sleeptime)

        # Update timestamp for next heartbeat
        heartbeat_event.timestamp = datetime.now(timezone.utc)

    # Give the dispatcher thread some time to complete sending the last events.
    # If we don't do this the events might possibly queue up and be sent the
    # next time the client starts instead.
    sleep(1)

# Synchronous example, insert a shutdown event
shutdown_data = {"label": "shutdown"}
shutdown_event = Event(timestamp=now, data=shutdown_data)
inserted_event = client.insert_event(bucket_id, shutdown_event)

# The event returned from insert_event has been assigned an id by aw-server
assert inserted_event.id is not None

# Fetch last 10 events from bucket
# Should be two events in order of newest to oldest
# - "shutdown" event with a duration of 0
# - "heartbeat" event with a duration of 5*sleeptime
events = client.get_events(bucket_id=bucket_id, limit=10)
print(events)

# Now lets clean up after us.
# You probably don't want this in your watchers though!
client.delete_bucket(bucket_id)

# If something doesn't work, run aw-server with --verbose to see why some request doesn't go through
# Good luck with writing your own watchers :-)
