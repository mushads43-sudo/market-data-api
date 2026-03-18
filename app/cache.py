import redis
import json
from app.config import REDIS_HOST, REDIS_PORT

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_cache(key):
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None


def set_cache(key, value, ttl):
    redis_client.setex(key, ttl, json.dumps(value))