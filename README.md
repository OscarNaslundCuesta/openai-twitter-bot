# Twitter Bot
Twitter bot using, Python, OAuth 2.0, v2 Twitter API and OpenAI API (GPT-3).
The bot uses a redis database to store access tokens.

![Image](twitter_bot.png)

## Features
- Webscrapes my friends website [https://uvkollen.se](https://uvkollen.se) for the current UV-index
- Creates a funny tweet using a GPT-3 prompt or ...
- Tweets a random appropriate pre-generated tweet
- Uses OAuth 2.0 PKCE Auth or HTTPBasicAuth



## How To Use

Get your keys after creating a app in [https://developer.twitter.com/](https://developer.twitter.com/). You are going to want to create an .env file and set up enviroment variables for security reasons. The `keys.py` can also be used but it isn't ideal.

Modify `tweet_generator.py` to fit your needs. In this case the bot webscrapes uvkollen.se for the current day's UV-index values for a certain city. It then tweets out the scraped values together with appropriate emojis without needing any more authentication. OpenAI API usage is optional and can be changed inside this file.

If you are tweeting directly from the `main.py` you will have to manually authenticate each tweet in your browser. If you are using `auto_tweeter.py` it will tweet automatically.



### Redis database

You will have to set up a redis database to store access tokens. In this instance the database is running locally.
Documentation: [https://redis.io/docs/getting-started/](https://redis.io/docs/getting-started/)

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
"mytoken"
```
