# Dynamic pricing - minimal example (run in Colab)
# Requisitos: pip install -U scikit-learn pandas numpy
# Código simple: genera datos sintéticos, entrena un modelo y recomienda precio.

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# -----------------------------
# 1) Generar dataset sintético
# -----------------------------
np.random.seed(0)
n = 500

# Features:
# - demand_index: demanda esperada (0..1)
# - competitor_price: precio medio competencia
# - seasonality: 0=low, 1=high (por ejemplo: temporada)
demand_index = np.clip(np.random.beta(2, 2, size=n), 0.05, 0.99)
competitor_price = np.random.normal(loc=100, scale=15, size=n)  # precio base de la competencia
seasonality = np.random.choice([0, 1], size=n, p=[0.7, 0.3])    # 30% temporada alta

# Regla simple para construir "precio óptimo observado" (target)
# Supongamos que precio objetivo sube con demanda y con seasonality,
# y se ajusta parcialmente respecto a la competencia.
base_margin = 10
price = competitor_price * 0.9 + base_margin + (demand_index - 0.5) * 40 + seasonality * 8
# agregar ruido
price += np.random.normal(scale=5, size=n)

df = pd.DataFrame({
    "demand_index": demand_index,
    "competitor_price": competitor_price,
    "seasonality": seasonality,
    "observed_price": price
})

# -----------------------------
# 2) Entrenar modelo predictivo
# -----------------------------
X = df[["demand_index", "competitor_price", "seasonality"]]
y = df["observed_price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluación rápida
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("Coeficientes:", dict(zip(X.columns, model.coef_)))
print("Intercept:", model.intercept_)

# -----------------------------
# 3) Función simple de recomendación
# -----------------------------
def suggest_price(demand_index, competitor_price, seasonality,
                  floor_price=None, ceiling_price=None, markup_limit=0.25):
    """
    Devuelve un precio sugerido usando el modelo entrenado.
    Parámetros:
      - demand_index: float en [0,1]
      - competitor_price: float (moneda)
      - seasonality: 0 o 1
      - floor_price, ceiling_price: opcionales límites
      - markup_limit: máximo markup relativo sobre competitor_price (ej. 0.25 = 25%)
    """
    X_in = np.array([[demand_index, competitor_price, int(bool(seasonality))]])
    predicted = float(model.predict(X_in)[0])

    # Aplicar política simple de negocio (ejemplos)
    # 1) No superar markup razonable sobre competencia
    max_allowed = competitor_price * (1 + markup_limit)
    suggested = min(predicted, max_allowed)
    # 2) Respetar piso y techo si se proporcionan
    if floor_price is not None:
        suggested = max(suggested, floor_price)
    if ceiling_price is not None:
        suggested = min(suggested, ceiling_price)

    # Redondeo práctico
    return round(suggested, 2)

# -----------------------------
# 4) Ejemplos de uso
# -----------------------------
examples = [
    (0.2, 95, 0),
    (0.8, 95, 1),
    (0.5, 110, 0),
    (0.9, 80, 1),
]

for d, c, s in examples:
    print(f"demand={d}, comp_price={c}, season={s} -> suggested = {suggest_price(d, c, s)}")
