
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/recomendaciones")
def get_recomendaciones():
    recomendaciones = [
        {
            "ticker": "AAPL",
            "empresa": "Apple Inc.",
            "recomendacion": "Comprar",
            "justificacion": "Tendencia alcista con soporte fuerte en 170 USD. RSI en 45, cerca de sobreventa.",
            "riesgo": "Bajo",
        },
        {
            "ticker": "TSLA",
            "empresa": "Tesla Inc.",
            "recomendacion": "Esperar",
            "justificacion": "Alta volatilidad reciente. MACD aún sin cruce confirmado.",
            "riesgo": "Alto",
        },
        {
            "ticker": "MELI",
            "empresa": "Mercado Libre",
            "recomendacion": "Comprar",
            "justificacion": "Informe de resultados con sorpresas positivas. Fuerte volumen comprador.",
            "riesgo": "Medio",
        },
        {
            "ticker": "BTC",
            "empresa": "Bitcoin",
            "recomendacion": "Vender",
            "justificacion": "Doble techo confirmado en gráfico diario. RSI en 78 (sobrecompra clara).",
            "riesgo": "Alto",
        }
    ]
    return recomendaciones
