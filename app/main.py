
import streamlit as st
import pandas as pd
from utils import load, box, ghi, score, monthly

# File paths
file_map = {
    "Benin": r"C:\Users\gasha\Desktop\solar-challenge-week0\data\benin_clean.csv",
    "Sierra Leone": r"C:\Users\gasha\Desktop\solar-challenge-week0\data\sierraleone_clean.csv",
    "Togo": r"C:\Users\gasha\Desktop\solar-challenge-week0\data\togo_clean.csv"
}

# Sidebar
st.sidebar.header("Options")
selected_country = st.sidebar.selectbox("Choose a country", list(file_map.keys()))
show_ghi = st.sidebar.checkbox("Show Average GHI Summary")
show_score = st.sidebar.checkbox("Show Investment Score Summary")
show_monthly = st.sidebar.checkbox("Show Monthly Average GHI Line Chart")

# Load selected country data
df = load(file_map[selected_country])
df["Country"] = selected_country

# Display data
st.title(f"Data for {selected_country}")
st.dataframe(df)

# Boxplots
metrics = ['GHI', 'DNI', 'DHI']
st.subheader("Metric Distributions")
for fig in box(df, metrics):
    st.pyplot(fig)

# Prepare all data for combined charts
all_dfs = []
for country, path in file_map.items():
    temp_df = load(path)
    temp_df["Country"] = country
    all_dfs.append(temp_df)

# Average GHI Summary
if show_ghi:
    st.subheader("Average GHI by Country")
    st.pyplot(ghi(all_dfs))

# Investment Score Summary
if show_score:
    st.subheader("Strategic Investment Priority by Country")
    st.pyplot(score(all_dfs))

# Monthly Average GHI Line Chart
if show_monthly:
    st.subheader("Monthly Average GHI by Country")
    st.pyplot(monthly(all_dfs))
