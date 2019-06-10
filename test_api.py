import json

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("iTOXXK1fUNrKZs9NsAi25xQHl",
                           "fvXHoZYFN8vlrbWdXyVSTBcjlC0H3tKHkVKQmTK3KSBqeUH8nQ")
auth.set_access_token("228125493-n1aNfibgceg5exq1NLi9ptk3DCzyIAUaRvIFmQz6",
                      "HI68fr3zB7HVK2H304GjhdwQnnFAW3qrAmFOQdS0y9Aio")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

api.update_status("Test tweet from Tweepy Python")

user = api.get_user("MikezGarcia")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

api.create_friendship("realpython")

api.update_profile(description="I like Python")

tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

for block in api.blocks():
    print(block.name)

for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        tweet = json.loads(data)
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")


tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])

tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favorite()
    tweet.user.follow()

for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print(f"{tweet.user.name} said: {tweet.text}")
