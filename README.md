# Real-Time Market Data API + Caching System

## **Overview**

This project is a high-performance backend system that simulates real-time market data APIs with caching and rate limiting.

It is designed to deliver low-latency responses, handle high request volumes, and demonstrate scalable backend architecture commonly used in financial systems.

---

## **Problem Statement**

Real-time market data systems must handle large volumes of requests while maintaining low latency and reliability. Without proper optimization, repeated API calls can increase response time and overload external services.

This project addresses these challenges by:
- Implementing caching to reduce redundant API calls  
- Applying rate limiting to prevent system abuse and ensure stability  
- Designing scalable APIs capable of handling high throughput  
- Simulating real-world financial data systems  

---

## **Tech Stack**

- Backend Framework: FastAPI  
- Caching: Redis  
- Language: Python  
- API Design: REST  
- Server: Uvicorn  

---

## **Approach**

### **Data Collection and Integration**
- Integrated mock and real-time API data sources  
- Fetched stock/crypto price data dynamically  
- Standardized response format for consistency  

---

### **Feature Engineering / System Design**
- Implemented cache-aside pattern for efficient data retrieval  
- Designed stateless API architecture for scalability  
- Added rate limiting to control request frequency  
- Optimized for low-latency responses  

---

### **Model Building (System Logic)**

- **API Layer:**
  - Built REST endpoint for fetching stock data  
  - Ensured structured JSON responses  

- **Caching Layer:**
  - Used Redis to store frequently accessed data  
  - Served cached responses when available  

- **Rate Limiting:**
  - Restricted excessive API calls to prevent abuse  
  - Improved system stability under load  

---

### **Evaluation**

- Measured response time improvement using caching  
- Verified correct cache hits and misses  
- Tested rate limiting under multiple requests  
- Ensured consistent API performance  

---

## **Results**

- Achieved low-latency responses using Redis caching  
- Reduced redundant API calls significantly  
- Built a scalable and efficient backend system  
- Ensured system reliability with rate limiting  
- Successfully simulated real-time market data API behavior  

---

## **Output**

- REST API endpoint for market data retrieval  
- JSON-based responses with source (cache/API)  
- Improved response time via caching layer  
- Stable performance under multiple requests  

---

## **How to Run**

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
## **Key Learning**

- Built a high-performance backend system using FastAPI  
- Implemented Redis caching using the cache-aside pattern  
- Learned rate limiting techniques for system protection  
- Designed scalable and stateless API architecture  
- Improved system performance by reducing redundant API calls  
- Gained understanding of real-time data systems in finance  
- Strengthened backend development and system design skills  
- Learned how to optimize APIs for low-latency responses  
