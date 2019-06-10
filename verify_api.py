import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("OpWT31iXkOpQcNGOUHr0bXhIa",
                           "6ZRTo9kJYWYyrQkJRL9pEkO7ptGCsRyiVXOTP63YkwlCd6aVpn ")
auth.set_access_token("228125493-wCCJ08xJSqZumA67Edy1af8wEXVI13tpetLJWgkn",
                      "YJhvTjrVirgeHTYnxmW64SOO1SoZzG1gXKW0RJc0kpDsi")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
