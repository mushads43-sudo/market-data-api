from fastapi import APIRouter, Request, HTTPException
from app.services import get_mock_stock
from app.cache import get_cache, set_cache
from app.rate_limiter import is_allowed
from app.config import CACHE_TTL

router = APIRouter()


@router.get("/stock/{symbol}")
def get_stock(symbol: str, request: Request):
    client_ip = request.client.host

    # Rate limiting
    if not is_allowed(client_ip):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    # Cache check
    cached_data = get_cache(symbol)
    if cached_data:
        return {"source": "cache", "data": cached_data}

    # Fetch fresh data
    data = get_mock_stock(symbol)

    # Store in cache
    set_cache(symbol, data, CACHE_TTL)

    return {"source": "api", "data": data}