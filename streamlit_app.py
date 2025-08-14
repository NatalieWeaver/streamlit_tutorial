import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("state_data.csv")

st.header("Changes in US State Demographics")

# Let user select which state to graph
state = st.selectbox("State:", df["State"].unique())
demographic = st.selectbox("Demographic:", ["Total Population", "Median Household Income"])

tab1, tab2 = st.tabs(["Plot", "Table"])

# Create a graph of demographic
with tab1:
    df_state = df[df["State"] == state]
    fig = px.line(
        df_state, x="Year", y=demographic, title=f"{demographic} of {state}"
    )
    st.plotly_chart(fig)

# Show the entire dataframe
with tab2:
    st.write(f"{state} Data")
    st.dataframe(df_state)
