import streamlit as st
from PIL import Image

patient_image = Image.open('patient.jpg')
st.image(patient_image, width = 300, use_column_width=False)

st.markdown("""

    # Sign Language Translator in Healthcare

    #### *What about a sign language translator to improve communication between healthcare professionals and deaf patients?* :open_hands:

""")
