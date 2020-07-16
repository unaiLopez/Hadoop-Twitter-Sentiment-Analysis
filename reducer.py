#!/usr/bin/python3
import sys
import json

users_tweets = {}

for line in sys.stdin:
	line_parts = line.split(" ||| ")
	if len(line_parts) == 4:
		if line_parts[0] not in users_tweets:	
			users_tweets[line_parts[0]] = {}
			users_tweets[line_parts[0]]["tweets"] = []
			users_tweets[line_parts[0]]["polarities"] = []
			users_tweets[line_parts[0]]["subjectivities"] = []

		users_tweets[line_parts[0]]["tweets"].append(line_parts[1])
		users_tweets[line_parts[0]]["polarities"].append(float(line_parts[2]))
		users_tweets[line_parts[0]]["subjectivities"].append(float(line_parts[3]))

for key in users_tweets:
	print(key, " ||| ", users_tweets[key]["tweets"], " ||| ", users_tweets[key]["polarities"], " ||| ", users_tweets[key]["subjectivities"])
