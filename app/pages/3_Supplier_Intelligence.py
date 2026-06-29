import streamlit as st
import pandas as pd

st.title(
"Supplier Intelligence"
)

risk = pd.read_csv(
    "data/processed/risk_master.csv"
)

component = st.selectbox(

    "Choose Component",

    risk["Component"].unique()

)

subset = risk[
    risk["Component"]==component
]

st.subheader(
"Available Suppliers"
)

st.dataframe(subset)

st.subheader(
"Recommended Low-Risk Suppliers"
)

recommend = (

subset

.sort_values(
"FinalRiskScore"
)

.head(3)

)

st.dataframe(recommend)