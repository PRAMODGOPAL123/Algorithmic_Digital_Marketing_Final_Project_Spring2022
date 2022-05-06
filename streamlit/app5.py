import re
import streamlit as st
from PIL import Image
import numpy as np
from xgboost_model_inference import xgboost_inference
def app():
	st.title('Furture Order Prediction')
	user_id = st.number_input('Please enter the Instacart UserID',step=1)
	product_id = st.number_input('Please enter the Product ID',step=1)
	last_three_times = st.number_input("Enter times user bought this product on its last 3 orders",step=1)
	total_orders = st.number_input("Total orders made by the user",step=1)
	total_times_of_reorder = st.number_input("Total number of times reordering is been done",step=1)
	total_num_of_products = st.number_input("Total number of ordered products",step=1)
	if total_num_of_products > 0:
		reorder_ratio = total_times_of_reorder/total_num_of_products
		# fixed_numbers = st.multiselect("Please select days of week oder has been done", [1, 2, 3, 4, 5,6,7])
		collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

		numbers = st.text_input("PLease different days of the week ordering done")
		fixed_numbers = collect_numbers(numbers)

		mean_dow = np.average(np.array(fixed_numbers))
		if mean_dow > 0:
			output  =  xgboost_inference(user_id, product_id, last_three_times, total_orders, reorder_ratio, mean_dow )
			if output == 0:
				st.subheader("Product will not be Re-ordered !!!")
			elif output == 1:
				st.subheader("Product will be Re-ordered !!!")