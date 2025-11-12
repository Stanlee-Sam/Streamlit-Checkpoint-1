import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Expresso Churn Prediction", page_icon="📱")

# Load trained model
model = joblib.load('expresso_model.pkl')

st.title("📱 Expresso Churn Prediction App")
st.write("This app predicts whether a telecom customer is likely to churn based on their usage behavior.")

# Create input fields
st.subheader("Enter Customer Details:")

REGION = st.text_input("Region (e.g., DAKAR, THIES)")
TENURE = st.number_input("Tenure (months)", min_value=0.0)
MONTANT = st.number_input("Montant (Recharge Amount)", min_value=0.0)
FREQUENCE_RECH = st.number_input("Recharge Frequency", min_value=0.0)
REVENUE = st.number_input("Revenue", min_value=0.0)
ARPU_SEGMENT = st.number_input("ARPU Segment", min_value=0.0)
FREQUENCE = st.number_input("Frequency", min_value=0.0)
DATA_VOLUME = st.number_input("Data Volume (MB)", min_value=0.0)
ON_NET = st.number_input("On Net Calls", min_value=0.0)
ORANGE = st.number_input("Orange Calls", min_value=0.0)
TIGO = st.number_input("Tigo Calls", min_value=0.0)
ZONE1 = st.number_input("Zone1", min_value=0.0)
ZONE2 = st.number_input("Zone2", min_value=0.0)
MRG = st.number_input("MRG", min_value=0.0)
REGULARITY = st.number_input("Regularity", min_value=0.0)
TOP_PACK = st.number_input("Top Pack", min_value=0.0)
FREQ_TOP_PACK = st.number_input("Frequency of Top Pack", min_value=0.0)

if st.button("🔍 Predict Churn"):
    # Make sure columns match exactly what model expects
    input_df = pd.DataFrame({
        'REGION': [REGION],
        'TENURE': [TENURE],
        'MONTANT': [MONTANT],
        'FREQUENCE_RECH': [FREQUENCE_RECH],
        'REVENUE': [REVENUE],
        'ARPU_SEGMENT': [ARPU_SEGMENT],
        'FREQUENCE': [FREQUENCE],
        'DATA_VOLUME': [DATA_VOLUME],
        'ON_NET': [ON_NET],
        'ORANGE': [ORANGE],
        'TIGO': [TIGO],
        'ZONE1': [ZONE1],
        'ZONE2': [ZONE2],
        'MRG': [MRG],
        'REGULARITY': [REGULARITY],
        'TOP_PACK': [TOP_PACK],
        'FREQ_TOP_PACK': [FREQ_TOP_PACK]
    })

    prediction = model.predict(input_df)
    result = "🚨 Customer is likely to churn" if prediction[0] == 1 else "✅ Customer is not likely to churn"
    st.success(result)
