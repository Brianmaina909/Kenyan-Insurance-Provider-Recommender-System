import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Display header images
st.image(['Insurers.png'], width=600, use_column_width='auto')

st.markdown("""
    <style>
    .stApp {
        background-color: lightblue;
        color: black;
    }
    h1, h2, h3 {
        font-family: 'Helvetica', sans-serif;
        color: darkblue;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the trained XGBoost model
model = joblib.load('xgboost_model.pkl')

# Load the dataset
df = pd.read_csv('cleaned_data.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Streamlit app
st.title("Insurance Provider Recommender")
st.write("""
This system helps Kenyan customers rate the reliability of insurance providers based on their non-liability claim settlement history.
""")

# User inputs
st.header("Select Insurer and Rating Metrics")

# Insurer selection
insurers = df['Insurer'].unique()
selected_insurer = st.selectbox('Pick Insurer', insurers)

# Year selection
years = df['Date'].dt.year.unique()
selected_year = st.selectbox('Select Year', sorted(years))

# Quarter selection
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
selected_quarter = st.selectbox('Select Quarter', quarters)

# Filter data based on selections
filtered_data = df[(df['Insurer'] == selected_insurer) & (df['Date'].dt.year == selected_year) & (df['Date'].dt.quarter == quarters.index(selected_quarter) + 1)]

if filtered_data.empty:
    st.write("No data available for the selected period.")
else:
    # Extract features for prediction
    features = filtered_data[['Claims_outstanding_at_the_beginning',
                              'Claims_intimated_and_revived',
                              'Claims_revised',
                              'Total_Claims_Payable',
                              'Claims_paid',
                              'Claims_declined',
                              'Claims_closed_as_no_claims',
                              'Total_Claims_Action_during_the_Quarter',
                              'Claims_outstanding_at_the_end',
                              'Claims_declined_ratio_(%)',
                              'Claims_closed_as_no_claims_ratio (%)',
                              'Insurer_Encoded']].values

    # Predict reliability score
    prediction = model.predict(features)
    st.write(f"Predicted Reliability Score for {selected_insurer} in {selected_year} {selected_quarter}: {prediction[0]:.2f}")
