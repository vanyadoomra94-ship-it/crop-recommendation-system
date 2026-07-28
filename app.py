import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

# Load model
model = joblib.load("crop_recommendation_model.pkl")

# Title
st.title("🌱 Crop Recommendation System")
mode = st.radio(
    "What would you like to do?",
    ["Recommend a Crop", "Check Crop Requirements"]
)
if mode == "Check Crop Requirements":

    st.subheader("🌾 Select a Crop")

    selected_crop = st.selectbox(
        "Which crop do you want to grow?",
        [
            "Wheat",
            "Rice",
            "Maize",
            "Cotton",
            "Sugarcane",
            "Barley",
            "Millet",
            "Chickpea",
            "Lentil",
            "Pea",
            "Pigeon Pea",
            "Black Gram",
            "Green Gram",
            "Groundnut",
            "Mustard",
            "Sunflower",
            "Soybean",
            "Kidney Beans",
            "Moth Beans",
            "Coconut",
            "Coffee",
            "Jute"
        ]
    )

    st.write("You selected:", selected_crop)
crop_requirements = {
    "Wheat": {
        "Crop": "Wheat",
        "Scientific Name": "Triticum aestivum",
        "Reference Condition": "HD 3226, timely-sown and irrigated conditions",
        "Nitrogen (N)": "150 kg/ha (ICAR reference)",
        "Phosphorus (P)": "80 kg/ha (ICAR reference)",
        "Potassium (K)": "60 kg/ha (ICAR reference)",
        "Temperature": "Cool growing conditions",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 30–90 cm",
        "Soil": "Well-drained loamy soil is generally suitable"
    },

    "Rice": {
        "Crop": "Rice",
        "Scientific Name": "Oryza sativa L.",
        "Reference Condition": "Varies by variety, soil, water availability, and cultivation system",
        "Nitrogen (N)": "Requirement varies with soil test and cultivation system",
        "Phosphorus (P)": "Requirement varies with soil test and cultivation system",
        "Potassium (K)": "Requirement varies with soil test and cultivation system",
        "Temperature": "Approximately 20–35°C",
        "Soil pH": "Approximately 5.5–7.0",
        "Rainfall": "High water availability is generally required",
        "Soil": "Clayey to loamy soils with good water-holding capacity"
    },

    "Maize": {
        "Crop": "Maize",
        "Scientific Name": "Zea mays L.",
        "Reference Condition": "Varies by variety, soil test, climate, and cultivation system",
        "Nitrogen (N)": "Requirement varies with soil test and production system",
        "Phosphorus (P)": "Requirement varies with soil test and production system",
        "Potassium (K)": "Requirement varies with soil test and production system",
        "Temperature": "Approximately 18–27°C",
        "Soil pH": "Approximately 5.5–7.5",
        "Rainfall": "Approximately 50–100 cm",
        "Soil": "Well-drained fertile loamy soil is generally suitable"
    },
    "Cotton": {
        "Crop": "Cotton",
        "Scientific Name": "Gossypium spp.",
        "Reference Condition": "Requirements vary by species, variety, soil, and region",
        "Nitrogen (N)": "Requirement varies with soil testing and production system",
        "Phosphorus (P)": "Requirement varies with soil testing and production system",
        "Potassium (K)": "Important nutrient; requirement varies with soil and crop conditions",
        "Temperature": "Approximately 21–30°C",
        "Soil pH": "Approximately 5.5–8.0",
        "Rainfall": "Approximately 50–100 cm",
        "Soil": "Well-drained fertile loamy or black soils are generally suitable"
    },

    "Sugarcane": {
        "Crop": "Sugarcane",
        "Scientific Name": "Saccharum officinarum",
        "Reference Condition": "Requirements vary by variety, soil, climate, and irrigation",
        "Nitrogen (N)": "Requirement varies with soil testing and production system",
        "Phosphorus (P)": "Requirement varies with soil testing and production system",
        "Potassium (K)": "Important nutrient; requirement varies with soil and crop conditions",
        "Temperature": "Approximately 20–35°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 75–150 cm",
        "Soil": "Deep, fertile, well-drained loamy soil is generally suitable"
    },

    "Barley": {
        "Crop": "Barley",
        "Scientific Name": "Hordeum vulgare L.",
        "Reference Condition": "Requirements vary by variety, soil test, climate, and production system",
        "Nitrogen (N)": "Requirement varies with soil testing and production system",
        "Phosphorus (P)": "Requirement varies with soil testing and production system",
        "Potassium (K)": "Requirement varies with soil testing and production system",
        "Temperature": "Approximately 12–25°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 30–60 cm",
        "Soil": "Well-drained loamy soil is generally suitable"
    },
}

requirements = crop_requirements[selected_crop]

st.subheader(f"🌱 {selected_crop} Requirements")

col1, col2 = st.columns(2)

items = list(requirements.items())

for i, (parameter, value) in enumerate(items):
    with col1 if i % 2 == 0 else col2:
        st.info(f"**{parameter}**\n\n{value}")

st.warning(
    "These are agricultural reference values, not a fertilizer prescription. "
    "Actual nutrient requirements depend on soil testing, variety, location, "
    "irrigation, and local agricultural recommendations."
)

st.write(
    "Enter the soil and environmental conditions below "
    "to get a suitable crop recommendation."
)

st.divider()

# Soil parameters
st.subheader("🌾 Soil Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        help="Nitrogen content in the soil"
    )

with col2:
    P = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        help="Phosphorus content in the soil"
    )

with col3:
    K = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        help="Potassium content in the soil"
    )

# Environmental parameters
st.subheader("🌤️ Environmental Parameters")

col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input(
        "Temperature (°C)",
        help="Average temperature"
    )

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        help="Relative humidity"
    )

with col2:
    ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        help="Soil acidity/alkalinity"
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        help="Expected rainfall"
    )

st.divider()

# Prediction
if st.button("🌱 Recommend Crop", use_container_width=True):

    sample = [[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]]

    prediction = model.predict(sample)

    crop = prediction[0].capitalize()

    st.success(f"🌾 Recommended Crop: **{crop}**")

    st.info(
        "This recommendation is generated using a "
        "Random Forest machine learning model."
    )

st.divider()

st.caption("Machine Learning Project • Random Forest • 99.3% Test Accuracy")
