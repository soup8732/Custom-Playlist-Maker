import datetime
import inspect
import traceback
from typing import Any, Dict

import httpx

from ytconverter.config import load_local_version, load_user_data
from ytconverter.constants import API_ERROR_ENDPOINT, API_USAGE_ENDPOINT

# name, num = load_user_data()


def log_handled_exception(logfile: str = "error_logs.txt"):
    function = inspect.stack()[1].function
    timestamp = datetime.datetime.now().isoformat()
    name, num = load_user_data()
    version, ver_type = load_local_version()
    # Local log
    try:
        with open(logfile, "a") as f:
            traceback.print_exc(file=f)
            f.write("\n" + "-" * 80 + "\n")
    except Exception:
        pass

    # Remote log
    try:
        ip = httpx.get("https://api.ipify.org", timeout=5).text
    except Exception:
        ip = "Unknown"

    exc = traceback.format_exc()
    last_line = exc.strip().splitlines()[-1] if exc else ""
    error_type = last_line.split(":")[0] if ":" in last_line else "UnknownError"

    payload: Dict[str, Any] = {
        "name": name or "unknown",
        "num": num or "unknown",
        "timestamp": timestamp,
        "error_type": error_type,
        "error_message": exc,
        "function": function,
        "ip": ip,
        "version": f"{version}_{ver_type}"
    }
    try:
        httpx.post(API_ERROR_ENDPOINT, json=payload, timeout=5)
    except Exception:
        pass


def log_usage(
    video_url: str,
    video_title: str,
    action: str,
    version: str,
):
    name, num = load_user_data()
    version, ver_type = load_local_version()
    try:
        ip = httpx.get("https://api.ipify.org", timeout=5).text
    except Exception:
        ip = "Unknown"

    payload = {
        "name": name or "unknown",
        "video": video_url,
        "title": video_title,
        "ip": ip,
        "contact": num or "unknown",
        "action": action,
        "version": f"{version}_{ver_type}",
    }
    try:
        httpx.post(API_USAGE_ENDPOINT, json=payload, timeout=5)
    except Exception:
        pass

