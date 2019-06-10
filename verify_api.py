import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("iTOXXK1fUNrKZs9NsAi25xQHl",
                           "fvXHoZYFN8vlrbWdXyVSTBcjlC0H3tKHkVKQmTK3KSBqeUH8nQ")
auth.set_access_token("228125493-n1aNfibgceg5exq1NLi9ptk3DCzyIAUaRvIFmQz6",
                      "HI68fr3zB7HVK2H304GjhdwQnnFAW3qrAmFOQdS0y9Aio")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
