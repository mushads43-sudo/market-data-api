import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
CACHE_TTL = int(os.getenv("CACHE_TTL"))
RATE_LIMIT = int(os.getenv("RATE_LIMIT"))