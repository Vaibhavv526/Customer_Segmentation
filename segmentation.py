import pandas as pd
import numpy as np
import streamlit as st
import joblib

# -------------------- LOAD MODELS SAFELY --------------------
try:
    kmeans = joblib.load('kmeans_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -------------------- UI --------------------
st.title("Customer Segmentation Web App")
st.write("Enter Customer Details to predict the segment")

# -------------------- INPUTS --------------------
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Income", min_value=0, max_value=200000, value=50000)
total_spending = st.number_input("Total Spending", min_value=0, max_value=200000, value=50000)
store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=100, value=10)
web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=100, value=10)
web_visits = st.number_input("Number of Web Visits per Month", min_value=0, max_value=100, value=2)

# -------------------- CREATE INPUT DATA --------------------
input_data = pd.DataFrame({
    'Age': [age],
    'Income': [income],
    'Total_Spending': [total_spending],
    'NumStorePurchases': [store_purchases],
    'NumWebPurchases': [web_purchases],
    'NumWebVisitsMonth': [web_visits]
})

# -------------------- ENSURE CORRECT FEATURE ORDER --------------------
try:
    input_data = input_data[scaler.feature_names_in_]
except Exception as e:
    st.error("Feature mismatch with scaler. Please check training columns.")
    st.stop()

# -------------------- SCALE --------------------
scaled_data = scaler.transform(input_data)

# -------------------- CLUSTER NAMES --------------------
cluster_names = {
    0: "Budget Customers",
    1: "Premium Customers",
    2: "Loyal High Spenders",
    3: "Regular Customers",
    4: "Occasional Buyers",
    5: "VIP Customers"
}

# -------------------- PREDICTION --------------------
if st.button("Predict Segment"):
    try:
        segment = int(kmeans.predict(scaled_data)[0])
        segment_name = cluster_names.get(segment, "Unknown")

        st.success(f"Customer belongs to: {segment_name} (Cluster {segment})")

        # -------------------- RECOMMENDATIONS --------------------
        st.subheader("Recommended Strategy")

        if segment_name == "VIP Customers":
            st.write("👉 Offer exclusive VIP deals, premium products, loyalty rewards")
        elif segment_name == "Premium Customers":
            st.write("👉 Promote high-end products and personalized offers")
        elif segment_name == "Loyal High Spenders":
            st.write("👉 Focus on retention, memberships, and rewards")
        elif segment_name == "Regular Customers":
            st.write("👉 Encourage upselling and cross-selling")
        elif segment_name == "Occasional Buyers":
            st.write("👉 Send discounts and engagement campaigns")
        elif segment_name == "Budget Customers":
            st.write("👉 Provide affordable deals and coupons")
            
        st.subheader("Cluster Descriptions")
        st.write("""
        Cluster 0: Low Income, Low Spending (Budget Customers)  
        Cluster 1: High Income, High Spending (Premium Customers)  
        Cluster 2: Very High Income, Very High Spending (Loyal High Spenders)  
        Cluster 3: Medium Income, Medium Spending (Regular Customers)  
        Cluster 4: Medium Income, Low Spending (Occasional Buyers)  
        Cluster 5: Very High Income, Very High Spending (VIP Customers)  
        """)

    except Exception as e:
        st.error(f"Prediction error: {e}")