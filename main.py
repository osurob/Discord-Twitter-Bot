import discord
from discord.ext import commands, tasks
import asyncio
import tweepy

consumer_key = 'YOUR TWITTER CONSUMER KEY'
consumer_secret = 'YOUR TWITTER CONSUMER SECRET'

access_token = 'YOUR TWITTER ACCESS_TOKEN'
access_token_secret = 'YOUR TWITTER TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

client = discord.Client()

#Stack for BNOnews Tweets
bno = [0,0,0,0]

@client.event
async def on_ready():
	#Starts BNOnews Twitter tracker
	background1.start()
	print('Bot is ready.')

#Task checks every 5 seconds if a new tweet has been posted
@tasks.loop(seconds=5)
async def background1():
		#Initiation grabs first 2 tweets
		#screen_name is the Twitter handle you wish to follow
		bno_tweets = api.user_timeline(screen_name ='TWITTER ACCOUNT NAME TO TRACK',count=2, tweet_mode="extended")
		bno_tweets = [tweet.id for tweet in bno_tweets]
		for tweet in bno_tweets:
			if tweet not in bno:
				#append and pop to stack if new post was made
				bno.append(tweet)
				bno.pop(0)
				print(tweet)
				#On the next line, replace with Twitter handle to follow
				message = 'https://twitter.com/REPLACE WITH TWITTER HANDLE/status/'+str(tweet)
				#Replace with channel id
				channel = client.get_channel(ENTER CHANNEL ID HERE)
				await channel.send(message)


#Replace with Bot token https://discordapp.com/developers/applications
#Located on bot tab
client.run('REPLACE WITH DISCORD BOT TOKEN')





