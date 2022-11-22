# © Roel Duijsings

import snscrape.modules.twitter as sntwitter
import pandas as pd


def getTweets():
    """
    Gather tweets from Twitter API. Query and max nr of tweets are set here. 
    
    Returns a DataFrame that is in reverse order of date. Writes df to tweets.csv file.
    """
    print("----------------------------------")
    print("      getTweets.py started")
    print("----------------------------------")

    query = "(Hebe OR hebe) lang:nl until:2022-10-21 since:2022-10-17"
    tweets = []
    limit = 10

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username,
                          tweet.content, tweet.url])

    df = pd.DataFrame(tweets, columns=["Date", "Username", "Tweet", "Url"])
    df.index.name = "id"

    # to save to csv
    df.to_csv("tweets.csv")

    print(f"Number of tweets collected: {len(df)}")
    print("----------------------------------")
    print("      getTweets.py finished")
    print("----------------------------------")
    return df
