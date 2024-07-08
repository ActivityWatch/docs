#!/usr/bin/env python3
from aw_client import ActivityWatchClient
from aw_core.models import Event
import re
from typing import Pattern, cast, List, Set
from copy import deepcopy

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

# sensitive data pattern
pattern = re.compile(r"Binance|Metamask|TrustWallet|Trust Wallet")

# what to replace sensitive data with
REDACTED = "REDACTED"

def _redact_event(e: Event, pattern: Pattern) -> Event:
    e = deepcopy(e)
    for k, v in e.data.items():
        if isinstance(v, str):
            if pattern.findall(v.lower()):
                e.data[k] = REDACTED
    return e

def _find_sensitive(el: List[Event], pattern: Pattern) -> Set:
    sensitive_ids = set()
    for e in el:
        if _check_event(e, pattern):
            sensitive_ids.add(e.id)
    return sensitive_ids

def _check_event(e: Event, pattern: Pattern) -> bool:
    for k, v in e.data.items():
        if isinstance(v, str):
            if pattern.findall(v.lower()):
                return True
    return False

sensitive_ids = _find_sensitive(events, pattern)
for e in events:
    print(f"Event id: {e.id}")
    if e.id in sensitive_ids:
        e_before = e
        e = _redact_event(e, pattern)
        print(f"\nData before: {e_before.data}")
        print(f"Data after:  {e.data}")
        
        client.delete_event(bucket_id, cast(int, e_before.id))
        client.insert_event(bucket_id, e)
        print("Redacted event")
