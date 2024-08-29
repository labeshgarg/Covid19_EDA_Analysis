import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def main():
    # Load data and filter for Afghanistan
    data = pd.read_csv('data/processed/processed_covid_data.csv')
    data = data[data['Country/Region'] == 'Afghanistan']

    features = StandardScaler().fit_transform(data[['NewCases', 'ConfirmedCases']].dropna())

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(features)

    print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")

    plt.figure(figsize=(8, 6))
    plt.scatter(principal_components[:, 0], principal_components[:, 1], alpha=0.7)
    plt.title('PCA for Afghanistan')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()

if __name__ == "__main__":
    main()
