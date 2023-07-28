# Twitter Bot
Twitter bot using, Python, OAuth 2.0, v2 Twitter API and OpenAI API (GPT-3).
The bot uses a redis database to store access tokens. [View the result here](https://github.com/OscarNaslundCuesta/openai-twitter-bot)!

![Image](twitter_bot.png)

## Features
- Webscrapes my friends website [uvkollen.se](https://uvkollen.se) for the current UV-index
- Creates a funny tweet using a GPT-3 prompt or ...
- Tweets a random appropriate pre-generated tweet
- Uses OAuth 2.0 PKCE Auth or HTTPBasicAuth

## Installation

**Git**

```
$ git clone https://github.com/OscarNaslundCuesta/openai-twitter-bot.git
$ cd openai-twitter-bot
$ pip install -r requirements.txt
```


## How To Use

Get your keys ("Client ID" and "Client Secret") after creating a app in [developer.twitter.com](https://developer.twitter.com/). You can find your OpenAI API-key at [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys). You are going to want to rename `.env.example` to `.env` and set up enviroment variables for your own keys.

Modify `tweet_generator.py` to fit your needs. In this case the bot webscrapes uvkollen.se for the current day's UV-index values for a certain city. It then tweets out the scraped values together with appropriate emojis without needing any more authentication. OpenAI API usage is optional and can be changed inside this file.

If you are tweeting directly from the `main.py` you will have to manually authenticate each tweet in your browser. If you are using `auto_tweeter.py` it will tweet automatically.



### Redis database

If you are running your redis database locally, you will have to set it up to store access tokens. In this instance the database is running locally.
Documentation: [redis.io/docs/getting-started/](https://redis.io/docs/getting-started/)

To start the redis database:
```
$ redis-server
```


Then test if the database is working properly in another terminal window:
```
$ redis-cli ping
PONG
```


To see the current token:
```
$ redis-cli
redis> GET token
"{'token_type': 'bearer', 'expires_in': 7200, 'access_token': 'abcdefgEXAMPLE123456', 'scope': ['tweet.write', 'users.read', 'tweet.read', 'offline.access'], 'refresh_token': 'abcdefgEXAMPLE123456', 'expires_at': 1690061044.901524}"

```

If the current token is empty, try to tweet once by running `main.py`.
This will set the token, so you can later tweet using `auto_tweeter.py`.


### Cloud Hosting
I am hosting my bot on Render.com using a cronjob, which runs once each day, together with a redis database.
In the secret `.env` file inside the cronjob I use the "External Redis URL" to connect to redis database. I have also whitelisted the cronjob's IP-addresses to be able to access the redis database.

The cronjob build command:
```
$ /opt/render/project/src/.venv/bin/python -m pip install --upgrade pip && pip install -r requirements.txt
```
The cronjob command that runs periodically:
```
$ python3 auto_tweeter.py
```