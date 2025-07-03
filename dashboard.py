import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 MEC Task Offloading Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV File", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = [col.strip().lower() for col in df.columns]  # Normalize columns

    st.subheader("Preview of Uploaded Data")
    st.write(df.head())

    # Plot Execution Type if available
    if 'assigned' in df.columns:
        st.subheader("Execution Type Distribution")
        st.bar_chart(df['assigned'].value_counts())
    else:
        st.warning("Column 'assigned' not found in this dataset.")

    # Plot Latency if available
    if 'latency_ms' in df.columns:
        st.subheader("Latency Distribution")
        st.bar_chart(df['latency_ms'])

    # Battery plot
    if 'battery_level' in df.columns:
        st.subheader("Battery Level Over Time")
        st.line_chart(df['battery_level'])

    # Task Priority
    if 'priority' in df.columns:
        st.subheader("Task Priority Breakdown")
        st.bar_chart(df['priority'].value_counts())
