import streamlit as st
import requests
import yfinance as yf
import os

# =========================
# CONFIG (Streamlit Cloud)
# =========================
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

# =========================
# COUNTRY DATA
# =========================
country_currency = {
    "Japan": "JPY",
    "India": "INR",
    "US": "USD",
    "UK": "GBP",
    "China": "CNY",
    "South Korea": "KRW"
}

country_indices = {
    "Japan": {
        "Nikkei 225": "^N225",
        "Tokyo Stock Exchange": {"lat": 35.682839, "lon": 139.759455}
    },
    "India": {
        "BSE Sensex": "^BSESN",
        "Bombay Stock Exchange": {"lat": 18.9296, "lon": 72.8331}
    },
    "US": {
        "S&P 500": "^GSPC",
        "New York Stock Exchange": {"lat": 40.7069, "lon": -74.0113}
    },
    "UK": {
        "FTSE 100": "^FTSE",
        "London Stock Exchange": {"lat": 51.5155, "lon": -0.0922}
    },
    "China": {
        "Shanghai Composite": "000001.SS",
        "Shanghai Stock Exchange": {"lat": 31.2304, "lon": 121.4737}
    },
    "South Korea": {
        "KOSPI": "^KS11",
        "Korea Exchange": {"lat": 37.5665, "lon": 126.9780}
    }
}

# =========================
# LLM RESPONSE (OpenRouter)
# =========================
def generate_llm_summary(country):
    prompt = f"""
    Provide one short paragraph explaining the economic significance
    and stock market importance of {country}.
    """

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
        },
    )

    return response.json()["choices"][0]["message"]["content"]

# =========================
# EXCHANGE RATE
# =========================
def get_exchange_rates(currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
    response = requests.get(url).json()

    return {
        "USD": response["rates"].get("USD"),
        "INR": response["rates"].get("INR"),
        "GBP": response["rates"].get("GBP"),
        "EUR": response["rates"].get("EUR"),
    }

# =========================
# STOCK VALUE
# =========================
def get_index_value(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    return float(data["Close"].iloc[-1])

# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Finance Intelligence Agent", layout="wide")

st.title("📈 Country Finance Intelligence Agent")

country = st.selectbox(
    "Select Country",
    ["Japan", "India", "US", "UK", "China", "South Korea"]
)

if st.button("Get Details"):

    currency = country_currency[country]

    st.subheader("💰 Official Currency")
    st.write(currency)

    st.subheader("💱 Exchange Rates (1 Unit)")
    rates = get_exchange_rates(currency)

    st.write(f"1 {currency} →")
    st.write(f"USD: {rates['USD']}")
    st.write(f"INR: {rates['INR']}")
    st.write(f"GBP: {rates['GBP']}")
    st.write(f"EUR: {rates['EUR']}")

    st.subheader("📊 Major Stock Index")

    index_name = list(country_indices[country].keys())[0]
    index_symbol = country_indices[country][index_name]

    index_value = get_index_value(index_symbol)

    st.write(f"{index_name}: {index_value}")

    st.subheader("📍 Stock Exchange HQ Location")

    exchange_name = list(country_indices[country].keys())[1]
    location = country_indices[country][exchange_name]

    st.map({
        "lat": [location["lat"]],
        "lon": [location["lon"]]
    })

    st.subheader("🧠 AI Economic Summary")

    summary = generate_llm_summary(country)
    st.write(summary)
