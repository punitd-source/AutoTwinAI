import pandas as pd

data=[

["CATL","Tesla","China","Battery"],

["Bosch","Toyota","Germany","Electronics"],

["LG Energy","GM","South Korea","Battery"],

["Tata AutoComp","Toyota","India","Interior"]

]

df=pd.DataFrame(
data,
columns=[
"Supplier",
"Buyer",
"Country",
"Component"
]
)

df.to_csv(
"data/raw/supplier.csv",
index=False
)