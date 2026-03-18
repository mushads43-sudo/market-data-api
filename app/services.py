import random
import requests

# OPTION 1: Mock Data (Safe)
def get_mock_stock(symbol):
    return {
        "symbol": symbol,
        "price": round(random.uniform(100, 500), 2),
        "timestamp": "real-time"
    }

# OPTION 2: Real API (optional)
def get_real_stock(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    return response.json()