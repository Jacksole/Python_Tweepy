#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py

import logging
import time

import tweepy

from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()
            return


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
