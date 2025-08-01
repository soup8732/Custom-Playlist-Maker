import json
import os
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = _SCRIPT_DIR / "data.json"
VERSION_FILE = _SCRIPT_DIR / "version.json"


def load_user_data():
    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
        return data.get("Name"), data.get("Num")
    except FileNotFoundError:
        return None, None


def save_user_data(name, num):
    DATA_FILE.write_text(json.dumps({"Name": name, "Num": num}))


def load_local_version():
    try:
        return json.loads(VERSION_FILE.read_text()).get("version"), json.loads(VERSION_FILE.read_text()).get("version_type")
    except Exception:
        return None

