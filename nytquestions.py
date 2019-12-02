import requests
import nltk

nltk.download('punkt')


def get_questions(NYT_API_KEY):
    included_fields = ['title', 'abstract']

    response = requests.get(
        'https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key='
        + NYT_API_KEY
    )

    questions = []

    for result in response.json()['results']:
        for field in included_fields:
            sentences = nltk.sent_tokenize(result[field])
            for sentence in sentences:
                if sentence[-1] == '?':
                    questions.append(sentence)

    return questions
