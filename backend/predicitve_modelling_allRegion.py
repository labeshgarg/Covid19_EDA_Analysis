import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt

def main():
    data = pd.read_csv('data/processed/processed_covid_data.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    aggregated_data = data.groupby('Date')['ConfirmedCases'].sum()

    model = ARIMA(aggregated_data, order=(1, 1, 1))
    result = model.fit()
    forecast = result.get_forecast(steps=30)
    forecast_df = forecast.summary_frame()

    y_true = aggregated_data[-30:] #30 days
    y_pred = forecast_df['mean']
    rmse = sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    print(f"RMSE: {rmse}, MAE: {mae}")

    plt.figure(figsize=(10, 5))
    plt.plot(aggregated_data.index, aggregated_data, label='Actual Cases')
    plt.plot(forecast_df.index, forecast_df['mean'], label='Forecasted Cases', color='red')
    plt.fill_between(forecast_df.index, forecast_df['mean_ci_lower'], forecast_df['mean_ci_upper'], color='pink', alpha=0.3)
    plt.title('Global Forecast vs Actuals')
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
