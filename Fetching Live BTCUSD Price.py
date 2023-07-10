import requests
import threading
import time


def get_live_price():
    while True:
        try:
            # Send a GET request to the CoinGecko API
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
            response.raise_for_status()  # Raise an exception if the request was unsuccessful

            # Parse the response as JSON
            data = response.json()

            # Extract the live price of Bitcoin
            live_price = data['bitcoin']['usd']

            # Print the live price
            print(f'Live Price: ${live_price}')

        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')

        # Sleep for 5 seconds
        time.sleep(5)


# Create and start the background thread
thread = threading.Thread(target=get_live_price)
thread.daemon = True
thread.start()

# Run the main thread to print the fetched live price
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
