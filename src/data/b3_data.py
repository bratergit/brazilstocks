from __future__ import annotations
from typing import Iterable, List, Union
import pandas as pd
import yfinance as yf

_COLMAP = {"Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume": "volume"}

class B3Data:
    def _norm(self, t: str) -> str:
        t = t.strip().upper()
        return t if t.endswith(".SA") else f"{t}.SA"

    def get_stock_data(
        self,
        ticker_list: Union[str, Iterable[str]],
        period: str = "1y",
        interval: str = "1d",
        auto_adjust: bool = True,
    ) -> pd.DataFrame:
        """
        Return OHLCV for B3 tickers using yfinance.
        Columns: ['ticker','date','open','high','low','close','volume']
        """
        tickers = [ticker_list] if isinstance(ticker_list, str) else list(ticker_list)
        if not tickers:
            raise ValueError("ticker_list must not be empty")
        tickers = [self._norm(t) for t in tickers]

        frames: List[pd.DataFrame] = []
        for t in tickers:
            hist = yf.Ticker(t).history(period=period, interval=interval, auto_adjust=auto_adjust)
            if hist.empty:
                continue
            hist = hist.rename(columns=_COLMAP)
            keep = [c for c in ["open", "high", "low", "close", "volume"] if c in hist.columns]
            hist = hist[keep]
            hist["ticker"] = t
            hist = hist.reset_index().rename(columns={"Date": "date"})
            frames.append(hist)

        if not frames:
            return pd.DataFrame(columns=["ticker", "date", "open", "high", "low", "close", "volume"])

        df = pd.concat(frames, ignore_index=True)
        return df.sort_values(["ticker", "date"]).reset_index(drop=True)

    def __init__(self):
        pass
    
    def get_stock_data(self, tickers, period="1mo"):
        """
        Fetch stock data for given tickers from Yahoo Finance
        
        Args:
            tickers (list): List of stock tickers
            period (str): Period for data (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
        
        Returns:
            pandas.DataFrame: Stock data
        """
        try:
            data = yf.download(tickers, period=period, group_by='ticker')
            
            if len(tickers) == 1:
                # Single ticker case
                df = data.reset_index()
                df['Ticker'] = tickers[0]
                return df
            else:
                # Multiple tickers case
                combined_data = []
                for ticker in tickers:
                    if ticker in data.columns.levels[0]:
                        ticker_data = data[ticker].reset_index()
                        ticker_data['Ticker'] = ticker
                        combined_data.append(ticker_data)
                
                if combined_data:
                    return pd.concat(combined_data, ignore_index=True)
                else:
                    return pd.DataFrame()
        
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

def get_stock_data(tickers, period="1mo"):
    """Standalone function for backwards compatibility"""
    b3_data = B3Data()
    return b3_data.get_stock_data(tickers, period)
