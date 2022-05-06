import pickle
import numpy as np
import xgboost as xgb
model = pickle.load(open("./pickle_files/finalized_model.pkl","rb"))


def xgboost_inference(user_id, product_id,last_three_order_times,c_total_orders,reorder_ratio,average_dow ):
	# user_id  = 12
	# product_id = 292
	# last_three_order_times = 0 #last_three = (times user bought product on its last 3 orders) / (total orders)
	# c_total_orders  = 2 #total number of customer orders
	# reorder_ratio = 0.1 #(total times of reorder) / (total # of ordered products)
	# average_dow = 2.5 # mean of order_dow column

	input_arr = np.array([[user_id,product_id,last_three_order_times,c_total_orders,reorder_ratio,average_dow]])


	output = model.predict(input_arr)
	return output[0]