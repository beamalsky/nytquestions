import requests
import nltk
import json
from pprint import pprint
from datetime import datetime, timezone
from dateutil import parser

import pandas as pd

nltk.download('punkt')

def get_questions(NYT_API_KEY, seconds_interval):
    BASE_URL = 'https://api.nytimes.com/svc/topstories/v2'
    included_fields = ['title', 'abstract']

    response = requests.get(
        'https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=' + NYT_API_KEY
    )

    questions = []

    for result in response.json()['results']:
        for field in included_fields:
            sentences = nltk.sent_tokenize(result[field])
            for sentence in sentences:
                if sentence[-1] == '?':
                    questions.append(sentence)

    return questions
