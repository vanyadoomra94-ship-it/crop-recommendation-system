import streamlit as st
import joblib

model = joblib.load("crop_recommendation_model.pkl")

st.title("🌱 Crop Recommendation System")

st.write("Enter the soil and environmental conditions to get a crop recommendation.")

N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)

temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
ph = st.number_input("pH", min_value=0.0, max_value=14.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

if st.button("Recommend Crop"):
    sample = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(sample)

    st.success(f"Recommended Crop: {prediction[0].capitalize()}")
