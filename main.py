import discord
from discord.ext import commands, tasks
import asyncio
import tweepy

consumer_key = 'OugFjBD8EQZ0LhiaNHjlzdJpQ'
consumer_secret = 'ov4YWrk3gJfWOBY22T3zhqyimcxdLuKGSMiurSdAXlpXNgjVOf'

access_token = '767856757410365440-Nyrs60lVWDN65FfWitDcgaDmYfN7Cqw'
access_token_secret = 'Qg6wTBVzcOs3yIa36Vua74IRm8GEeprkYmub49iR3IUDe'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

client = discord.Client()

bno = [0,0,0,0]
cnbc = [0,0,0,0]
fed = [0,0,0,0]
test = [0,0,0,0]

@client.event
async def on_ready():
	background1.start()
	background2.start()
	background3.start()
	print('Bot is ready.')

@tasks.loop(seconds=5)
async def background1():
		bno_tweets = api.user_timeline(screen_name ='BNOdesk',count=2, tweet_mode="extended")
		bno_tweets = [tweet.id for tweet in bno_tweets]
		for tweet in bno_tweets:
			if tweet not in bno:
				bno.append(tweet)
				bno.pop(0)
				print(tweet)
				message = 'https://twitter.com/BNOdesk/status/'+str(tweet)
				channel = client.get_channel(691754811518877728)
				await channel.send(message)

@tasks.loop(seconds=5)
async def background2():
		cnbc_tweets = api.user_timeline(screen_name ='CNBCnow',count=2, tweet_mode="extended")
		cnbc_tweets = [tweet.id for tweet in cnbc_tweets]
		for tweet in cnbc_tweets:
			if tweet not in cnbc:
				cnbc.append(tweet)
				cnbc.pop(0)
				print(tweet)
				message = 'https://twitter.com/CNBCnow/status/'+str(tweet)
				channel = client.get_channel(691754871971643423)
				await channel.send(message)

@tasks.loop(seconds=5)
async def background3():
		fed_tweets = api.user_timeline(screen_name ='federalreserve',count=2, tweet_mode="extended")
		fed_tweets = [tweet.id for tweet in fed_tweets]
		for tweet in fed_tweets:
			if tweet not in fed:
				fed.append(tweet)
				fed.pop(0)
				print(tweet)
				message = 'https://twitter.com/federalreserve/status/'+str(tweet)
				channel = client.get_channel(691754886986989568)
				await channel.send(message)




client.run('NjkxNzUyMjc5MjU0MjM3NDA0.XnovrQ.37qBSG84ohHWTPMQVImWR-mFOSg')
