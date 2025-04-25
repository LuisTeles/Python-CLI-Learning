### app/importers.py
import json
from app.models import create_task

def import_from_file(path: str):
    if path.endswith(".json"):
        with open(path, "r") as f:
            data = json.load(f)
            for item in data:
                create_task(item["name"], item["duration"], item["days_passed"])
    elif path.endswith(".txt"):
        with open(path, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    create_task(parts[0], int(parts[1]), int(parts[2]))