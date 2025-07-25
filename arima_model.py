from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def run_arima(data):
    train = data[:-100]
    test = data[-100:]

    model = ARIMA(train, order=(5,1,0))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=100)
    mse = mean_squared_error(test, forecast)
    print(f'ARIMA MSE: {mse:.2f}')

    plt.figure(figsize=(12,6))
    plt.plot(test.index, test['Close'], label='Actual')
    plt.plot(test.index, forecast, label='Forecast')
    plt.title('ARIMA Forecast')
    plt.legend()
    plt.show()