# 📈 Stock Recommendation System (Full-Stack AI Project)

🔗 **Live Application:**  
👉 https://stock-recommendation-system.onrender.com/

---

## 🧠 Problem Statement

Stock market decisions are often influenced by emotions, incomplete information, and delayed analysis.  
Retail investors usually lack access to:

- Data-driven price trend analysis  
- Financial news sentiment interpretation  
- A unified system that converts analysis into actionable insights  

### 🎯 Objective
To build an **end-to-end intelligent stock recommendation platform** that analyzes historical stock prices and financial news sentiment to generate **BUY / HOLD / SELL** recommendations through a user-friendly web interface.

---

## 💡 Solution Overview

This project is a **full-stack AI-powered web application** that:

- Fetches historical stock market data
- Performs feature engineering
- Uses machine learning to predict price movement
- Analyzes financial news sentiment using NLP
- Combines predictions and sentiment to generate recommendations
- Displays results in a modern, animated fintech-style UI
- Is fully deployed and accessible online

---

## 🏗️ System Architecture

# 📈 Stock Recommendation System (Full-Stack AI Project)

🔗 **Live Application:**  
👉 https://stock-recommendation-system.onrender.com/

---

## 🧠 Problem Statement

Stock market decisions are often influenced by emotions, incomplete information, and delayed analysis.  
Retail investors usually lack access to:

- Data-driven price trend analysis  
- Financial news sentiment interpretation  
- A unified system that converts analysis into actionable insights  

### 🎯 Objective
To build an **end-to-end intelligent stock recommendation platform** that analyzes historical stock prices and financial news sentiment to generate **BUY / HOLD / SELL** recommendations through a user-friendly web interface.

---

## 💡 Solution Overview

This project is a **full-stack AI-powered web application** that:

- Fetches historical stock market data
- Performs feature engineering
- Uses machine learning to predict price movement
- Analyzes financial news sentiment using NLP
- Combines predictions and sentiment to generate recommendations
- Displays results in a modern, animated fintech-style UI
- Is fully deployed and accessible online

---

## 🏗️ System Architecture

    User (Browser)
    ↓
    Frontend (HTML, CSS, JavaScript)
    ↓
    Flask Backend (API)
    ↓
    ML Pipeline
    ├── Stock Data Fetching
    ├── Data Preprocessing
    ├── Price Prediction Model
    ├── News Sentiment Analysis
    └── Recommendation Engine

---

## ⚙️ Technology Stack

### 🔹 Backend
- Python
- Flask
- Gunicorn (production server)

### 🔹 Machine Learning
- Scikit-learn (Random Forest Classifier)
- Pandas, NumPy
- Joblib (model persistence)

### 🔹 Data Sources
- Yahoo Finance – Historical stock prices
- Yahoo Finance – Financial news headlines

### 🔹 NLP
- NLTK (VADER Sentiment Analyzer)

### 🔹 Frontend
- HTML5
- CSS3 (modern fintech UI, animations, parallax effects)
- JavaScript (AJAX, DOM manipulation)
- Chart.js (candlestick chart visualization)

### 🔹 Deployment
- Render (Free Tier)
- GitHub (source code hosting)

---

## 🧩 Key Features

### ✅ Stock Data Analysis
- Uses a **pre-trained fixed list of stocks**
- Dropdown-based selection to prevent invalid inputs

### ✅ Machine Learning Prediction
- Predicts **next-day price movement** (UP / DOWN)
- Outputs prediction confidence score

### ✅ News Sentiment Analysis
- Fetches latest financial news headlines
- Classifies sentiment as **Positive / Neutral / Negative**

### ✅ Recommendation Engine
Final recommendation is generated using:
- Predicted price direction
- Model confidence threshold
- News sentiment score

Outputs:
- 🟢 BUY  
- 🟡 HOLD  
- 🔴 SELL  

### ✅ Modern User Interface
- Animated landing page (About section)
- Scroll-based reveal & parallax background
- Candlestick price chart
- Live Indian Standard Time display
- Cursor-follow animation
- Fully mobile responsive design

---

## 🖥️ User Flow

1. Application opens with **About Us** landing section
2. User scrolls down to the analyzer
3. Selects a stock from the dropdown
4. Clicks **Analyze**
5. System displays:
   - Price direction
   - Confidence score
   - News sentiment
   - BUY / HOLD / SELL recommendation
   - Candlestick price chart

---

## 🚀 Deployment Details

The application is deployed using **Render (Free Tier)**.

### Deployment Configuration

- **Build Command**
  ```bash
  pip install -r requirements.txt
- **Start Command**
  ```bash
  gunicorn api.app:app
  ```
## Project Structure
      stock-platform/
      │
      ├── api/
      │   └── app.py              # Flask entry point
      │
      ├── app/
      │   ├── pipeline.py         # End-to-end ML pipeline
      │   └── config.py
      │
      ├── ml/
      │   ├── fetch.py            # Stock data fetching
      │   ├── preprocess.py       # Feature engineering
      │   ├── predict.py          # Price prediction
      │   ├── sentiment.py        # News sentiment analysis
      │   └── recommend.py        # Recommendation logic
      │
      ├── frontend/
      │   ├── index.html          # UI layout
      │   ├── style.css           # Styling & animations
      │   └── script.js           # Frontend logic
      │
      ├── models/                 # Trained ML models
      ├── requirements.txt
      └── README.md

