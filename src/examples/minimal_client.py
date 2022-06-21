#!/usr/bin/env python3

from datetime import datetime, timezone

from aw_core.models import Event
from aw_client import ActivityWatchClient

# We'll run with testing=True so we don't mess up any production instance.
# Make sure you've started aw-server with the `--testing` flag as well.
client = ActivityWatchClient("test-client", testing=True)

bucket_id = "{}_{}".format("test-client-bucket", client.client_hostname)
client.create_bucket(bucket_id, event_type="dummydata")

shutdown_data = {"label": "some interesting data"}
now = datetime.now(timezone.utc)
shutdown_event = Event(timestamp=now, data=shutdown_data)
inserted_event = client.insert_event(bucket_id, shutdown_event)

events = client.get_events(bucket_id=bucket_id, limit=1)
print(events) # Should print a single event in a list

client.delete_bucket(bucket_id)
