import streamlit as st
import joblib
import pandas as pd

# Load the saved Random Forest pipeline
model = joblib.load('random_forest_pipeline.pkl')

# Streamlit app
st.title("Toyota Corolla Price Prediction App 🚗💰")

st.write("Enter the car details below to predict its price:")

# User inputs
age = st.slider('Age of the car (in months)', 0, 300, 60)
km = st.number_input('Kilometers driven', 0, 300000, 50000)
hp = st.number_input('Horsepower', 50, 200, 90)
cc = st.number_input('Engine size (CC)', 1000, 3000, 1600)
doors = st.selectbox('Number of doors', [2, 3, 4, 5])
gears = st.selectbox('Number of gears', [4, 5, 6])

fuel_type = st.selectbox('Fuel Type', ['Diesel', 'Petrol', 'CNG'])
color = st.selectbox('Color', ['Blue', 'Red', 'Grey', 'Silver', 'Black', 'White'])

# Binary features
automatic = st.selectbox('Automatic Transmission?', ['No', 'Yes'])
abs_feature = st.selectbox('ABS?', ['No', 'Yes'])
airco = st.selectbox('Air Conditioning?', ['No', 'Yes'])
cd_player = st.selectbox('CD Player?', ['No', 'Yes'])
powered_windows = st.selectbox('Powered Windows?', ['No', 'Yes'])
power_steering = st.selectbox('Power Steering?', ['No', 'Yes'])
airbag_1 = st.selectbox('Driver Airbag?', ['No', 'Yes'])
airbag_2 = st.selectbox('Passenger Airbag?', ['No', 'Yes'])
sport_model = st.selectbox('Sport Model?', ['No', 'Yes'])
metallic_rim = st.selectbox('Metallic Rim?', ['No', 'Yes'])
radio = st.selectbox('Radio?', ['No', 'Yes'])
mfr_guarantee = st.selectbox('Manufacturer’s Guarantee?', ['No', 'Yes'])

# Prepare input data as DataFrame with correct column names
input_df = pd.DataFrame([{
    'Age_08_22': age,
    'KM': km,
    'HP': hp,
    'CC': cc,
    'Doors': doors,
    'Gears': gears,
    'Fuel_Type': fuel_type,
    'Color': color,
    'Automatic': int(automatic == 'Yes'),
    'ABS': int(abs_feature == 'Yes'),
    'Airbag_1': int(airbag_1 == 'Yes'),
    'Airbag_2': int(airbag_2 == 'Yes'),
    'Airco': int(airco == 'Yes'),
    'CD_Player': int(cd_player == 'Yes'),
    'Powered_Windows': int(powered_windows == 'Yes'),
    'Power_Steering': int(power_steering == 'Yes'),
    'Radio': int(radio == 'Yes'),
    'Sport_Model': int(sport_model == 'Yes'),
    'Metallic_Rim': int(metallic_rim == 'Yes'),
    'Mfr_Guarantee': int(mfr_guarantee == 'Yes')
}])

# Predict button
if st.button('Predict Price'):
    predicted_price = model.predict(input_df)[0]
    st.success(f"Estimated Price: ${predicted_price:.2f}")
