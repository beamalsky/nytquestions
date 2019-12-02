import time
import sys
import tweepy
from pprint import pprint

from nytquestions import get_questions

LOCAL_DEVELOPMENT = False

if LOCAL_DEVELOPMENT:
    from secrets import *

else:
    from os import environ

    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']
    NYT_API_KEY = environ['NYT_API_KEY']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

questions = get_questions(NYT_API_KEY)

for question in questions:
    q = str(question)

    try:
        api.update_status(q)
        print("New tweet posted: " + q)
    except tweepy.error.TweepError:
        print("Duplicate found: " + q)
