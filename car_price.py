import pickle

import pandas as pd
import sklearn
import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

st.title("Car Resale Price Prediction")


cars_df = pd.read_csv("cars24-car-price.csv")

st.dataframe(cars_df.head())


# save
# with open('model.pkl','wb') as f:
#     pickle.dump(clf,f)


# load
with open('car_pred_model', 'rb') as f:
    model = pickle.load(f)

print("model loaded successfully")
# same as sklearn model.
# model.predict()

st.header("Car Price Prediction")
st.write("Enter the details of the car to predict its price.")

col1, col2 = st.columns(2)

with col1:
    fuel_type = st.selectbox("Select the fuel type",
                            ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

    engine = st.slider("Set the Engine Power",
                       500, 5000, step=100)
with col2:

    transmission_type = st.selectbox("Select the transmission type",
                                   ["Manual", "Automatic"])

    seats = st.selectbox("Enter the number of seats",
                       [4,5,7,9,11])

## Encoding Categorical features
## Use the same encoding as used during the training.
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

if st.button("Predict Price"):
    st.write("Predicting...")

    encoded_fuel_type = encode_dict["fuel_type"][fuel_type]
    encoded_transmission_type = encode_dict["transmission_type"][transmission_type]

    input_data = [[2012.0,2,120000,encoded_fuel_type,encoded_transmission_type,19.7,engine,46.3,seats]]
    price = model.predict(input_data)
    st.header(f"Predicted Price: ₹ {price[0]:.2f} Lakhs")