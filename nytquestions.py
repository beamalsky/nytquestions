import requests
import nltk
import json
from pprint import pprint
from datetime import datetime, timezone

nltk.download('punkt')

def get_questions(NYT_API_KEY, seconds_interval):
    BASE_URL = 'https://api.nytimes.com/svc/topstories/v2'
    included_fields = ['title', 'abstract']

    response = requests.get(
        'https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=' + NYT_API_KEY
    )

    # Get recent articles. Refresh interval should be set in bot.py
    now = datetime.now(timezone.utc)
    time_format = '%Y-%m-%dT%H:%M:%S%z'
    new_results = [
        x for x in response.json()['results']
        if ((now - datetime.strptime(x['updated_date'], time_format)).seconds < seconds_interval)
    ]

    questions = []

    for result in new_results:
        for field in included_fields:
            sentences = nltk.sent_tokenize(result[field])
            for sentence in sentences:
                if sentence[-1] == '?':
                    questions.append(sentence)

    return questions
