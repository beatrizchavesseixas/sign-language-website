import streamlit as st
from PIL import Image


patient_image = Image.open('patient.jpg')
st.image(patient_image, width = 250, use_column_width=False)

st.markdown("""

    # Sign Language Translator in Healthcare

    #### *What about a sign language translator to improve communication between healthcare professionals and deaf patients?* :open_hands:

""")


biavideo = open("beatriz_novo.mp4", "rb")
st.video(biavideo)
