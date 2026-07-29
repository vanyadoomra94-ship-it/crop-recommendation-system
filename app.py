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
    "Pea": {
        "Crop": "Pea",
        "Scientific Name": "Pisum sativum L.",
        "Reference Condition": "Requirements vary by variety, soil, climate, and production system",
        "Nitrogen (N)": "Varies with soil test and crop management",
        "Phosphorus (P)": "Varies with soil test and crop management",
        "Potassium (K)": "Varies with soil test and crop management",
        "Temperature": "Approximately 10–25°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Moderate moisture is generally required",
        "Soil": "Well-drained loamy soil is generally suitable"
    },

    "Pigeon Pea": {
        "Crop": "Pigeon Pea",
        "Scientific Name": "Cajanus cajan (L.) Millsp.",
        "Reference Condition": "Usually grown under rainfed conditions; requirements vary by variety and region",
        "Nitrogen (N)": "Varies with soil test and production system",
        "Phosphorus (P)": "Varies with soil test and production system",
        "Potassium (K)": "Varies with soil test and production system",
        "Temperature": "Warm growing conditions",
        "Soil pH": "Approximately 6.5–7.5",
        "Rainfall": "Moderate rainfall; sensitive to waterlogging",
        "Soil": "Well-drained loamy or alluvial soil is generally suitable"
    },

    "Black Gram": {
        "Crop": "Black Gram",
        "Scientific Name": "Vigna mungo (L.) Hepper",
        "Reference Condition": "Requirements vary by variety, soil, climate, and season",
        "Nitrogen (N)": "Varies with soil test and crop management",
        "Phosphorus (P)": "Varies with soil test and crop management",
        "Potassium (K)": "Varies with soil test and crop management",
        "Temperature": "Approximately 25–35°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 35–75 cm",
        "Soil": "Well-drained loamy to sandy-loam soil"
    },

    "Green Gram": {
        "Crop": "Green Gram",
        "Scientific Name": "Vigna radiata (L.) R. Wilczek",
        "Reference Condition": "Requirements vary by variety, soil, climate, and season",
        "Nitrogen (N)": "Varies with soil test and crop management",
        "Phosphorus (P)": "Varies with soil test and crop management",
        "Potassium (K)": "Varies with soil test and crop management",
        "Temperature": "Approximately 25–35°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 35–75 cm",
        "Soil": "Well-drained sandy-loam to loamy soil"
    },

    "Groundnut": {
        "Crop": "Groundnut",
        "Scientific Name": "Arachis hypogaea L.",
        "Reference Condition": "Requirements vary by variety, soil, climate, and production system",
        "Nitrogen (N)": "Varies with soil test and crop management",
        "Phosphorus (P)": "Varies with soil test and crop management",
        "Potassium (K)": "Varies with soil test and crop management",
        "Temperature": "Approximately 25–30°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 50–100 cm",
        "Soil": "Well-drained sandy-loam or loamy soil"
    },

    "Mustard": {
        "Crop": "Mustard",
        "Scientific Name": "Brassica juncea L.",
        "Reference Condition": "Requirements vary by variety, soil test, climate, and region",
        "Nitrogen (N)": "Varies with soil test and production system",
        "Phosphorus (P)": "Varies with soil test and production system",
        "Potassium (K)": "Varies with soil test and production system",
        "Temperature": "Approximately 10–25°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 35–60 cm",
        "Soil": "Well-drained loamy soil is generally suitable"
    },

    "Sunflower": {
        "Crop": "Sunflower",
        "Scientific Name": "Helianthus annuus L.",
        "Reference Condition": "Requirements vary by hybrid, soil, climate, and production system",
        "Nitrogen (N)": "Varies with soil test and production system",
        "Phosphorus (P)": "Varies with soil test and production system",
        "Potassium (K)": "Varies with soil test and production system",
        "Temperature": "Approximately 20–30°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 40–75 cm",
        "Soil": "Well-drained loamy soil is generally suitable"
    },

    "Soybean": {
        "Crop": "Soybean",
        "Scientific Name": "Glycine max (L.) Merr.",
        "Reference Condition": "Requirements vary by variety, soil test, climate, and production system",
        "Nitrogen (N)": "Varies with soil test and biological nitrogen fixation",
        "Phosphorus (P)": "Varies with soil test and production system",
        "Potassium (K)": "Varies with soil test and production system",
        "Temperature": "Approximately 20–30°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Approximately 45–75 cm",
        "Soil": "Well-drained loamy soil is generally suitable"
    },

    "Kidney Beans": {
        "Crop": "Kidney Beans",
        "Scientific Name": "Phaseolus vulgaris L.",
        "Reference Condition": "Requirements vary by variety, soil, climate, and production system",
        "Nitrogen (N)": "Varies with soil test and crop management",
        "Phosphorus (P)": "Varies with soil test and crop management",
        "Potassium (K)": "Varies with soil test and crop management",
        "Temperature": "Approximately 18–25°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "Moderate, well-distributed moisture is generally required",
        "Soil": "Well-drained loamy soil is generally suitable"
    },

    "Moth Beans": {
        "Crop": "Moth Beans",
        "Scientific Name": "Vigna aconitifolia (Jacq.) Marechal",
        "Reference Condition": "A drought-tolerant pulse crop; requirements vary by variety and region",
        "Nitrogen (N)": "Varies with soil test and crop management",
        "Phosphorus (P)": "Varies with soil test and crop management",
        "Potassium (K)": "Varies with soil test and crop management",
        "Temperature": "Approximately 25–35°C",
        "Soil pH": "Approximately 6.0–8.0",
        "Rainfall": "Low to moderate rainfall conditions are generally suitable",
        "Soil": "Well-drained sandy or sandy-loam soil"
    },

    "Coconut": {
        "Crop": "Coconut",
        "Scientific Name": "Cocos nucifera L.",
        "Reference Condition": "Requirements vary by variety, soil, climate, and plantation management",
        "Nitrogen (N)": "Varies with soil testing and plantation management",
        "Phosphorus (P)": "Varies with soil testing and plantation management",
        "Potassium (K)": "Varies with soil testing and plantation management",
        "Temperature": "Approximately 20–32°C",
        "Soil pH": "Approximately 5.5–7.5",
        "Rainfall": "High and well-distributed moisture is generally preferred",
        "Soil": "Deep, well-drained soils with good moisture retention"
    },

    "Coffee": {
        "Crop": "Coffee",
        "Scientific Name": "Coffea spp.",
        "Reference Condition": "Requirements vary considerably by coffee species, variety, altitude, and region",
        "Nitrogen (N)": "Varies with soil testing and plantation management",
        "Phosphorus (P)": "Varies with soil testing and plantation management",
        "Potassium (K)": "Varies with soil testing and plantation management",
        "Temperature": "Moderate, species-dependent conditions",
        "Soil pH": "Approximately 5.5–6.5",
        "Rainfall": "Moderate to high, well-distributed rainfall",
        "Soil": "Deep, fertile, well-drained soil rich in organic matter"
    },

    "Jute": {
        "Crop": "Jute",
        "Scientific Name": "Corchorus spp.",
        "Reference Condition": "Requirements vary by species, variety, soil, climate, and region",
        "Nitrogen (N)": "Varies with soil test and production system",
        "Phosphorus (P)": "Varies with soil test and production system",
        "Potassium (K)": "Varies with soil test and production system",
        "Temperature": "Approximately 24–35°C",
        "Soil pH": "Approximately 6.0–7.5",
        "Rainfall": "High rainfall and moisture are generally preferred",
        "Soil": "Fertile, well-drained loamy to alluvial soil"
    },
}
if mode == "Check Crop Requirements":

    st.subheader("🌾 Select a Crop")

    selected_crop = st.selectbox(
        "Which crop do you want to grow?",
        list(crop_requirements.keys())
    )

    requirements = crop_requirements[selected_crop]

    st.success(
        f"🌾 Planning to grow {selected_crop}? "
        "Here are the general soil and environmental requirements."
    )

    st.header(f"🌱 {selected_crop} Growing Requirements")

    st.caption(
        "General agricultural reference information. "
        "Actual nutrient needs can vary with soil, variety, climate, and farming conditions."
    )

    col1, col2, col3 = st.columns(3)

    st.markdown("### 🌱 Nutrient Requirements")

    nutrients = [
        ("Nitrogen (N)", requirements.get("Nitrogen (N)", "Not available")),
        ("Phosphorus (P)", requirements.get("Phosphorus (P)", "Not available")),
        ("Potassium (K)", requirements.get("Potassium (K)", "Not available"))
    ]

    for i, (name, value) in enumerate(nutrients):
        with [col1, col2, col3][i]:
            st.metric(name, value)

    st.markdown("### 🌦️ Environmental Requirements")

    col4, col5 = st.columns(2)

    with col4:
        st.info(
            f"🌡️ **Temperature**\n\n"
            f"{requirements.get('Temperature', 'Not available')}"
        )

        st.info(
            f"🧪 **Soil pH**\n\n"
            f"{requirements.get('Soil pH', 'Not available')}"
        )

    with col5:
        st.info(
            f"🌧️ **Rainfall**\n\n"
            f"{requirements.get('Rainfall', 'Not available')}"
        )

        st.info(
            f"🌾 **Suitable Soil**\n\n"
            f"{requirements.get('Soil', 'Not available')}"
        )

    st.markdown("### 📌 Reference Condition")

    st.write(
        requirements.get(
            "Reference Condition",
            "Conditions vary depending on crop and location."
        )
    )









st.markdown("### 📌 Reference Condition")

st.write(
    requirements.get(
        "Reference Condition",
        "Conditions vary depending on crop and location."
    )
)

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
