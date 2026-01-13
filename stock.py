import datetime

import streamlit as st
# "yfinance" is a popular library to fetch financial data
import yfinance as yf

st.title("Stock Price Analyzer")
st.subheader("Analyze and visualize stock prices over time.")

col1, col2, col3 = st.columns(3)
with col1:
    company = st.text_input("Company ticker", "MSFT")
with col2:
    sd = st.date_input("Start date", datetime.date(2024, 10, 1))
with col3:
    ed = st.date_input("End date", datetime.date(2024, 12, 31))

ticker = yf.Ticker(company)
ticker_data = ticker.history(start=sd, end=ed)

st.subheader("Here is the raw day wise stock price." + f" ({company})")
st.dataframe(ticker_data.head())

st.subheader("Price movement over time.")
st.line_chart(ticker_data["Close"])

st.subheader("Volume traded over time.")
st.bar_chart(ticker_data["Volume"])