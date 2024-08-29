# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score
# import matplotlib.pyplot as plt

# def main():
#     data = pd.read_csv('data/processed/processed_covid_data.csv')
#     features = data[['NewCases', 'ConfirmedCases']].dropna()

#     # KMeans Clustering
#     kmeans = KMeans(n_clusters=3, random_state=0)
#     labels = kmeans.fit_predict(features)

#     # Calculate Silhouette Score for all regions
#     score = silhouette_score(features, labels)
#     print(f"Silhouette Score: {score}")

#     # Plotting
#     plt.figure(figsize=(10, 6))
#     plt.scatter(features['NewCases'], features['ConfirmedCases'], c=labels, cmap='viridis')
#     plt.title('Global Cluster Analysis')
#     plt.xlabel('New Cases')
#     plt.ylabel('Confirmed Cases')
#     plt.colorbar(label='Cluster Label')
#     plt.show()

# if __name__ == "__main__":
#     main()

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def plot_cluster_analysis(x_max=None, y_max=None):
    """
    Plots the cluster analysis with adjustable x and y limits.

    Parameters:
    x_max (int or float): Maximum value for the x-axis (New Cases).
    y_max (int or float): Maximum value for the y-axis (Confirmed Cases).
    """
    
    data = pd.read_csv('data/processed/processed_covid_data.csv')
    
    features = data[['NewCases', 'ConfirmedCases']].dropna()

    # KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    data['Cluster'] = kmeans.fit_predict(features)

    plt.figure(figsize=(10, 6))
    plt.scatter(features['NewCases'], features['ConfirmedCases'], c=data['Cluster'], cmap='viridis')
    plt.title('Global COVID-19 Cluster Analysis')
    plt.xlabel('New Cases')
    plt.ylabel('Confirmed Cases')
    plt.colorbar(label='Cluster')
  
    if x_max:
        plt.xlim(0, x_max)
    if y_max:
        plt.ylim(0, y_max)
    
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    plot_cluster_analysis(x_max=5000, y_max=200000)  
