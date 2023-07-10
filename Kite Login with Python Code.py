import requests
import json
def login(request):
    url = "https://kite.zerodha.com/api/login"

    payload = {
        "user_id": "MANTHA",
        "password": "7722331",
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

    print(response.json())



