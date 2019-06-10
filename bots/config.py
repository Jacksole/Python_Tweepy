# tweepy-bots/bots/config.py
import logging
import os

import tweepy

logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv("iTOXXK1fUNrKZs9NsAi25xQHl")
    consumer_secret = os.getenv(
        "fvXHoZYFN8vlrbWdXyVSTBcjlC0H3tKHkVKQmTK3KSBqeUH8nQ")
    access_token = os.getenv(
        "228125493-n1aNfibgceg5exq1NLi9ptk3DCzyIAUaRvIFmQz6")
    access_token_secret = os.getenv(
        "HI68fr3zB7HVK2H304GjhdwQnnFAW3qrAmFOQdS0y9Aio")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
