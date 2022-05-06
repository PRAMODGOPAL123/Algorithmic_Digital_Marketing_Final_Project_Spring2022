import streamlit as st
from PIL import Image
def app():
    st.title('Exploratory Data Analysis')

    option = st.selectbox(
     'Please select the option you want to analyse... ',
     ('Order by the hour of the day', 'Orders by day of week',\
      'Best Selling Products','Departments Vs Products Count','Most Popular Products',\
      'Aisles Vs Products Count','Customer Reorders Frequency',\
      'Total Orders and Reorders From Most Popular Aisles',\
      'Aisles with Highest Reorder Ratio','Aisles with Lowest Reorder Ratio',\
      'Total Orders and Reorders From Departments','Departments with Highest Reorder Ratio'))

    if option == 'Order by the hour of the day':
    	img =  Image.open("images/EDA/EDA7.PNG")
    	st.image(img)
    elif option == 'Orders by day of week':
    	img =  Image.open("images/EDA/EDA8.PNG")
    	st.image(img)
    elif option == 'Best Selling Products':
    	img =  Image.open("images/EDA/EDA10.PNG")
    	st.image(img)

    elif option == 'Departments Vs Products Count':
    	img =  Image.open("images/EDA/EDA11.PNG")
    	st.image(img)

    elif option == 'Aisles Vs Products Count':
    	img =  Image.open("images/EDA/EDA12.PNG")
    	st.image(img)


    elif option == 'Customer Reorders Frequency':
    	img =  Image.open("images/EDA/EDA9.PNG")
    	st.image(img)

    elif option == 'Total Orders and Reorders From Most Popular Aisles':
    	img =  Image.open("images/EDA/EDA1.PNG")
    	st.image(img)

    elif option == 'Aisles with Highest Reorder Ratio':
    	img =  Image.open("images/EDA/EDA2.PNG")
    	st.image(img)

    elif option == 'Aisles with Lowest Reorder Ratio':
    	img =  Image.open("images/EDA/EDA3.PNG")
    	st.image(img)

    elif option == 'Total Orders and Reorders From Departments':
    	img =  Image.open("images/EDA/EDA4.PNG")
    	st.image(img)

    elif option == 'Departments with Highest Reorder Ratio':
    	img =  Image.open("images/EDA/EDA5.PNG")
    	st.image(img)

    elif option == 'Most Popular Products':
    	img =  Image.open("images/EDA/EDA6.PNG")
    	st.image(img)
