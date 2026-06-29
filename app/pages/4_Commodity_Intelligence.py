import streamlit as st
import pandas as pd
import plotly.express as px

st.title(
    "Commodity Intelligence"
)

oil = pd.read_csv(
    "data/raw/oil.csv"
)

print(oil.columns)

oil.reset_index(
    inplace=True
)

fig = px.line(

    oil,

    x="index",

    y="Close",

    title="Oil Price Trend"

)

st.plotly_chart(
    fig,
    width="stretch"
)


st.subheader(
"Material Substitution"
)

material_df = pd.DataFrame({

"Original":[
"Nickel",
"Copper",
"Steel"
],

"Alternative":[
"LFP Battery",
"Aluminum Wiring",
"Composite Alloy"
]

})

st.dataframe(
    material_df
)