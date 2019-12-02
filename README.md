# 🗞 nytquestions

What questions is the New York Times asking today?

A Twitter bot inspired by [this tweet](https://twitter.com/blprnt/status/1201124570155159552) from Jer Thorp, as well as [@NYT_first_said](https://twitter.com/nyt_first_said) and [@nyt_diff](https://twitter.com/nyt_diff). Checks the [Times Wire API](https://developer.nytimes.com/docs/timeswire-product/1/overview) every 10 minutes for new questions.

Uses Python, tweepy, and Heroku. S/o to [this post](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39) by [Emily Cain](https://emcain.github.io/) for the guiding method.

## Requirements

- [Docker](https://www.docker.com/)


## Running the app locally

To get started, run the following from your terminal:

1. Clone this repository and `cd` into your local copy.

  ```bash
  git clone git@github.com:beamalsky/nytquestions.git
  cd nytquestions
  ```

2. Switch the `LOCAL_DEVELOPMENT` variable in `bot.py` to `False`

3. Rename `secrets_example.py` to `secrets.py`:

  ```bash
  mv secrets_example.py secrets.py
  ```

4. You'll need your own [Twitter](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens) and [NYT](https://developer.nytimes.com/) API keys. Get them and fill them in to your new `secrets.py` file.

5. Run the app locally!

  ```bash
  docker-compose run --rm app python bot.py
  ```
