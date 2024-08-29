#NOT USED
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_data(file_path, x, y, title):
    data = pd.read_csv(file_path)
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x, y=y, data=data)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

# Plotting
plot_data('data/processed/processed_covid_data.csv', 'Date', 'ConfirmedCases', 'COVID-19 Confirmed Cases Over Time')
