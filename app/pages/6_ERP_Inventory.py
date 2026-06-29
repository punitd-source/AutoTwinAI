import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title(
" ERP Inventory"
)

days = 60

demand = np.random.randint(
100,
400,
days
)

df = pd.DataFrame({

"Day":range(days),

"Demand":demand

})

df["Forecast"]=(

df["Demand"]

.rolling(7)

.mean()

)

inventory = 1200

st.metric(
    "Inventory",
    inventory
)

if inventory<1500:

    st.warning(
        "ERP Reorder Triggered"
    )

fig = px.line(

    df,

    x="Day",

    y=["Demand","Forecast"]

)

st.plotly_chart(
    fig,
    width="stretch"
)