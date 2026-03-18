# 📈 Real-Time Market Data API + Caching System

## 🚀 Overview
A high-performance backend system simulating real-time market data APIs with caching and rate limiting.

## 💡 Features
- FastAPI backend
- Redis caching (low latency)
- Rate limiting (DoS protection)
- REST API design
- Mock + real API integration

## 🧠 System Design Highlights
- Cache-aside pattern
- Stateless API
- Low latency responses
- Horizontal scalability ready

## ⚡ Endpoints
GET /stock/{symbol}

## ▶️ Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🔥 Example
```bash
GET /stock/bitcoin
```


## 📊 Output
{
  "source": "cache",
  "data": {
    "symbol": "bitcoin",
    "price": 342.12
  }
}

## 🏦 Why This Project Stands Out
- Demonstrates backend engineering fundamentals
- Shows system design thinking
- Finance + scalability domain

## 🔮 Future Improvements
- WebSockets (real-time streaming)
- Kafka integration
- Distributed rate limiting
- Docker deployment
