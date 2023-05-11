# Twitter Bot
Twitter bot with Python, OAuth 2.0 and v2 Twitter API.
The bot uses a redis database to store access tokens.



## How To Use

Get your keys after creating a app in `https://developer.twitter.com/` and put them in `keys.py`

Modify `tweet_text.py` to fit your needs. In this case the bot webscrapes uvkollen.se for the current day's UV-index values for a certain city. It then tweets out the scraped values together with appropriate emojis without needing any more authentication.

If you are tweeting directly from the `main.py` you will have to manually authenticate each tweet in your browser.



### Redis database

You will have to set up a redis database to store access tokens. In this instance the database is running locally.
Documentation: `https://redis.io/docs/getting-started/`


To test if the database is working properly:
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
