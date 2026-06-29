import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Supply Chain Intelligence",
    layout="wide"
)

st.title(" Supply Chain Control Tower")

# -------------------------
# LOAD DATA
# -------------------------

risk = pd.read_csv(
    "data/processed/risk_master.csv"
)

country_coords = {

    "China":[35.8617,104.1954],
    "Germany":[51.1657,10.4515],
    "India":[20.5937,78.9629],
    "South Korea":[35.9078,127.7669]

}

# -------------------------
# KPI SECTION
# -------------------------

st.subheader("Supply Chain KPIs")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Suppliers",
    len(risk)
)

col2.metric(
    "High Risk Suppliers",
    len(
        risk[
            risk["FinalRiskScore"] > 0.5
        ]
    )
)

col3.metric(
    "Countries",
    risk["Country"].nunique()
)

col4.metric(
    "Critical Commodity",
    "Nickel"
)
# -------------------------
#Geopolitical Dependency
# -------------------------

st.subheader(
    "Geopolitical Dependency"
)

country_dep = (

risk

.groupby("Country")

.size()

.reset_index(
name="Suppliers"
)

)

fig = px.pie(

    country_dep,

    names="Country",

    values="Suppliers",

    title="Supplier Dependency by Country"

)

st.plotly_chart(
    fig,
    width="stretch"
)





# -------------------------
# CRITICAL RISKS
# -------------------------

st.subheader(
    "Critical Supply Chain Risks"
)

highrisk = (

    risk

    .sort_values(
        "FinalRiskScore",
        ascending=False
    )

)

st.dataframe(
    highrisk,
    width="stretch"
)

# -------------------------
# RISK VISUALIZATION
# -------------------------

st.subheader(
    "Supplier Risk Distribution"
)

fig = px.bar(

    risk,

    x="Supplier",

    y="FinalRiskScore",

    color="Country",

    title="Risk Score by Supplier"

)

st.plotly_chart(
    fig,
    width="stretch"
)

# -------------------------
# EVENT SIMULATION
# -------------------------

st.subheader(
    "Disruption Simulator"
)

event = st.selectbox(

    "Choose Supply Chain Event",

    [

        "No Event",

        "China Battery Ban",

        "Copper Shock",

        "Oil Shock",

        "Port Congestion"

    ]

)

risk2 = risk.copy()

if event=="China Battery Ban":

    risk2.loc[
        risk2["Country"]=="China",
        "FinalRiskScore"
    ] += 0.40

if event=="Copper Shock":

    risk2.loc[
        risk2["Commodity"]=="Copper",
        "FinalRiskScore"
    ] += 0.25

if event=="Oil Shock":

    risk2["FinalRiskScore"] += 0.15

if event=="Port Congestion":

    risk2["FinalRiskScore"] += 0.10

# -------------------------
# ALTERNATE SOURCING
# -------------------------

st.subheader(
    "Alternate Supplier Recommendation"
)

component = st.selectbox(

    "Choose Component",

    risk2["Component"].unique()

)

recommend = (

    risk2[
        risk2["Component"]==component
    ]

    .sort_values(
        "FinalRiskScore"
    )

    .head(3)

)

st.dataframe(
    recommend,
    width="stretch"
)

# -------------------------
# SUPPLIER NETWORK
# -------------------------

st.subheader(
    "Supplier–OEM Network"
)

G = nx.Graph()

OEMs = set(
    risk["Buyer"]
)

for _, row in risk.iterrows():

    G.add_edge(
        row["Supplier"],
        row["Buyer"]
    )

fig, ax = plt.subplots(
    figsize=(14,8)
)

pos = nx.spring_layout(
    G,
    seed=42,
    k=2
)

node_colors=[]

for node in G.nodes():

    if node in OEMs:

        node_colors.append(
            "#ff6b6b"
        )

    else:

        node_colors.append(
            "#4dabf7"
        )

nx.draw_networkx_nodes(

    G,

    pos,

    node_size=3500,

    node_color=node_colors,

    alpha=0.95,

    ax=ax

)

nx.draw_networkx_edges(

    G,

    pos,

    width=3,

    edge_color="gray",

    ax=ax

)

nx.draw_networkx_labels(

    G,

    pos,

    font_size=11,

    font_weight="bold",

    ax=ax

)

legend_text = """

OEM = Red Nodes

Supplier = Blue Nodes

"""

ax.text(

    1.02,

    0.95,

    legend_text,

    transform=ax.transAxes,

    fontsize=12,

    verticalalignment='top'

)

ax.set_title(
    "Automotive Supplier–OEM Relationship Map"
)

ax.axis("off")

st.pyplot(fig)

# -------------------------
# GLOBAL MAP
# -------------------------

st.subheader(
    "Global Supplier Footprint"
)

map_df = risk.copy()

map_df["lat"] = map_df["Country"].map(
    lambda x: country_coords[x][0]
)

map_df["lon"] = map_df["Country"].map(
    lambda x: country_coords[x][1]
)

st.pydeck_chart(

    pdk.Deck(

        initial_view_state=pdk.ViewState(

            latitude=25,

            longitude=20,

            zoom=1

        ),

        layers=[

            pdk.Layer(

                "ScatterplotLayer",

                data=map_df,

                get_position='[lon, lat]',

                get_radius=400000,

                get_fill_color='[255,0,0,180]',

                pickable=True

            )

        ]

    )

)

# -------------------------
# RAW DATA TABLE
# -------------------------

st.subheader(
    "Supplier Dataset"
)

st.dataframe(
    risk,
    width="stretch"
)