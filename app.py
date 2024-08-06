import streamlit as st
import xgboost as xgb
import pickle
import pandas as pd

# Load the model
with open('xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app
st.title("XGBoost Model Deployment")

# Collect user input
def user_input_features():
    feature1 = st.sidebar.number_input("Feature 1")
    feature2 = st.sidebar.number_input("Feature 2")
    # Add more features as needed
    data = {
        'feature1': feature1,
        'feature2': feature2,
        # Add more features as needed
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Display user input
st.subheader('User Input:')
st.write(df)

# Make predictions
if st.button('Predict'):
    prediction = model.predict(df)
    st.subheader('Prediction:')
    st.write(prediction)

# If it's a classifier, show predicted probabilities
if isinstance(model, xgb.XGBClassifier):
    if st.button('Predict Probability'):
        prediction_proba = model.predict_proba(df)
        st.subheader('Prediction Probability:')
        st.write(prediction_proba)
