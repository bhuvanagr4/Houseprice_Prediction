import streamlit as st
import joblib
import numpy as np

model = joblib.load("./house_price_tree_model.pkl")

st.title("House Price Prediction App")
st.write("This app predicts the price of a house based on its features.")

fea1 = st.number_input("Enter the Square_Footage of the house : ", min_value=0.0, step=1.0)
fea2 = st.number_input("Enter the Number_of_Bedrooms in the house : ", min_value=0, step=1)
fea3 = st.number_input(" Enter the Num_Bathrooms in house : ", min_value=0, step=1)
fea4 = st.number_input("Enter the Year_Built in years : ", min_value=0, step=1)
fea5 = st.number_input("Enter the Lot_Size in square feet : ", min_value=0.0, step=1.0)
fea6 = st.number_input("Enter the Garage_Size in number of cars : ", min_value=0, step=1)
fea7 = st.number_input(" Neighborhood_Quality ")

if st.button("Predict Price"):
    features = np.array([[fea1, fea2, fea3, fea4, fea5, fea6, fea7]])
    prediction = model.predict(features)
    st.write(f"The predicted price of the house is: {prediction[0]:.2f}")
