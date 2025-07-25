from utils.data_loader import load_stock_data
from models.arima_model import run_arima
# from models.prophet_model import run_prophet
# from models.lstm_model import run_lstm

# Load stock data
data = load_stock_data('AAPL', '2015-01-01', '2024-12-31')

# Run desired model
run_arima(data)
# run_prophet(data)
# run_lstm(data)