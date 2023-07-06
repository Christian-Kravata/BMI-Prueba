# Required Libraries
import streamlit as st
# App Title
st.title('BMI Calculator')
# Weight Input
weight = st.number_input('Enter your weight (in kg)')
# Height Input
height = st.number_input('Enter your height (in cm)')
# BMI Calculation
if st.button('Calculate BMI'):
    height_m = height / 100.0  # converting cm to meters
    bmi = weight / (height_m ** 2)
    st.subheader(f'Your BMI is {bmi:.2f}')