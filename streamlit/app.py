import app1
import app2
import app3
import app4
import app5
import streamlit as st
PAGES = {
    "Home Page": app1,
    "Data Analysis": app2,
    "RFM Analysis": app3,
    "Product Recommendor": app4,
    "Future Order Predictor": app5
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()