# © Roel Duijsings

import snscrape.modules.twitter as sntwitter
import pandas as pd


def preprocess(query, maxTweets):
    """
    Preprocess the tweets:
    - collects them from Twitter API,
    - replaces username and URL by placeholders,

    Returns a DataFrame["Date", "Username", "Raw_text", "Url","Text"]
    """
    df = getTweets(query, maxTweets)
    df["Text"] = df["Raw_text"].map(replacePlaceholders)

    return df


def getTweets(query, maxTweets):
    """
    Gather tweets from Twitter API. Query and maxTweets are used here.

    Returns a DataFrame that is in reversed chronological order.
    """
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) >= maxTweets:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.url])

    df = pd.DataFrame(tweets, columns=["Date", "Username", "Raw_text", "Url"])
    df.index.name = "id"

    return df


def replacePlaceholders(tweet):
    """
    Replace username and URL in tweet text by @USER and HTTP
    """
    new_tweet = []
    for word in tweet.split(" "):
        if word.startswith("@") and len(word) > 1:
            word = "@USER"
        elif word.startswith("http"):
            word = "HTTP"
        new_tweet.append(word)
    return " ".join(new_tweet)
