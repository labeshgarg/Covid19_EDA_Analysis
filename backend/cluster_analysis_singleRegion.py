import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv('data/processed/processed_covid_data.csv')
    features = data[['NewCases', 'ConfirmedCases']].dropna()

    kmeans = KMeans(n_clusters=3, random_state=0)
    labels = kmeans.fit_predict(features)

    score = silhouette_score(features, labels)
    print(f"Silhouette Score: {score}")

    plt.figure(figsize=(10, 6))
    plt.scatter(features['NewCases'], features['ConfirmedCases'], c=labels, cmap='viridis')
    plt.title('Global Cluster Analysis')
    plt.xlabel('New Cases')
    plt.ylabel('Confirmed Cases')
    plt.colorbar(label='Cluster Label')
    plt.show()

if __name__ == "__main__":
    main()
