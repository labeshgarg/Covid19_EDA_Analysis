import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt

def main():
    data = pd.read_csv('data/processed/processed_covid_data.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    afghanistan_data = data[data['Country/Region'] == 'Afghanistan']
    afghanistan_data.set_index('Date', inplace=True)

    model = ARIMA(afghanistan_data['ConfirmedCases'], order=(1, 1, 1))
    result = model.fit()
    forecast = result.get_forecast(steps=30)
    forecast_df = forecast.summary_frame()

    y_true = afghanistan_data['ConfirmedCases'][-30:]  # Assuming last 30 days as a test set
    y_pred = forecast_df['mean']
    rmse = sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    print(f"RMSE: {rmse}, MAE: {mae}")

    plt.figure(figsize=(10, 5))
    plt.plot(afghanistan_data.index, afghanistan_data['ConfirmedCases'], label='Actual Cases')
    plt.plot(forecast_df.index, forecast_df['mean'], label='Forecasted Cases', color='red')
    plt.fill_between(forecast_df.index, forecast_df['mean_ci_lower'], forecast_df['mean_ci_upper'], color='pink', alpha=0.3)
    plt.title('Forecast vs Actuals for Afghanistan')
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
