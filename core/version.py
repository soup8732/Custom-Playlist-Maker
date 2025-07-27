import httpx

from ytconverter.config import load_local_version
from ytconverter.constants import VERSION_URL


def check_version():
    try:
        remote = httpx.get(VERSION_URL, timeout=5).json().get("version")
    except Exception:
        return None, None
    local = load_local_version()
    return local, remote
