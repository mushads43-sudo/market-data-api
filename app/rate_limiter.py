import time
from app.config import RATE_LIMIT

request_log = {}


def is_allowed(client_ip):
    now = time.time()
    window = 60  # 1 minute window

    if client_ip not in request_log:
        request_log[client_ip] = []

    request_log[client_ip] = [t for t in request_log[client_ip] if now - t < window]

    if len(request_log[client_ip]) >= RATE_LIMIT:
        return False

    request_log[client_ip].append(now)
    return True
