import streamlit as st
from PIL import Image
import base64

#Display logo on the left and titleon the right
col1, col2 = st.columns([1, 6])
with col2:
    #st.markdown('<h1 style="float: left;">MEDIAL SERVICES</h1><img style="float: right;" src="MEDICAL SYMBOL.PNG" />', unsafe_allow_html=True)
    st.title("The Model in Action")


#Visualize patient info
st.subheader("The progress")
st.text("Step 1")


col1, col2, col3 = st.columns(3)

with col1:
    giovideo = open("giovanna_novo.mp4", "rb")
    st.video(giovideo)

with col2:
    biavideo = open("beatriz_novo.mp4", "rb")
    st.video(biavideo)

with col3:
    pablovideo = open("pablo_novo.mp4", "rb")
    st.video(pablovideo)
