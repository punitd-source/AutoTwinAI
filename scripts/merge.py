import pandas as pd

supplier=pd.read_csv(
"data/raw/supplier.csv"
)

component=pd.read_csv(
"data/raw/component_map.csv"
)

country=pd.read_csv(
"data/raw/worldbank_gdp.csv"
)

master=supplier.merge(
component,
on="Component"
)

print(master)

master.to_csv(
"data/processed/master.csv",
index=False
)