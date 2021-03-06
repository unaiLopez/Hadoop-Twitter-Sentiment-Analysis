from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

api_key = '***********************'
api_secret = '***********************'
access_token = '***********************'
access_token_secret = '***********************'

tracklist = ['#covid19', '#covid', '#coronavirus']
lang = ['en']

class StdOutListener(StreamListener):
	def on_data(self, data):
		print(data)
		return True
	def error(self, status):
		print(status)

if __name__ == '__main__':
	l = StdOutListener()

	auth = OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(track = tracklist, languages=lang)
