import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/processed/processed_covid_data.csv')
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  
data.dropna(subset=['Date'], inplace=True)  
data.set_index('Date', inplace=True)

print(data.head())
print("Date Range:", data.index.min(), data.index.max())

plt.figure(figsize=(10, 5))
plt.plot(data.index, data['ConfirmedCases'], marker='o', linestyle='-')
plt.title('Check Date Parsing')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
