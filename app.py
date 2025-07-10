import streamlit as st
import pickle
import numpy as np

st.title("Home Energy Consumption Predictor")
st.write("Enter your home parameters to predict total energy consumption.")

# Load the trained RandomForestRegressor model
with open("energy_saver_model.pkl", "rb") as f:
    model = pickle.load(f)

# User input fields
appliance_usage = st.number_input("Appliance Usage (kWh)", min_value=0.0, value=5.0)
light_usage = st.number_input("Light Usage (hours)", min_value=0.0, max_value=24.0, value=6.0)
ac_hours = st.number_input("AC Usage (hours)", min_value=0.0, max_value=24.0, value=4.0)
heater_hours = st.number_input("Heater Usage (hours)", min_value=0.0, max_value=24.0, value=2.0)
temperature = st.number_input("Temperature (°C)", min_value=-20.0, max_value=50.0, value=22.0)

# Prepare input for prediction
# Feature order: ['appliance_usage_kwh', 'light_usage_hours', 'ac_usage_hours', 'heater_usage_hours', 'temperature']
data = np.array([[appliance_usage, light_usage, ac_hours, heater_hours, temperature]])

if st.button("Predict Energy Consumption"):
    prediction = model.predict(data)[0]
    st.success(f"Predicted Total Energy Consumption: {prediction:.2f} kWh")

    # Suggestions based on high usage
    suggestions = []
    if appliance_usage > 10:
        suggestions.append("Reduce appliance usage where possible.")
    if light_usage > 8:
        suggestions.append("Reduce light usage hours.")
    if ac_hours > 8:
        suggestions.append("Consider reducing AC usage hours.")
    if heater_hours > 8:
        suggestions.append("Consider reducing heater usage hours.")
    if temperature > 28:
        suggestions.append("Try to keep indoor temperature moderate.")
    if suggestions:
        st.warning("Suggestions to save energy:")
        for s in suggestions:
            st.write(f"- {s}")
    else:
        st.info("Your usage is within normal range.")