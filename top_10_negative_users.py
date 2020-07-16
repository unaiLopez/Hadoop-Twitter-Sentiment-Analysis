#!/usr/bin/python3
import sys
import numpy as np

active_users_avgpolarity = []
active_users_data = []

for line in sys.stdin:
	dict_user_data = {}

	line_parts = line.split(" ||| ")
	
	tweets = eval(line_parts[1])
	polarities = eval(line_parts[2])
	subjectivities = eval(line_parts[3])
	avgPolarity = float(line_parts[4])
	avgSubjectivity = float(line_parts[5])

	dict_user_data["user"] = line_parts[0]
	dict_user_data["tweets"] = tweets
	dict_user_data["polarities"] = polarities
	dict_user_data["subjectivities"] = subjectivities
	dict_user_data["avgPolarity"] = avgPolarity
	dict_user_data["avgSubjectivity"] = avgSubjectivity

	active_users_avgpolarity.append(avgPolarity)
	active_users_data.append(dict_user_data)

print("THESE ARE THE TOP 10 MOST NEGATIVE USERS ACCORDING TO #COVID, #COVID19 AND #CORONAVIRUS IN TWITTER")
print()

counter = 1

for order_user in np.argsort(active_users_avgpolarity)[:10]:

	print("USER #", counter);
	print()
	
	print("Username : ", active_users_data[order_user]["user"])
	print("Tweets :\n")
	for index in range(len(active_users_data[order_user]["tweets"])):
		print("\t", active_users_data[order_user]["tweets"][index], " ||| Polarity: ", active_users_data[order_user]["polarities"][index], " ||| Subjectivity: ", active_users_data[order_user]["subjectivities"][index])
		print()
	print("AVERAGE POLARITY OF THE USER IS: ", active_users_data[order_user]["avgPolarity"])
	print("AVERAGE SUBJECTIVITY OF THE USER IS: ", active_users_data[order_user]["avgSubjectivity"])
	
	print()
	print("==================================================================================================================================")
	print("==================================================================================================================================")
	print()

	counter += 1


	
		
