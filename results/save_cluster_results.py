import pandas as pd
from sklearn.cluster import KMeans

def save_cluster_results():
    
    data = pd.read_csv('data/processed/processed_covid_data.csv')
    features = data[['NewCases', 'ConfirmedCases']].dropna()

    kmeans = KMeans(n_clusters=3, random_state=0)
    data['Cluster'] = kmeans.fit_predict(features)

    data[['NewCases', 'ConfirmedCases', 'Cluster']].to_csv('results/cluster_results.csv', index=False)
    print("Cluster results saved to 'results/cluster_results.csv'")

if __name__ == "__main__":
    save_cluster_results()
