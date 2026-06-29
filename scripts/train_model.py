import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(
    "data/raw/manufacturing.csv"
)

print(df.head())

X = df[
[
"cylinders",
"displacement",
"horsepower",
"weight"
]
]

y = df["mpg"]

X_train,X_test,y_train,y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

model = RandomForestRegressor()

model.fit(
    X_train,
    y_train
)

score=model.score(
    X_test,
    y_test
)

print("R² Score:",score)