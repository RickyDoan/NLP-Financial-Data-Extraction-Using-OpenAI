import streamlit as st
from helper import extract_financial_data

# Streamlit UI
st.title("Financial Data Extractor")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Enter News Article")
    user_input = st.text_area("Paste the financial news article here:", height=150)

with col2:
    st.subheader("Extracted Financial Data")
    if user_input:  # Only process if user enters text
        df = extract_financial_data(user_input)
        st.table(df)
    else:
        st.write("Waiting for input...")