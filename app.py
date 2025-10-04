import streamlit as st
import pandas as pd
from src.data.b3_data import B3Data
from src.utils.investment_calculator import calculate_investment_value, investment_growth_schedule

def main():
    st.title("Brazilian Stocks Dashboard")

    # Input for tickers
    tickers_input = st.text_input("Enter stock tickers (comma-separated, e.g., PETR4.SA,VALE3.SA)", "PETR4.SA,VALE3.SA")

    if tickers_input:
        ticker_list = [ticker.strip() for ticker in tickers_input.split(',')]

        # Fetch data
        b3_data = B3Data()
        stock_data = b3_data.get_stock_data(ticker_list)

        if not stock_data.empty:
            st.subheader("Stock Data")
            st.dataframe(stock_data)
        else:
            st.warning("No data found for the given tickers.")
    
    # Investment Calculator Section
    st.markdown("---")
    st.subheader("💰 Investment Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        principal = st.number_input("Initial Investment (R$)", min_value=0.0, value=10000.0, step=100.0)
        monthly_contribution = st.number_input("Monthly Contribution (R$)", min_value=0.0, value=500.0, step=50.0)
    
    with col2:
        annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=100.0, value=7.0, step=0.1)
        years = st.number_input("Investment Period (years)", min_value=1, max_value=50, value=10, step=1)
    
    # Convert percentage to decimal
    annual_rate_decimal = annual_rate / 100
    
    if st.button("Calculate Investment"):
        final_value = calculate_investment_value(principal, monthly_contribution, annual_rate_decimal, years)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Final Value", f"R$ {final_value:,.2f}")
        
        with col2:
            total_contributions = principal + (monthly_contribution * 12 * years)
            st.metric("Total Contributions", f"R$ {total_contributions:,.2f}")
        
        with col3:
            total_interest = final_value - total_contributions
            st.metric("Interest Earned", f"R$ {total_interest:,.2f}")
        
        # Growth schedule
        st.subheader("Investment Growth Schedule")
        schedule_df = investment_growth_schedule(principal, monthly_contribution, annual_rate_decimal, years)
        st.dataframe(schedule_df)
        
        # Chart
        st.subheader("Investment Growth Chart")
        st.line_chart(schedule_df.set_index('year')[['balance', 'total_contributions']])

if __name__ == "__main__":
    main()
