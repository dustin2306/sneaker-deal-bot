import json
import os

FILE = "deals_seen.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

def is_new(deal_id):
    with open(FILE, "r") as f:
        seen = json.load(f)

    if deal_id in seen:
        return False

    seen.append(deal_id)
    with open(FILE, "w") as f:
        json.dump(seen, f)

    return True
