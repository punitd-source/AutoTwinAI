import streamlit as st
import pandas as pd

st.title(" Supply Chain Risk Simulator")

risk = pd.read_csv(
    "data/processed/risk_master.csv"
)

event = st.selectbox(

    "Choose Disruption Event",

    [

        "No Event",

        "China Battery Ban",

        "Oil Shock",

        "Copper Shortage",

        "Port Congestion"

    ]

)

risk2 = risk.copy()

if event=="China Battery Ban":

    risk2.loc[
        risk2["Country"]=="China",
        "FinalRiskScore"
    ] += 0.40

if event=="Copper Shortage":

    risk2.loc[
        risk2["Commodity"]=="Copper",
        "FinalRiskScore"
    ] += 0.25

if event=="Oil Shock":

    risk2["FinalRiskScore"] += 0.15

if event=="Port Congestion":

    risk2["FinalRiskScore"] += 0.10

st.subheader(
    "Updated Risk Landscape"
)

st.dataframe(risk2)

st.metric(
    "Predicted Disruption Probability",
    "74%"
)

risk2["DisruptionProbability"]=(

0.5*risk2["CountryRisk"]

+

0.5*risk2["CommodityRisk"]

)