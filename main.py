import numpy as np
import streamlit as st

# import pickle
import joblib

# model_lr = pickle.load(open("model.pkl", "rb"))
# model_svr = pickle.load(open("model_svr.pkl", "rb"))

model_lr = joblib.load("model_lr.pkl")
model_svr = joblib.load("model_svr.pkl")

st.set_page_config(
    page_title="CO2 Emission Prediction", page_icon=":car:", layout="centered"
)

st.title("CO2 Emission Prediction by Vehicles")

transmission_type = ["Automatic", "Manual"]

fuel_type = ["Petrol", "Premium Petrol", "Diesel"]

col1, col2, col3 = st.columns(3)

with col1:
    engine_size = st.number_input("Engine size(in L)", min_value=1.10)

with col2:
    cylinders = st.select_slider("Cylinders", options=range(4, 13, 2))

with col3:
    fuel_consumption = st.select_slider(
        "Fuel Consumption(in kmpl)", options=range(1, 51)
    )

col4, col5 = st.columns(2)

with col4:
    transmission_type_inp = st.selectbox("Transmission Type", options=transmission_type)

if transmission_type_inp == "Automatic":
    transmission_type_inp = 0
else:
    transmission_type_inp = 1

with col5:
    fuel_type_inp = st.selectbox("Fuel Type", options=fuel_type)

if fuel_type_inp == "Petrol":
    fuel_type_inp = 0
elif fuel_type_inp == "Premium Petrol":
    fuel_type_inp = 1
else:
    fuel_type_inp = 2


def predict_co2():
    # Define all feature names columns
    columns = [
        "Engine Size(L)",
        "Cylinders",
        "Transmission",
        "Fuel Type",
        "Fuel Consumption Comb (kmpl)",
    ]

    # Reshape input data to make it 2D
    input_data = np.array(
        [
            [
                engine_size,
                cylinders,
                transmission_type_inp,
                fuel_type_inp,
                fuel_consumption,
            ]
        ]
    )

    # Predict CO2 emission
    # predicted_co2 = model_lr.predict(input_data)
    predicted_co2 = model_svr.predict(input_data)

    if predicted_co2:
        st.error(f"Predicted CO2 Emission: {round(predicted_co2[0], ndigits=2)} g/km")


st.button("Predict CO2 emitted", type="primary", on_click=predict_co2)
