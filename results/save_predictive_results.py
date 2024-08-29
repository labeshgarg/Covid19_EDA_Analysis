import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def save_predictive_results():
   
    data = pd.read_csv('data/processed/processed_covid_data.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    aggregated_data = data.groupby('Date')['ConfirmedCases'].sum()

    model = ARIMA(aggregated_data, order=(1, 1, 1))
    result = model.fit()
    forecast = result.get_forecast(steps=30)
    forecast_df = forecast.summary_frame()

    forecast_df.to_csv('results/predictive_results.csv')
    print("Predictive results saved to 'results/predictive_results.csv'")

if __name__ == "__main__":
    save_predictive_results()
