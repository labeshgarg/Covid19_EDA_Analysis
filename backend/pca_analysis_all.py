# # import pandas as pd
# # from sklearn.decomposition import PCA
# # from sklearn.preprocessing import StandardScaler
# # import matplotlib.pyplot as plt

# # def main():
# #     data = pd.read_csv('data/processed/processed_covid_data.csv')
# #     features = StandardScaler().fit_transform(data[['NewCases', 'ConfirmedCases']].dropna())

# #     # PCA for all regions
# #     pca = PCA(n_components=2)
# #     principal_components = pca.fit_transform(features)
    
# #     # Explained Variance
# #     print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")

# #     # Plotting
# #     plt.figure(figsize=(8, 6))
# #     plt.scatter(principal_components[:, 0], principal_components[:, 1], alpha=0.7)
# #     plt.title('Global PCA')
# #     plt.xlabel('Principal Component 1')
# #     plt.ylabel('Principal Component 2')
# #     plt.show()

# # if __name__ == "__main__":
# #     main()
# import pandas as pd
# import matplotlib.pyplot as plt
# from statsmodels.tsa.arima.model import ARIMA

# def plot_zoomed_forecast(zoom_days=180):
#     """
#     Plots the forecast vs actual cases with a zoomed-in view based on the specified number of days.

#     Parameters:
#     zoom_days (int): Number of days to zoom in on from the most recent date.
#     """
#     # Load data and ensure dates are parsed correctly
#     data = pd.read_csv('data/processed/processed_covid_data.csv')
#     data['Date'] = pd.to_datetime(data['Date'])
#     data.set_index('Date', inplace=True)

#     # Aggregate confirmed cases for all regions
#     aggregated_data = data.groupby('Date')['ConfirmedCases'].sum()

#     # ARIMA model fitting
#     model = ARIMA(aggregated_data, order=(1, 1, 1))
#     result = model.fit()
#     forecast = result.get_forecast(steps=30)
#     forecast_df = forecast.summary_frame()

#     # Calculate the start date for the zoomed-in view based on user input
#     zoom_start_date = aggregated_data.index[-zoom_days]

#     # Visualization (zoomed in)
#     plt.figure(figsize=(12, 6))
#     plt.plot(aggregated_data.index, aggregated_data, label='Actual Cases')
#     plt.plot(forecast_df.index, forecast_df['mean'], label='Forecasted Cases', color='red')
#     plt.fill_between(forecast_df.index, forecast_df['mean_ci_lower'], forecast_df['mean_ci_upper'], color='pink', alpha=0.3)
#     plt.title(f'Zoomed-in: Global Forecast vs Actual Cases (Last {zoom_days} Days)')
#     plt.xlabel('Date')
#     plt.ylabel('Confirmed Cases')
#     plt.xlim([zoom_start_date, forecast_df.index[-1]])  # Set x-axis limits for zoomed-in view
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# if __name__ == "__main__":
#     # Example usage: User can specify the number of days to zoom in
#     plot_zoomed_forecast(zoom_days=90)  # Adjust the number of days as needed

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def plot_pca_analysis(x_max=None, y_max=None):
    """
    Plots the PCA analysis with adjustable x and y limits.

    Parameters:
    x_max (int or float): Maximum value for the x-axis (Principal Component 1).
    y_max (int or float): Maximum value for the y-axis (Principal Component 2).
    """
    
    data = pd.read_csv('data/processed/processed_covid_data.csv')

    features = StandardScaler().fit_transform(data[['NewCases', 'ConfirmedCases']].dropna())

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(features)

    print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")

    plt.figure(figsize=(8, 6))
    plt.scatter(principal_components[:, 0], principal_components[:, 1], alpha=0.7)
    plt.title('PCA of Global COVID-19 Data')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')

    if x_max:
        plt.xlim(-x_max, x_max)
    if y_max:
        plt.ylim(-y_max, y_max)
    
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    
    plot_pca_analysis(x_max=5, y_max=5) 
