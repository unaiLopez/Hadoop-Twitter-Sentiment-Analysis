#!/usr/bin/python3
import sys
from textblob import TextBlob
import json

for line in sys.stdin:
	replace_symbols = ['#', '@', '*', 'RT']
	try:
		line = json.loads(line)
		user_name = line["user"]["screen_name"]
		text = line["text"]

		for symbol in replace_symbols:
			text = text.replace(symbol, '')

		sentiment = TextBlob(text).sentiment
		print (user_name," ||| ", text, " ||| ", sentiment.polarity, " ||| ", sentiment.subjectivity)
	except:
		pass
