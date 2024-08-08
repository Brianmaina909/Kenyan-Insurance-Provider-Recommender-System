import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Background image and custom styles
st.markdown("""
<style>
.stApp {
    background-image: url("https://www.google.com/imgres?q=insurance%20companies%20in%20kenya&imgurl=https%3A%2F%2Fkenyanwallstreet.com%2Fwp-content%2Fuploads%2F2018%2F09%2Finsurance-companies-in-kenya.jpg&imgrefurl=https%3A%2F%2Fkenyanwallstreet.com%2Fafricas-insurance-premiums-set-to-go-up-report-indicates%2Finsurance-companies-in-kenya%2F&docid=LAJmeS047AaKRM&tbnid=3lhdsYBheaV7LM&vet=12ahUKEwi0xZCqlOaHAxVym_0HHf_zEbQQM3oECFkQAA..i&w=750&h=350&hcb=2&ved=2ahUKEwi0xZCqlOaHAxVym_0HHf_zEbQQM3oECFkQAA");
    background-size: cover;
    color: white;
}
h1, h2, h3 {
    font-family: 'Arial', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Load the trained XGBoost model
model = joblib.load('xgboost_model.pkl')

# Load the dataset
df = pd.read_csv('cleaned_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Streamlit app
st.title("🌟 Insurance Provider Recommender")
st.write("""
This system helps Kenyan customers find reliable insurance providers based on their non-liability claim settlement history.
""")

# User inputs
st.header("Input Data")

# Insurer selection
insurers = df['Insurer'].unique()
selected_insurer = st.selectbox('Select Insurer', insurers)

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
    prediction = model.predict(features)
    st.write(f"Predicted Reliability Score for {selected_insurer} in {selected_year} {selected_quarter}: **{prediction[0]:.2f}**")
