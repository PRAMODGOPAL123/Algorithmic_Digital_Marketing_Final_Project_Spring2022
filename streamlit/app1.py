import streamlit as st
from PIL import Image
def app():
    st.title('InstaCart Marketing Analytics')
    img =  Image.open("./images/instacart.jpg")
    st.image(img,width=600)
  