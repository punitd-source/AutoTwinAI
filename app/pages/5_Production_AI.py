import streamlit as st
import numpy as np

st.title(
"Production AI"
)

temperature = st.slider(
"Temperature",
100,
500,
300
)

torque = st.slider(
"Torque",
0,
100,
45
)

cp = round(
    np.random.uniform(
        1.1,
        1.8
    ),
    2
)

cpk = round(
    np.random.uniform(
        0.8,
        1.5
    ),
    2
)

st.metric(
    "Cp",
    cp
)

st.metric(
    "Cpk",
    cpk
)

if cpk < 1:

    st.error(
        "Process Drift Detected"
    )

else:

    st.success(
        "Process Stable"
    )

failure = (

temperature/500

+

torque/100

)/2

st.metric(

"Failure Probability",

f"{failure:.1%}"

)

st.info(

"Operator Guidance: Reduce torque by 5%."

)