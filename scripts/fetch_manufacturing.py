import pandas as pd
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv"

response = requests.get(url)

if response.status_code == 200:

    df = pd.read_csv(
        StringIO(response.text)
    )

    print(df.head())

    df.to_csv(
        "data/raw/manufacturing.csv",
        index=False
    )

    print("SUCCESS")

else:

    print("Download failed")