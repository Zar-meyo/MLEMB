import joblib
import streamlit as st

model = joblib.load("regression.joblib")

size = st.number_input("Size")
bedrooms = st.number_input("Number of bedrooms", min_value=1)
hasGarden = st.number_input("Has a garden", min_value=0, max_value=1, step=1)

prediction = model.predict([[size, bedrooms, hasGarden]])

st.write(f"prediction: {prediction}")