import requests
import pandas as pd
import xlwings as xw

url = "https://www.nseindia.com/api/option-chain-equities?symbol=RELIANCE"
headers = {"Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "en-US,en;q=0.9,gu;q=0.8",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

}

session = requests.Session()
data = session.get(url, headers=headers).json()["records"]["data"]

ocdata = []
for i in data:
    for j, k in i.items():
        if j == "CE" or j == "PE":
            info = k
            info["instrumentType"] = j
            ocdata.append(info)
df = pd.DataFrame(ocdata)
wb = xw.Book("option_chain.xlsx")
st = wb.sheets("reliance")
st.range("A1").value = df

print(df)
