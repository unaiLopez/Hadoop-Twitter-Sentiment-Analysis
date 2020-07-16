#!/usr/bin/python3
import sys

avgPolarity = 0
avgSubjetivity = 0


for line in sys.stdin:
	sumPolarity = 0
	sumSubjectivity = 0
	line_parts = line.split(" ||| ")

	tweets = eval(line_parts[1])
	polarities = eval(line_parts[2])
	subjectivities = eval(line_parts[3])
	
	if len(tweets) > 10:
		avgPolarity = 0
		avgSubjectivity = 0
		for index in range(len(tweets)):
			sumPolarity += polarities[index]
			sumSubjectivity += subjectivities[index]
		avgPolarity = sumPolarity / len(tweets)
		avgSubjectivity = sumSubjectivity / len(tweets)
		
		print(line_parts[0], " ||| ", tweets, " ||| ", polarities, " ||| ", subjectivities, " ||| ", avgPolarity, " ||| ", avgSubjectivity)
		
