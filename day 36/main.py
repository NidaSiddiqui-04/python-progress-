import requests
stock_api_key="DGA7VHW4VCDJA2YC"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=stock_api_key'
r = requests.get(url)
data = r.json()

print(data)

