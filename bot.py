import time
import sys
import tweepy

from nytquestions import get_questions
from secrets import *

# use this for production; set vars in heroku dashboard
# from os import environ
# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']

# Check for new questions every 15 minutes
seconds_interval = 15 * 60

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    questions = get_questions(seconds_interval)
    print(questions)

    for question in questions:
        try:
            api.update_status(str(question))
        except tweepy.error.TweepError:
            print("Duplicate found. Passing...")

    time.sleep(seconds_interval)
