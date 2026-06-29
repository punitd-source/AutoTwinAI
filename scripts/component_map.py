import pandas as pd

mapping=[

["Battery","Nickel"],

["Electronics","Copper"],

["Interior","Plastic"]

]

df=pd.DataFrame(
mapping,
columns=[
"Component",
"Commodity"
]
)

df.to_csv(
"data/raw/component_map.csv",
index=False
)