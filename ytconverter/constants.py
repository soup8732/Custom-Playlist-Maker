import re

URL_RE = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$")

API_ERROR_ENDPOINT = "https://tracker-api-od1b.onrender.com/log-error"
API_USAGE_ENDPOINT = "https://tracker-api-od1b.onrender.com/log-download"
VERSION_URL = "https://raw.githubusercontent.com/kaifcodec/ytconverter/main/version.json"
PYPI_VERSION_URL = "https://pypi.org/pypi/ytconverter/json"
