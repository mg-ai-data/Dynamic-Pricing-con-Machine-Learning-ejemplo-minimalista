📈 Dynamic Pricing con Machine Learning (Ejemplo Minimalista) Este proyecto implementa un sistema básico de precios dinámicos utilizando datos sintéticos y un modelo de Machine Learning. Es un ejemplo ideal para entender cómo funcionan los modelos que ajustan precios según demanda, competencia y estacionalidad.

Incluye:

Generación de dataset sintético Entrenamiento de un modelo (Linear Regression) Evaluación rápida del desempeño Función de recomendación de precios basada en reglas de negocio 🚀 ¿Qué resuelve este proyecto? El objetivo es estimar un precio óptimo sugerido considerando múltiples factores:

Índice de demanda (demand_index) Precio de la competencia (competitor_price) Estacionalidad (seasonality) Límites opcionales de precio (piso/techo) Restricciones comerciales como markup máximo permitido Es una base práctica para construir sistemas reales de pricing dinámico en:

eCommerce SaaS Retail Marketplaces Servicios con demanda variable 🧠 Cómo funciona

Generación de datos sintéticos Crea un dataset con 500 filas simulando:
Demanda (0..1) Precio promedio de competidores Estacionalidad Precio óptimo observado (target) 2) Entrenamiento Se usa LinearRegression para aprender la relación entre las variables y el precio objetivo.

Evaluación Imprime:
MAE (error absoluto medio) Coeficientes del modelo Intercepto 4) Función suggest_price() Usa el modelo + reglas de negocio para:

Prevenir precios demasiado altos (markup limit) Respetar piso/techo si se especifican Entregar un precio final redondeado

▶️ Instalación ```bash pip install -r requirements.txt
