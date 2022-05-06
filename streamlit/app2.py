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
    	img =  Image.open("images/EDA/EDA7.png")
    	st.image(img)
    elif option == 'Orders by day of week':
    	img =  Image.open("images/EDA/EDA8.png")
    	st.image(img)
    elif option == 'Best Selling Products':
    	img =  Image.open("images/EDA/EDA10.png")
    	st.image(img)

    elif option == 'Departments Vs Products Count':
    	img =  Image.open("images/EDA/EDA11.png")
    	st.image(img)

    elif option == 'Aisles Vs Products Count':
    	img =  Image.open("images/EDA/EDA12.png")
    	st.image(img)


    elif option == 'Customer Reorders Frequency':
    	img =  Image.open("images/EDA/EDA9.png")
    	st.image(img)

    elif option == 'Total Orders and Reorders From Most Popular Aisles':
    	img =  Image.open("images/EDA/EDA1.png")
    	st.image(img)

    elif option == 'Aisles with Highest Reorder Ratio':
    	img =  Image.open("images/EDA/EDA2.png")
    	st.image(img)

    elif option == 'Aisles with Lowest Reorder Ratio':
    	img =  Image.open("images/EDA/EDA3.png")
    	st.image(img)

    elif option == 'Total Orders and Reorders From Departments':
    	img =  Image.open("images/EDA/EDA4.png")
    	st.image(img)

    elif option == 'Departments with Highest Reorder Ratio':
    	img =  Image.open("images/EDA/EDA5.png")
    	st.image(img)

    elif option == 'Most Popular Products':
    	img =  Image.open("images/EDA/EDA6.png")
    	st.image(img)


    	
    # st.subheader("Total Orders and Reorders From Most Popular Aisles")
    # img =  Image.open("images/EDA/EDA1.png")
    # st.image(img)

    # st.subheader("Aisles with Highest Reorder Ratio")
    # img_1 =  Image.open("images/EDA/EDA2.png")
    # st.image(img_1)

    # st.subheader("Aisles with Lowest Reorder Ratio")
    # img_2 =  Image.open("images/EDA/EDA3.png")
    # st.image(img_2)

    # st.subheader("Total Orders and Reorders From Departments")
    # img_3 =  Image.open("images/EDA/EDA4.png")
    # st.image(img_3)

    # st.subheader("Departments with Highest Reorder Ratio")
    # img_4 =  Image.open("images/EDA/EDA5.png")
    # st.image(img_4)

    # st.subheader("Most Popular Products")
    # img_5 =  Image.open("images/EDA/EDA6.png")
    # st.image(img_5)

    # st.subheader("Order by the hour of the day")
    # img_6 =  Image.open("images/EDA/EDA7.png")
    # st.image(img_6)

    

    # st.subheader("Orders by day of week")
    # img_7 =  Image.open("images/EDA/EDA8.png")
    # st.image(img_7)

    # st.subheader("Customer Reorders Frequency")
    # img_8 =  Image.open("images/EDA/EDA9.png")
    # st.image(img_8)

    # st.subheader("Best Selling Products")
    # img_9 =  Image.open("images/EDA/EDA10.png")
    # st.image(img_9)

    # st.subheader("Departments Vs Products Count")
    # img_10 =  Image.open("images/EDA/EDA11.png")
    # st.image(img_10)

    # st.subheader("Aisles Vs Products Count")
    # img_12 =  Image.open("images/EDA/EDA12.png")
    # st.image(img_12)
