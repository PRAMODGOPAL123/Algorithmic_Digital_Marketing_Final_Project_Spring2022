import streamlit as st
from PIL import Image

def app():
	st.title('RFM Customer Segmentation Analysis')
	if st.button('Generate RFM Plot.'):
		img =  Image.open("images/RFM.PNG")
		st.image(img)