import streamlit as st
import pandas as pd
from src.data.b3_data import B3Data


def main():
    st.title("Brazilian Stocks Dashboard")

    # Input for tickers
    tickers_input = st.text_input(
        "Enter stock tickers (comma-separated, e.g., PETR4.SA,VALE3.SA)",
        "PETR4.SA,VALE3.SA",
    )

    if tickers_input:
        ticker_list = [ticker.strip() for ticker in tickers_input.split(",")]

        # Fetch data
        b3_data = B3Data()
        stock_data = b3_data.get_stock_data(ticker_list)

        if not stock_data.empty:
            st.subheader("Stock Data")
            st.dataframe(stock_data)
        else:
            st.warning("No data found for the given tickers.")


if __name__ == "__main__":
    main()
