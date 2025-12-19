import streamlit as st
import pickle
import numpy as np
import ui  

# --- Files Load Karein ---
try:
    model = pickle.load(open('final_multi_model.pkl', 'rb'))
    scaler_X = pickle.load(open('scaler_X.pkl', 'rb'))
    scaler_y = pickle.load(open('scaler_y.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files nahi milein! Please check filenames.")
    st.stop()

ui.apply_custom_css()
ui.display_header()


# app.py ke sidebar section ko English help text ke sath update karein
with st.sidebar:
    st.markdown("### ⚙️ Input Features")
    
    # Quantity input with English help text
    quantity = st.number_input(
        "Quantity", 
        min_value=1, 
        value=100, 
        help="Enter the total number of units sold."
    )
    
    # Cost input with English help text and range guidance
    cost = st.number_input(
        "Cost (£)", 
        min_value=0.1, 
        value=10.0, 
        help="Enter the cost per unit. Typically, this ranges between £10 and £30 based on historical data."
    )
    
    st.info("The model is based on Quantity and Cost features.")
    predict_btn = st.button("Predict Now")


if predict_btn:
    # 1. Input ko scale karein
    scaled_features = scaler_X.transform([[quantity, cost]])
    
    # 2. Prediction lein
    prediction_scaled = model.predict(scaled_features)
    
    # 3. Wapas Pounds mein badlein
    prediction_original = scaler_y.inverse_transform(prediction_scaled)
    
    # Negative values ko 0 set karein
    profit = max(0, prediction_original[0][0])
    revenue = max(0, prediction_original[0][1])
    
    # UI Results Cards
    ui.display_result_card(profit, revenue)
    
    # Graphs Display
    ui.display_graphs(profit, revenue)
else:
    st.info("👈 Please enter values in the sidebar and click 'Predict Now'")