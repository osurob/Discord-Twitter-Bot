

#This example application will send messages to discord channels when a new post is made from
#a specified Twitter account. In this example I use @BNOnews, @CNBCnow, and @federalreserve


import discord
from discord.ext import commands, tasks
import asyncio
import tweepy

#Twitter API 
consumer_key = 'CONSUMER KEY FROM TWITTER DEVELOPER PORTAL'
consumer_secret = 'CONSUMER SECRET FROM TWITTER DEVELOPER PORTAL'
access_token = 'ACCESS TOKEN FROM TWITTER DEVELOPER PORTAL'
access_token_secret = 'ACCESS TOKEN SECRET FROM TWITTER DEVELOPER PORTAL'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#Start discord client
client = discord.Client()

bno = []
cnbc = []
fed = []

@client.event
async def on_ready():
	background.start()
	print('Bot is ready.')

#screen_name represents the twitter handle to follow
#replace "ENTER CHANNEL ID HERE" with actual channel id pulled from discord.
#to get channel id, right click on the channel and copy it
#go to message and replace /BNOdesk/ to the name of 

#Seconds is the number of seconds in between checking if a new post has been made
@tasks.loop(seconds=2)
async def background():
		#Replace screen_name with the handle of the twitter account you'd like to follow
		bno_tweets = api.user_timeline(screen_name ='BNOdesk',count=2, tweet_mode="extended")
		bno_tweets = [tweet.id for tweet in bno_tweets]
		for tweet in bno_tweets:
			if tweet not in bno:
				bno.append(tweet)
				print(tweet)
				#Replace BNOdesk in message to name of screen_name you're planning on following
				message = 'https://twitter.com/BNOdesk/status/'+str(tweet)
				channel = client.get_channel(ENTER CHANNEL ID HERE)
				await channel.send(message)

		#Replace screen_name with the handle of the twitter account you'd like to follow
		cnbc_tweets = api.user_timeline(screen_name ='CNBCnow',count=2, tweet_mode="extended")
		cnbc_tweets = [tweet.id for tweet in cnbc_tweets]
		for tweet in cnbc_tweets:
			if tweet not in cnbc:
				cnbc.append(tweet)
				print(tweet)
				#Replace CNBCnow in message to name of screen_name you're planning on following
				message = 'https://twitter.com/CNBCnow/status/'+str(tweet)
				channel = client.get_channel(ENTER CHANNEL ID HERE)
				await channel.send(message)


		#Replace screen_name with the handle of the twitter account you'd like to follow
		fed_tweets = api.user_timeline(screen_name ='federalreserve',count=2, tweet_mode="extended")
		fed_tweets = [tweet.id for tweet in fed_tweets]
		for tweet in fed_tweets:
			if tweet not in fed:
				fed.append(tweet)
				print(tweet)
				#Replace federalreserve in message to name of screen_name you're planning on following
				message = 'https://twitter.com/federalreserve/status/'+str(tweet)
				channel = client.get_channel(ENTER CHANNEL ID HERE)
				await channel.send(message)

#replaace with actual discord bot key found in discord developer portal
client.run('DISCORD BOT KEY')

