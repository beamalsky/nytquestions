import requests
import nltk

from secrets import API_KEY

nltk.download('punkt')

def get_questions():
    BASE_URL = 'https://api.nytimes.com/svc/topstories/v2'
    included_fields = ['title', 'abstract']

    response = requests.get(
        'https://api.nytimes.com/svc/topstories/v2/home.json?api-key=' + API_KEY
    )

    questions = []

    for result in response.json()['results']:
        for field in included_fields:
            sentences = nltk.sent_tokenize(result[field])
            for sentence in sentences:
                if sentence[-1] == '?':
                    questions.append(sentence)

    return questions
