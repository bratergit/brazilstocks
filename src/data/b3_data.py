from __future__ import annotations
from typing import Iterable, List, Union
import pandas as pd
import yfinance as yf

_COLMAP = {"Open":"open","High":"high","Low":"low","Close":"close","Volume":"volume"}

def _norm(t: str) -> str:
    t = t.strip().upper()
    return t if t.endswith(".SA") else f"{t}.SA"

def get_stock_data(
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
    tickers = [_norm(t) for t in tickers]

    frames: List[pd.DataFrame] = []
    for t in tickers:
        hist = yf.Ticker(t).history(period=period, interval=interval, auto_adjust=auto_adjust)
        if hist.empty:
            continue
        hist = hist.rename(columns=_COLMAP)
        keep = [c for c in ["open","high","low","close","volume"] if c in hist.columns]
        hist = hist[keep]
        hist["ticker"] = t
        hist = hist.reset_index().rename(columns={"Date":"date"})
        frames.append(hist)

    if not frames:
        return pd.DataFrame(columns=["ticker","date","open","high","low","close","volume"])

    df = pd.concat(frames, ignore_index=True)
    return df.sort_values(["ticker","date"]).reset_index(drop=True)
