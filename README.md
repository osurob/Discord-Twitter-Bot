# Discord-Twitter-Bot
A discord bot that will send out messages everytime a specified user on Twitter has posted a new tweet

## Twitter API 
In order to gather information from Twitter I used the tweepy API to query tweets. It is necessary to have a Twitter developer account if you do not have one you can make one here: https://developer.twitter.com/en/apps. 

Replace screen_name here with the name of the Twitter handle you wish to get post notifications for. 
<code> cnbc_tweets = api.user_timeline(screen_name ='CNBCnow',count=2, tweet_mode="extended") </code>

Insert the channel ID that you wish to send Tweets to.
<code>channel = client.get_channel(ENTER CHANNEL ID HERE)</code>


### Requirements/Dependencies
There are some general library requirements for the project and some which are specific to individual methods.
The general requirements are as follows.


-> <code>Tweepy</code>

-> <code>Discord</code>

-> <code>asyncio</code>

-> <code>discord.ext</code>

-> <code>Twitter account</code>

-> <code>Discord account</code>



#### Usage

1. In order to use the code you must have the listed dependencies installed. 
2. Clone the github repo
3. Go to https://developer.twitter.com/en/apps and create new app, fill out information and get Consumer key/secret and access token/secret.
4. Open the twitterSentiment.py file and change the consumer_key, consumer_secret, access_token, and access_key to the twitter app api information you got from the previous step.
5. Go to https://discordapp.com/developers/applications make a new application, and a new bot, set admin privalleges on it, go to the Bot tab and copy the bot key and paste it in the main.py file here: client.run('DISCORD BOT KEY'). 
5. Open terminal and run main.py. <code>python3 main.py</code>

