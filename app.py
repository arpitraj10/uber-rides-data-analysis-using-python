import streamlit as st
from utils.data_loader import load_data
from utils.preprocessing import preprocess_data
from utils.visualizations import (
    rides_by_hour,
    rides_by_day,
    purpose_distribution
)

st.set_page_config(
    page_title="Uber Rides Dashboard",
    layout="wide"
)

# Title
st.title("Uber Rides Data Analysis Dashboard")

# Load Data
df = load_data("C:\Users\ARPIT RAJPUROHIT\OneDrive\Documents\uber rides data analysis project\data\uber_rides.csv")
df = preprocess_data(df)

# Sidebar Filters
st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df['CATEGORY'].unique(),
    default=df['CATEGORY'].unique()
)

purpose_filter = st.sidebar.multiselect(
    "Select Purpose",
    options=df['PURPOSE'].unique(),
    default=df['PURPOSE'].unique()
)

filtered_df = df[
    (df['CATEGORY'].isin(category_filter)) &
    (df['PURPOSE'].isin(purpose_filter))
]

# KPI Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Rides", len(filtered_df))
col2.metric("Average Miles", round(filtered_df['MILES'].mean(), 2))
col3.metric("Peak Hour", filtered_df['HOUR'].mode()[0])

st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs([
    "Time Analysis",
    "Day Analysis",
    "Purpose Analysis"
])

with tab1:
    st.plotly_chart(rides_by_hour(filtered_df), use_container_width=True)

with tab2:
    st.plotly_chart(rides_by_day(filtered_df), use_container_width=True)

with tab3:
    st.plotly_chart(purpose_distribution(filtered_df), use_container_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Uber Data Analysis")
