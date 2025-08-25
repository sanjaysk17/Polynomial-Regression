import pickle
import streamlit as st 
model=pickle.load(open('model.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))
st.title("Bike Rental Prediction")
num=st.number_input("Enter a Temperature ")
num=scaler.transform([[num]])
op=model.predict(num)
st.button("Predict Bike Rental")
st.write("Your Bike Rental is",op)

