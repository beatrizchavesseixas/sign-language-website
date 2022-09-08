import streamlit as st
from PIL import Image
import base64

#Display logo on the left and titleon the right
col1, col2 = st.columns([1, 6])
with col2:
    #st.markdown('<h1 style="float: left;">MEDIAL SERVICES</h1><img style="float: right;" src="MEDICAL SYMBOL.PNG" />', unsafe_allow_html=True)
    st.title("The Model in Action")


#Visualize patient info
st.subheader("Patient details")
st.text("Name: Patricia Washington \nAge:31\nGenre: Female")


biagif= Image.open('beatriz.gif')
st.image(biagif, use_column_width=False)
