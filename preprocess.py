# © Roel Duijsings

import snscrape.modules.twitter as sntwitter
import pandas as pd


def preprocess(query, maxTweets):
    df = getTweets(query, maxTweets)
    df['Text'] = df["Text"].map(replacePlaceholders)
    return df


def getTweets(query, maxTweets):
    """
    Gather tweets from Twitter API. Query and max nr of tweets are set here. 

    Returns a DataFrame that is in reverse order of date. Writes df to tweets.csv file.
    """
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == maxTweets:
            break
        else:
            tweets.append([tweet.date, tweet.user.username,
                          tweet.content, tweet.url])

    df = pd.DataFrame(tweets, columns=["Date", "Username", "Text", "Url"])
    df.index.name = "id"

    # to save to csv
    df.to_csv("tweets.csv")

    return df


def replacePlaceholders(tweet):
    """
    Replace username and URL in tweet text by @USER and HTTP
    """
    new_tweet = []
    for word in tweet.split(" "):
        word = '@USER' if word.startswith('@') and len(word) > 1 else word
        word = 'HTTP' if word.startswith('http') else word
        new_tweet.append(word)
    return " ".join(new_tweet)
