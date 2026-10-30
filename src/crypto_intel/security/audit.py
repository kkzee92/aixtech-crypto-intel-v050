"""Hash-chained audit log with multi-hash seal."""
import hashlib
import json
from datetime import datetime, timezone

def seal_event(event: dict, prev_hash: str = "") -> dict:
    event["timestamp"] = datetime.now(timezone.utc).isoformat()
    event["prev_hash"] = prev_hash
    payload = json.dumps(event, sort_keys=True).encode()
    event["sha256"] = hashlib.sha256(payload).hexdigest()
    event["sha3"] = hashlib.sha3_256(payload).hexdigest()  # multi-hash
    return event
