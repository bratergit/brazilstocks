from src.data import get_stock_data

print(get_stock_data(["PETR4", "VALE3"], period="1mo").head())
