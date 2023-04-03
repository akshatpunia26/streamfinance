import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(page_title='Simple Finance Dashboard', page_icon=':moneybag:')
ticker_symbol = st.sidebar.text_input("Enter a ticker symbol (e.g. AAPL)", "AAPL")
start_date = st.sidebar.date_input('Start date', datetime.date(2020, 1, 1))
end_date = st.sidebar.date_input('End date', datetime.date(2022, 1, 1))

# Get the stock data from Yahoo Finance
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(start=start_date, end=end_date)

# Calculate some simple metrics
ticker_df['daily_returns'] = ticker_df['Close'].pct_change()
ticker_df['cumulative_returns'] = (1 + ticker_df['daily_returns']).cumprod() - 1
st.header("Stock Price Chart")
st.line_chart(ticker_df['Close'])
st.header("Volume Chart")
st.line_chart(ticker_df['Volume'])
st.header("Daily Returns Chart")
st.line_chart(ticker_df['daily_returns'])
st.header("Cumulative Returns Chart")
st.line_chart(ticker_df['cumulative_returns'])
st.header("Stock Data")
st.write(ticker_df)