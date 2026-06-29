import pandas as pd
import numpy as np

days=100

demand=np.random.randint(
100,
400,
days
)

df=pd.DataFrame(
{"Demand":demand}
)

df["Forecast"]=(
df["Demand"]
.rolling(7)
.mean()
)

print(df)