# Project 01: Unit Convertor
# Build a Google Unit Convertor using Python & StreamLit

import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: skyblue;
        color:white
}
    .stApp{
        background-color: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding:30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1{
        text-align: center;
        font-size: 36px;
        color: white;

    }
    .stButton>button{
        background: linear-gradient(45deg, #0b5394, #351c75);
        color:white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stbutton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color:black;
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background:rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        color: black;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#tile & description
st.markdown("<h1> Unit Convertor using Python & StreamLit </h1> ", unsafe_allow_html=True )
st.write("Easily convert between different units of length, weight & temperature.")

#siebar menu
coversion_type = st.sidebar.selectbox("Choose Conversion Type",["Length","Weight","Temperature"])
value = st.number_input("Enter Value", value= 0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)
if coversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters","Kilometers", "Centimeters","Milimeters","Miles","Yards","Inches","Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters","Kilometers", "Centimeters","Milimeters","Miles","Yards","Inches","Feet"])
elif coversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms","Grams","Miligrams","Pounds","Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms","Grams","Miligrams","Pounds","Ounces"])

elif coversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsis", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsis", "Fahrenheit", "Kelvin"])

# Values Converted Function
def length_convertor(value, from_unitm, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Milometers': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value,from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams':1000, 'Miligrams':100000, 'Pounds':2.2046, 'Ounces':35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Celcius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) *5/9 if to_unit == "Celcius" else (value -32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if  to_unit == "Celcius" else (value - 273.15) * 9/5+32 if to_unit == "Fahrenheit" else value
    return value

# Button for convert values
if st.button("Convert Values"):
    if coversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif coversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif coversion_type == "Temperature":
        result = temperature_convertor(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: 4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown ("<div class='footer'>All Right Reserved @ Copyright </div>", unsafe_allow_html=True )

