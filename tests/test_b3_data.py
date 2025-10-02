import pandas as pd
from src.data.b3_data import get_stock_data

def test_fetch_two_tickers():
    df = get_stock_data(["PETR4","VALE3"], period="1mo", interval="1d")
    assert isinstance(df, pd.DataFrame)
    assert {"ticker","date"}.issubset(df.columns)
    assert {"PETR4.SA","VALE3.SA"}.issubset(set(df["ticker"].unique()))
    assert len(df) > 0
