import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("indian_industries.csv")

# Sidebar
selected_industry = st.sidebar.selectbox("Select Industry", df["Industry"].unique())

# Filter data
filtered_df = df[df["Industry"] == selected_industry]

# Show data
st.write("Performance of", selected_industry)
fig = px.line(filtered_df, x="Month", y="Sales")
st.plotly_chart(fig)
