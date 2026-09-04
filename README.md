# 📈 Dynamic Pricing with Machine Learning

This project implements a basic dynamic pricing system using synthetic data and a Machine Learning model.

It is a practical example for understanding how pricing models can adjust prices based on demand, competition, and seasonality.

## 🚀 What Does This Project Solve?

The goal is to estimate a suggested optimal price based on multiple factors:

- Demand index (`demand_index`)
- Competitor price (`competitor_price`)
- Seasonality (`seasonality`)
- Optional price floor and ceiling
- Business constraints such as maximum allowed markup

This provides a practical foundation for building real-world dynamic pricing systems for:

- eCommerce
- SaaS
- Retail
- Marketplaces
- Services with variable demand

## 🧠 How It Works

### 1. Synthetic Data Generation

The project generates a synthetic dataset with 500 rows simulating:

- Demand (0–1)
- Average competitor price
- Seasonality
- Observed optimal price (target)

### 2. Model Training

A `LinearRegression` model is trained to learn the relationship between the input variables and the target price.

### 3. Model Evaluation

The project reports:

- MAE (Mean Absolute Error)
- Model coefficients
- Model intercept

### 4. Price Recommendation

The `suggest_price()` function combines the trained model with business rules to:

- Prevent excessive markups
- Respect optional price floors and ceilings
- Return a final rounded price

## ▶️ Installation

```bash
pip install -r requirements.txt
