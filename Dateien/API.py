import requests
from datetime import datetime as dt

url = "https://openexchangerates.org/api/latest.json?app_id=..." # Daten entfernt
r = requests.get(url)

dict1 = r.json()

time = dt.fromtimestamp(dict1["timestamp"])
print (f"Datum: {time}")
print (f"1$ in € = {dict1['rates']['EUR']}")
