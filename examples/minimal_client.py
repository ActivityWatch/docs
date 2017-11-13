#!/usr/bin/env python3

from time import sleep
from datetime import datetime, timedelta, timezone

from aw_core.models import Event
from aw_client import ActivityWatchClient

client = ActivityWatchClient("test-client", testing=True)
bucket_id = "{}_{}".format("test-client-bucket", client.hostname)
event_type = "dummydata"

client.create_bucket(bucket_id, event_type="test")

shutdown_data = {"label": "some interesting data"}
shutdown_event = Event(timestamp=now, data=shutdown_data)
inserted_event = client.insert_event(bucket_id, shutdown_event)

events = client.get_events(bucket_id=bucket_id, limit=1)
print(events) # Should print a single event in a list

client.delete_bucket(bucket_id)
