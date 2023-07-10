import requests
import pandas as pd
import pytz

# Define the API endpoint URL
url = "https://api-testnet.bybit.com/v5/market/mark-price-kline?category=inverse&symbol=BTCUSD&interval=15&start=1609483705&end=1672555705"

# Send the API request and retrieve the response
response = requests.get(url)
response_data = response.json()

print(response_data)
# Extract the data from the API response
data = response_data["result"]["list"]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close"])

# Convert the "timestamp" column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms").dt.tz_localize("UTC")

#Converting the timestamp column into IST Zone

ist_tz = pytz.timezone("Asia/Kolkata")
df["timestamp"] = df["timestamp"].dt.tz_convert(ist_tz)

# Set the "timestamp" column as the DataFrame index
df.set_index("timestamp", inplace=True)

print(df)