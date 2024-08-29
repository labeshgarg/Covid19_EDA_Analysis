import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def save_pca_results():
    
    data = pd.read_csv('data/processed/processed_covid_data.csv')
    features = StandardScaler().fit_transform(data[['NewCases', 'ConfirmedCases']].dropna())

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(features)
    explained_variance = pca.explained_variance_ratio_

    pca_df = pd.DataFrame(principal_components, columns=['PC1', 'PC2'])
    pca_df.to_csv('results/pca_results.csv', index=False)
 
    variance_df = pd.DataFrame(explained_variance, columns=['Explained Variance Ratio'])
    variance_df.to_csv('results/pca_explained_variance.csv', index=False)

    print("PCA results saved to 'results/pca_results.csv'")
    print("Explained variance saved to 'results/pca_explained_variance.csv'")

if __name__ == "__main__":
    save_pca_results()
