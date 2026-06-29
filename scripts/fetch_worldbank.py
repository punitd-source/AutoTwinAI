import requests
import pandas as pd

countries = ["IND","CHN","DEU","USA","JPN","KOR"]

rows=[]

for c in countries:

    url=f"https://api.worldbank.org/v2/country/{c}/indicator/NY.GDP.MKTP.KD.ZG?format=json&per_page=10"

    r=requests.get(url).json()

    value=None

    for entry in r[1]:

        if entry["value"] is not None:
            value=entry["value"]
            break

    rows.append([c,value])

df=pd.DataFrame(
    rows,
    columns=["CountryCode","GDPGrowth"]
)

print(df)

df.to_csv(
"data/raw/worldbank_gdp.csv",
index=False
)