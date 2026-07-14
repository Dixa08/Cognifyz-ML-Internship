# ==========================================
# Restaurant Rating Prediction System
# Cognifyz ML Internship
# Developed by: Dixa
# ==========================================

import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Restaurant Rating Predictor",
    page_icon="🍽️",
    layout="wide"
)

# -------------------------------------------------
# Load Model & Dataset
# -------------------------------------------------
model = joblib.load("models/restaurant_rating_model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

df = pd.read_csv("data/Dataset.csv")

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.title("🍽 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "🏠 Home",
        "🤖 Predict Rating",
        "📊 Model Performance",
        "👩‍💻 About"
    ]
)

# =====================================================
# HOME PAGE
# =====================================================

if page == "🏠 Home":

    st.title("🍽 Restaurant Rating Prediction System")

    st.markdown("""
    ### Welcome 👋

    This application predicts the **Aggregate Rating**
    of restaurants using a Machine Learning model.

    **Internship:** Cognifyz Technologies

    **Algorithm Used:** Random Forest Regressor
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Dataset Size",
            "9551"
        )

    with col2:
        st.metric(
            "Features",
            "13"
        )

    with col3:
        st.metric(
            "Best Model",
            "Random Forest"
        )

    st.divider()

    st.subheader("📌 Project Workflow")

    st.markdown("""
    ✅ Data Collection

    ✅ Data Cleaning

    ✅ Exploratory Data Analysis

    ✅ Feature Engineering

    ✅ Model Training

    ✅ Model Evaluation

    ✅ Prediction
    """)


# =====================================================
# MODEL PERFORMANCE
# =====================================================

elif page == "📊 Model Performance":

    st.title("📊 Model Performance")

    result = pd.DataFrame({
        "Model":[
            "Linear Regression",
            "Decision Tree",
            "Random Forest"
        ],
        "R² Score":[
            0.303,
            0.923,
            0.962
        ],
        "RMSE":[
            1.259,
            0.420,
            0.296
        ]
    })

    st.dataframe(
        result,
        use_container_width=True
    )

    st.success("✅ Random Forest achieved the highest accuracy.")

# =====================================================
# PREDICTION PAGE
# =====================================================

elif page == "🤖 Predict Rating":

    st.title("🤖 Predict Restaurant Rating")

    # Select Restaurant
    restaurant = st.selectbox(
        "Select Restaurant",
        sorted(df["Restaurant Name"].unique())
    )

    # Show restaurant details
    row = df[df["Restaurant Name"] == restaurant].iloc[0]

    st.subheader("Restaurant Details")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**City:**", row["City"])
        st.write("**Cuisine:**", row["Cuisines"])
        st.write("**Average Cost for Two:**", row["Average Cost for two"])
        st.write("**Price Range:**", row["Price range"])

    with col2:
        st.write("**Votes:**", row["Votes"])
        st.write("**Table Booking:**", row["Has Table booking"])
        st.write("**Online Delivery:**", row["Has Online delivery"])

    if st.button("🔮 Predict Rating"):

        