import streamlit as st
from utils import load, box, ghi, score, monthly

# File paths
file_map = {
    "Benin": r"https://drive.google.com/uc?export=download&id=1m6Ph3OP7LkRBHnKZBeb-h9AKXypqioNk",
    "Sierra Leone": r"https://drive.google.com/uc?export=download&id=1xTSguWTLZA-h3UR2Zl3WRV80wKcE9vaa",
    "Togo": r"https://drive.google.com/uc?export=download&id=1Kowv-VIvGS1NARZEeEkrtmOPP1bmcjH9"
}

# Sidebar options
st.sidebar.header("Sidebar of Solar Data")
selected_country = st.sidebar.selectbox("Select a country", list(file_map.keys()))
st.sidebar.header("Check the box")
show_ghi = st.sidebar.checkbox("Show Average GHI Summary")
show_score = st.sidebar.checkbox("Show Investment Score Summary")
show_monthly = st.sidebar.checkbox("Show Monthly Average GHI Line Chart")

# Main body title
st.title("Solar Data Analysis Dashboard")
st.markdown("The dashboard provides insights into solar resource metrics (GHI, DNI, DHI) and investment priorities across selected countries.")
st.markdown("The default selected country is benin.")

# Load selected country data
df = load(file_map[selected_country])
df["Country"] = selected_country

# Display data
st.subheader(f"Data for {selected_country}")
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
