# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from scipy.stats import ttest_ind
# from statsmodels.tsa.arima.model import ARIMA

# def load_data(path):
#     return pd.read_csv(path)

# def clean_data(data):
#     data = data.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"], var_name="Date", value_name="ConfirmedCases")
#     data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y')
#     return data

# def handle_missing_values(data):
#     missing_percent = data.isnull().sum() * 100 / len(data)
#     print("Missing values percentage:\n", missing_percent)

#     # Drop columns with more than 50% missing values (if any)
#     data = data.loc[:, missing_percent < 50]

#     # For other columns, fill missing values
#     data.fillna(method='ffill', inplace=True)
#     return data

# def normalize_data(data):
#     scaler = MinMaxScaler()
#     data[['ConfirmedCases']] = scaler.fit_transform(data[['ConfirmedCases']])
#     return data

# def add_new_cases_feature(data):
#     data['NewCases'] = data.groupby('Country/Region')['ConfirmedCases'].diff().fillna(0)
#     return data

# def compare_two_groups(data, group1, group2):
#     group1_data = data[data['Country/Region'] == group1]['ConfirmedCases']
#     group2_data = data[data['Country/Region'] == group2]['ConfirmedCases']
    
#     stat, p = ttest_ind(group1_data, group2_data)
#     print(f"Statistical Test Result: t={stat}, p={p}")

# def perform_time_series_forecasting(data):
#     model = ARIMA(data['ConfirmedCases'], order=(1, 1, 1))
#     result = model.fit()
#     print(result.summary())
#     return result

# # Load and clean the data
# data_path = 'data/raw/time_series_covid19_confirmed_global.csv'
# data = load_data(data_path)
# data = clean_data(data)
# data = handle_missing_values(data)
# data = normalize_data(data)
# data = add_new_cases_feature(data)

# # Optionally, apply statistical testing or forecasting
# compare_two_groups(data, 'Italy', 'Spain')
# forecast_result = perform_time_series_forecasting(data[data['Country/Region'] == 'US'])

# # Save the processed data
# data.to_csv('data/processed/advanced_processed_covid_data.csv', index=False)
import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(data):
    data = data.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"], var_name="Date", value_name="ConfirmedCases")
    data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y')
    return data

def add_new_cases_feature(data):
    
    data.sort_values(['Country/Region', 'Date'], inplace=True)
    data['NewCases'] = data.groupby('Country/Region')['ConfirmedCases'].diff().fillna(0)
    return data

def main():
    data_path = 'data/raw/time_series_covid19_confirmed_global.csv'
    data = load_data(data_path)
    data = clean_data(data)
    data = add_new_cases_feature(data)

    data.to_csv('data/processed/processed_covid_data.csv', index=False)
    print('Data processing completed and saved.')

if __name__ == "__main__":
    main()
