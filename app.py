import pickle
import streamlit as st 
model=pickle.load(open('model.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))
st.title("Bike Rental Prediction")
num=st.number_input("Enter a Temperature ")
num=scaler.transform([[num]])
op=model.predict(num)
button=st.button("Predict Bike Rental")
if button:
    st.write("Your Bike Rental is",op)

