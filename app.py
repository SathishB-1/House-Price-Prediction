import pandas as pd
import streamlit as st
import joblib

# Load trained model
model = joblib.load('xgb_model.jb')

# Streamlit UI
st.title("🏡 House Price Prediction (₹ INR)")
st.write("Fill in the details below to estimate the house price in Indian Rupees.")

# List of input features
features = [
    'OverallQual', 'GrLivArea', 'GarageCars', '1stFlrSF',
    'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
    'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
    'CentralAir'
]

# Create input fields dynamically
user_input = {}

for feature in features:
    if feature == 'CentralAir':
        user_input[feature] = st.radio(f"🔘 {feature} (Has Central Air?)", ['Yes', 'No'], index=0)
    else:
        user_input[feature] = st.number_input(
            f"📏 {feature}",
            min_value=0.0, step=1.0 if feature in ['OverallQual', 'FullBath', 'Fireplaces', 'GarageCars'] else 0.1
        )

# Prediction Button
if st.button("🔮 Predict Price"):
    # Convert 'Yes'/'No' to numeric for CentralAir
    user_input['CentralAir'] = 1 if user_input['CentralAir'] == "Yes" else 0
    
    # Convert input to DataFrame
    input_df = pd.DataFrame([user_input])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Convert to Indian Rupees (assuming model was trained on USD)
    conversion_rate = 83  # Approx. 1 USD = 83 INR (Update with live rate if needed)
    prediction_inr = prediction * conversion_rate

    # Display result with ₹ formatting
    st.success(f"🏠 Estimated House Price: **₹{prediction_inr:,.2f}** 🎉")
