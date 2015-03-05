import tweepy
import os
import json

def getUserTweets(twitter_handle):

	auth = tweepy.OAuthHandler(os.environ['consumer_token'], os.environ['consumer_secret'])
	auth.set_access_token(os.environ['access_token'], os.environ['access_secret'])
	api = tweepy.API(auth)

	user_tweets = []

	# make initial request, only allowed 200 at a time

	new_tweets = api.user_timeline(screen_name = twitter_handle, count=200)
	no_retweets = filterRetweets(new_tweets)
	user_tweets += no_retweets

	#get id of the oldest tweet, to use as next request placeholder

	oldest = user_tweets[-1].id -1

	#then keep going through all the tweets that twitter lets you take

	while len(new_tweets) >0 :
		new_tweets = api.user_timeline(screen_name = twitter_handle, count =200, max_id = oldest)
		no_retweets = filterRetweets(new_tweets)
		user_tweets += no_retweets
		oldest = user_tweets[-1].id -1

	# get only the text

	tweet_text = outputText(user_tweets)

	return tweet_text

def filterRetweets(tweets):
	clean_tweets = []
	for tweet in tweets:
		if 'retweeted_status' not in tweet._json.keys():
			clean_tweets.append(tweet)
	return clean_tweets

def outputText(tweets):
	tweet_text = []
	for tweet in tweets:
		tweet_text.append(tweet._json['text'])
	return tweet_text

def cleanTweetText(tweet_text):
	clean_text= []
	for tweet in tweet_text:
		words = tweet.split()
		clean_words = [word for word in words if word[0] != '@' and word[0:4] != 'http'] #hacky way to get rid of irrelevant tweet words and urls
		clean_text.append(' '.join(clean_words))
	return clean_text

def writeTextFile(clean_text, title):
	with open(title, 'w') as text_file:
		for tweet in clean_text:
			text_file.write(tweet.encode("UTF-8") +'\n')




if __name__ == '__main__':
	getUserTweets('mallelis')






