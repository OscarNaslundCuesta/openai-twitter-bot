import main
import redis
import json
import keys
from requests.auth import HTTPBasicAuth
import tweet_text


twitter = main.make_token()
client_id = keys.client_id
client_secret = keys.client_secret
token_url = "https://api.twitter.com/2/oauth2/token"

t = main.r.get("token")
bb_t = t.decode("utf8").replace("'", '"')
data = json.loads(bb_t)

auth = HTTPBasicAuth(keys.client_id, keys.client_secret)

refreshed_token = twitter.refresh_token(
    client_id=client_id,
    auth=auth,
    token_url=token_url,
    refresh_token=data["refresh_token"],
)

st_refreshed_token = '"{}"'.format(refreshed_token)
j_refreshed_token = json.loads(st_refreshed_token)
main.r.set("token", j_refreshed_token)

#https://twitter.com/uvkollen
city = "Stockholm"
payload_text = tweet_text.create_tweet(city)
payload = {"text": f"{payload_text}"}

main.post_tweet(payload, refreshed_token)

