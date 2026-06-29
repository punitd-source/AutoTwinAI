import pandas as pd
import numpy as np

df=pd.read_csv(
"data/processed/master.csv"
)

df["CountryRisk"]=np.random.rand(
len(df)
)

df["CommodityRisk"]=np.random.rand(
len(df)
)

df["FinalRiskScore"]=(
0.5*df["CountryRisk"]
+
0.5*df["CommodityRisk"]
)

df["SupplierRating"] = np.random.randint(
    1,
    6,
    len(df)
)

df["PaymentDays"] = np.random.randint(
    30,
    120,
    len(df)
)

df["PricingScore"] = np.random.rand(
    len(df)
)

print(df)

df.to_csv(
"data/processed/risk_master.csv",
index=False
)