import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"  # sample API
response = requests.get(url)

if response.status_code == 200:
    print("✅ API call successful!")
    data=response.json()
    print(type(data))
    df = pd.DataFrame(data)
    print(df.head())
else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")