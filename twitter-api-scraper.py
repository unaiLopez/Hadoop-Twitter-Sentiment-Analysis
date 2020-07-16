from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

api_key = 'zLLMeyiztjdJvRACz7hCNW4BQ'
api_secret = 'AKlPRe9T8uu2eryLMB6RHNW5L1wk4SZTRqp0iRKC4FzYCq4fpf'
access_token = '1259880175048720385-3ep4rNQZu2FeooOJZ1U64epgzn60fU'
access_token_secret = 'D2n10T7dvoaqvHI36RNAZX8EsZgVdcEBLF8mkMO8JLQY7'

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
