import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color:  #000000;
        color:white;    
    }
    .stApp {
        background:linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px  10px 30px rgba(0, 0, 0, 0.3);
        
    }
    
    h1 {
        text-align: center
        font-size:36px;
        color: white;
    }
    
    .stButton>button {
        background: linear-gradient(45deg,rgb(148, 11, 102),rgb(117, 28, 87));
        color: white;
        font-size: 18px;
        paddingL 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shodow: 0px 5px 15px rgba(80, 12, 149, 0.4);
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size:20px;
        font-weight: bold;
        text-align: cednter;
        background: rgba(255, 255, 255, 0.1);
        padding:25px;
        border-radius: 10px;
        marging-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        marging-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    } 
    """,
    unsafe_allow_html=True 
)
#tital and description Streamlit <h1
st.markdown("<h1> Unit Converter using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write(" Easily convert between different units of length , weight, and temprature. ")

#sidebar menu
conversion_type = st.sidebar.selectbox("Choose Converversion Type", ["Length", "Weight", "Temprature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches","Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches","Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Miligrams", "Pounds", "Ounces"] )
    with col2:
        to_unit = st.selectbox("To",["Kilogram", "Grams", "Miligrams", "Pounds", "Ounces"])
elif conversion_type == "Temprature": 
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"]) 
    with col2: 
        to_unit =st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
#converted function

def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centemeters': 100, 'Milimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'inches': 39.37
    }     
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Miligrams': 1000000, 'Pounds': 2.2046, 'Ounces': 35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temprature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit ==  "Celsius" else (value -32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value -273.15) * 9/5+32 if to_unit == "Fahrenheit" else value
    return value

#button for conversion
if st.button("🤖convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
        
    elif conversion_type == "Temprature":
        result = temprature_converter(value, from_unit, to_unit)
        
    st.markdown(f"<div class = 'result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    
st.markdown("<div class='footer'>Created with love by Roma</div>", unsafe_allow_html=True)
    
    
    
    
    
    
    

    

           