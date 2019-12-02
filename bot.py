import time
import sys
import tweepy
from pprint import pprint

from nytquestions import get_questions

LOCAL_DEVELOPMENT = False

if LOCAL_DEVELOPMENT:
    from secrets import *

    # Check for new questions from the last day
    seconds_interval = 24 * 60 * 60

else:
    from os import environ

    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']
    NYT_API_KEY = environ['NYT_API_KEY']

    # Check for new questions every 5 minutes
    seconds_interval = 5 * 60

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    questions = get_questions(NYT_API_KEY, seconds_interval)
    print("Questions found: ")
    pprint(questions)

    for question in questions:
        try:
            api.update_status(str(question))
        except tweepy.error.TweepError:
            print("Duplicate found. Passing...")

    time.sleep(seconds_interval)
