# Twitter Bot
Twitter bot using, Python, OAuth 2.0, v2 Twitter API and OpenAI API (GPT-3).
The bot uses a redis database to store access tokens.



## How To Use

Get your keys after creating a app in [https://developer.twitter.com/](https://developer.twitter.com/) and put them in `keys.py`.

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
