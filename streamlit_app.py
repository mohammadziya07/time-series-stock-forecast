import streamlit as st
from utils.data_loader import load_stock_data
import matplotlib.pyplot as plt

st.title("📈 Stock Price Forecasting")

ticker = st.text_input("Enter Ticker Symbol", "AAPL")
data = load_stock_data(ticker, "2020-01-01", "2024-12-31")

st.subheader("Historical Closing Prices")
st.line_chart(data['Close'])