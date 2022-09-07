import streamlit as st
from PIL import Image

#Display logo on the left and titleon the right
col1, col2 = st.columns([1, 6])
medical_image = Image.open('medical_symbol.png')
with col1:
    st.image(medical_image, width=100)
with col2:
    #st.markdown('<h1 style="float: left;">MEDIAL SERVICES</h1><img style="float: right;" src="MEDICAL SYMBOL.PNG" />', unsafe_allow_html=True)
    st.title("MEDICAL SERVICES")

#Visualize patient info
st.subheader("Patient details")
st.text("Name: Sarah Sanders \nAge:30\nGenre: Female")
