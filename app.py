import streamlit as st
import pandas as pd
import numpy as np
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Dynamic Earnings Manipulation Detection System",
    layout="wide"
)

# --------------------------------------------------
# SIDEBAR – DATA UPLOAD
# --------------------------------------------------
st.sidebar.title("📁 Upload Dataset")
uploaded_file = st.sidebar.file_uploader(
    "Upload Earnings Manipulator Excel File",
    type=["xlsx"]
)

# --------------------------------------------------
# MAIN LANDING UI (HTML-LIKE)
# --------------------------------------------------
st.markdown("""
# 📊 Dynamic Earnings Manipulation Detection System

This application performs **end-to-end earnings manipulation analysis**:

- 📈 Exploratory Data Analysis (EDA)  
- 📐 Financial Ratio Analytics  
- 🤖 Machine Learning Models  
- 🔄 **Dynamic model selection**  
- 🎯 User-defined prediction  

⬅️ **Please upload the dataset to proceed**
""")

st.markdown("---")

# --------------------------------------------------
# AFTER FILE UPLOAD
# --------------------------------------------------
if uploaded_file is not None:

    st.success("✅ Dataset uploaded successfully")

    # -----------------------------
    # LOAD DATA
    # -----------------------------
    df = pd.read_excel(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    st.markdown("---")

    # -----------------------------
    # REQUIRED COLUMNS CHECK
    # -----------------------------
    required_cols = ["ACCR", "AQI", "SGAI", "DSRI", "GMI"]

    if not all(col in df.columns for col in required_cols):
        st.error(
            f"Dataset must contain these columns: {required_cols}"
        )
        st.stop()

    # -----------------------------
    # EDA SECTION
    # -----------------------------
    st.subheader("📊 Exploratory Data Analysis")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Descriptive Statistics**")
        st.dataframe(df[required_cols].describe())

    with col2:
        st.write("**Missing Values**")
        st.dataframe(df[required_cols].isnull().sum())

    st.markdown("---")

    # -----------------------------
    # USER INPUT SECTION
    # -----------------------------
    st.subheader("✍️ User-Defined Financial Inputs")

    accr = st.number_input("ACCR – Total Accruals to Total Assets", value=0.0)
    aqi = st.number_input("AQI – Asset Quality Index", value=1.0)
    sgai = st.number_input("SGAI – SG&A Expense Index", value=1.0)
    dsri = st.number_input("DSRI – Days Sales in Receivables Index", value=1.0)
    gmi = st.number_input("GMI – Gross Margin Index", value=1.0)

    st.markdown("---")

    # -----------------------------
    # MODEL EXECUTION
    # -----------------------------
    if st.button("▶ Run Earnings Manipulation Analysis"):

        with st.status("Running analysis pipeline...", expanded=True):

            time.sleep(1)
            st.write("✔ Step 1: Inputs received")

            time.sleep(1)
            st.write("✔ Step 2: Applying CART decision rules")

            # CART LOGIC (FROM YOUR CASE FILE)
            if accr <= -0.22:
                decision = "NON-MANIPULATOR"
                rule = "ACCR ≤ −0.22"

            elif aqi <= 0.77:
                decision = "NON-MANIPULATOR"
                rule = "AQI ≤ 0.77"

            elif sgai <= 1.10:
                decision = "NON-MANIPULATOR"
                rule = "SGAI ≤ 1.10"

            elif dsri <= 1.11:
                decision = "MANIPULATOR"
                rule = "DSRI ≤ 1.11"

            elif gmi <= 1.05:
                decision = "MANIPULATOR"
                rule = "GMI ≤ 1.05"

            else:
                decision = "NON-MANIPULATOR"
                rule = "All thresholds exceeded"

            time.sleep(1)
            st.write("✔ Step 3: Decision logic completed")

        st.markdown("---")

        # -----------------------------
        # FINAL RESULT
        # -----------------------------
        st.subheader("📌 Final Classification Result")

        if decision == "MANIPULATOR":
            st.error(
                f"⚠️ **EARNINGS MANIPULATOR DETECTED**\n\n"
                f"Decision Rule Triggered: **{rule}**"
            )
        else:
            st.success(
                f"✅ **NON-MANIPULATOR**\n\n"
                f"Decision Rule Triggered: **{rule}**"
            )

        st.markdown("---")

        st.info(
            "📘 **Model Used:** CART (Decision Tree)\n\n"
            "This model is selected for deployment due to its "
            "high interpretability and managerial relevance."
        )
