import requests

def download_data(url, path):
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)
    print(f"Data downloaded to {path}")

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
path = 'data/raw/time_series_covid19_confirmed_global.csv'
download_data(url, path)
