📈 Country Finance Intelligence Agent

An AI-powered Streamlit application that provides real-time financial intelligence about selected countries, including:

Official currency

Real-time exchange rates

Major stock exchanges and indices

Live index values

Google Maps location of stock exchange headquarters

AI-generated economic summary

🚀 Features
1️⃣ Official Currency

Displays the official currency of the selected country.

2️⃣ Real-Time Exchange Rates

Fetches live exchange rates of 1 unit of the country’s currency to:

USD

INR

GBP

EUR

Uses: ExchangeRate-API

3️⃣ Stock Market Data

Displays:

Major stock index (e.g., Nikkei 225, S&P 500, Sensex)

Current live index value

Uses: Yahoo Finance (yfinance)

4️⃣ Stock Exchange Location

Displays Google Maps pin of the country’s main stock exchange headquarters.

Uses: Streamlit st.map()

5️⃣ AI Economic Summary

Generates a short AI-based summary explaining:

Economic importance

Financial market significance

Uses:

LLM via OpenRouter (Mistral 7B)

🏗 Tech Stack
Component	Technology Used
Frontend	Streamlit
LLM Engine	Mistral 7B (via OpenRouter)
Financial Data	Yahoo Finance
Exchange Rates	ExchangeRate API
Maps	Streamlit Map
Framework	LangChain-style Agent Architecture
📂 Project Structure
ps2_finance_agent/
│
├── app.py
├── requirements.txt
├── README.md

🔐 Environment Variables (Streamlit Cloud Secrets)

Add the following inside Streamlit Cloud → Settings → Secrets:

OPENROUTER_API_KEY = "your_openrouter_key"

🖥 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/yourusername/ps2_finance_agent.git
cd ps2_finance_agent

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Application
streamlit run app.py

🌍 Supported Countries

Japan

India

United States

United Kingdom

China

South Korea

📸 Expected Output

For example, if user selects Japan, the app displays:

Currency: JPY

Exchange Rates (JPY → USD, INR, GBP, EUR)

Index: Nikkei 225 (live value)

Map pin: Tokyo Stock Exchange

AI-generated economic summary

🎓 Academic Objective

This project demonstrates:

Integration of LLM with deterministic financial APIs

Real-time data retrieval

Hybrid AI + API architecture

Streamlit-based UX design

Financial data orchestration using agent-like structure

🧠 Architecture Overview

User Input → Streamlit UI
→ LLM for contextual reasoning
→ Financial APIs for factual data
→ Unified structured output

This hybrid approach ensures:

Reduced hallucination

Real-time financial accuracy

Context-aware explanation

⚠️ Disclaimer

Exchange rates and stock values are fetched in real time.

Data accuracy depends on external APIs.

This application is for educational purposes only.
