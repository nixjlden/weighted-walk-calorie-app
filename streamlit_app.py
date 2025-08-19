import streamlit as st
import numpy as np

# --- Helper functions ---
def calculate_met(activity, speed_kmh, extra_weight, body_weight):
    # Base MET values for walking/running (approximate)
    if activity == "Walking":
        if speed_kmh < 3:
            base_met = 2.0
        elif speed_kmh < 5:
            base_met = 3.5
        elif speed_kmh < 7:
            base_met = 4.3
        else:
            base_met = 5.0
    elif activity == "Running":
        if speed_kmh < 8:
            base_met = 7.0
        elif speed_kmh < 10:
            base_met = 9.8
        else:
            base_met = 11.5
    else:
        base_met = 3.5  # default for walking

    # Adjust MET if carrying extra weight
    if activity == "Walking with Added Weight":
        factor = 1 + (extra_weight / body_weight) * 1.5
        return base_met * factor

    return base_met

def calculate_calories(met, weight, duration_min):
    # Standard MET formula
    calories_per_min = (met * 3.5 * weight) / 200
    return calories_per_min * duration_min

# --- Streamlit app UI ---
st.title("Weighted Walk Calorie Calculator")

st.sidebar.header("User Info")
age = st.sidebar.number_input("Age (years)", 10, 100, 41)
height = st.sidebar.number_input("Height (cm)", 100, 250, 175)
weight = st.sidebar.number_input("Weight (kg)", 30.0, 200.0, 70.0)

action = st.selectbox(
    "Choose Activity",
    ["Walking", "Running", "Walking with Added Weight"]
)

speed = st.number_input("Average speed (km/h)", 1.0, 20.0, 6.0)
duration = st.number_input("Duration (minutes)", 1, 300, 60)

extra_weight = 0.0
if action == "Walking with Added Weight":
    extra_weight = st.number_input("Extra weight carried (kg)", 1.0, 50.0, 5.0)

if st.button("Calculate Calories"):
    met = calculate_met(action, speed, extra_weight, weight)
    calories = calculate_calories(met, weight, duration)
    st.success(f"Estimated calories burned: {calories:.1f} kcal")
    st.caption(f"MET used: {met:.2f}")