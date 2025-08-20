import streamlit as st

# --- Helper functions ---
def calculate_met(activity, speed_kmh):
    # Base MET values for walking/running (approximate)
    # Removed body_weight param as it's unused
    if activity in ["Walking", "Walking with Added Weight"]:
        if speed_kmh < 3:
            return 2.0
        elif speed_kmh < 5:
            return 3.5
        elif speed_kmh < 7:
            return 4.3
        else:
            return 5.0
    elif activity == "Running":
        if speed_kmh < 8:
            return 7.0
        elif speed_kmh < 10:
            return 9.8
        else:
            return 11.5
    return 3.5  # fallback

def calculate_calories(met, weight, duration_min):
    # Standard MET formula
    calories_per_min = (met * 3.5 * weight) / 200
    return calories_per_min * duration_min

# --- Streamlit app UI ---
st.title("Weighted Walk Calorie Calculator")

st.sidebar.header("User Info")
age = st.sidebar.number_input("Age (years)", 10, 100, 41)
height = st.sidebar.number_input("Height (cm)", 100, 250, 193)
weight = st.sidebar.number_input("Weight (kg)", 30.0, 250.0, 100.0)

action = st.selectbox(
    "Choose Activity",
    ["Walking", "Running", "Walking with Added Weight"]
)

speed = st.number_input("Average speed (km/h)", 1.0, 20.0, 6.0)
duration = st.number_input("Duration (minutes)", 1, 300, 60)

extra_weight = 0.0
if action == "Walking with Added Weight":
    extra_weight = st.number_input("Extra weight carried (kg)", 1.0, 50.0, 5.0)
    st.info("Note: Walking with added weight should burn MORE calories than regular walking because of the extra effort. If not, check your inputs.")

if st.button("Calculate Calories"):
    if weight <= 0 or (extra_weight < 0 if action == "Walking with Added Weight" else False) or speed <= 0 or duration <= 0:
        st.error("Please enter valid positive values.")
    else:
        # Use walking MET for both walking activities
        met_activity = "Walking" if action == "Walking with Added Weight" else action
        met = calculate_met(met_activity, speed)

        # Use total effective weight for added weight
        effective_weight = weight + extra_weight if action == "Walking with Added Weight" else weight

        # Calculate
        calories = calculate_calories(met, effective_weight, duration)

        # Display
        st.success(f"Estimated calories burned: {calories:.1f} kcal")
        st.caption(f"MET used: {met:.2f} · Effective weight: {effective_weight:.1f} kg")

        # Debug info
        st.write("**Debug Info (to verify logic):**")
        st.write(f"- Selected Activity: {action}")
        st.write(f"- MET Activity Used: {met_activity}")
        st.write(f"- Extra Weight: {extra_weight} kg")
        st.write(f"- Calories per minute: {(met * 3.5 * effective_weight / 200):.2f} kcal")

        # Quick comparison if walking with weight
        if action == "Walking with Added Weight":
            walking_calories = calculate_calories(met, weight, duration)
            st.write(f"**Comparison:** Regular walking (without extra weight) would burn {walking_calories:.1f} kcal for the same inputs.")
