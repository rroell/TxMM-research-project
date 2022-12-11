from snscrape.modules.twitter import TwitterTweetScraper
import pandas as pd
from preprocess import replacePlaceholders

LIMIT = 10
# TODO: rewrite emotionNL database to readable
with open("EmotioNL_tweets.txt") as f:
    next(f)  # skip header
    tweets = []
    i = 0
    for line in f:
        line_splitted = line.split()
        tweet_id = line_splitted[1][2:-2]
        category = line_splitted[-1]

        # TODO: check if this is needed, can it not be inserted directly into huggingface? read emails!!
        try:
            for tweet in TwitterTweetScraper(tweet_id).get_items():
                text = replacePlaceholders(tweet.content)
                tweets.append([tweet_id, text, category])
                print(tweet_id, text, category)
        except:
            print("This tweet does not exist:", tweet_id)
        i += 1
        if i > LIMIT:
            break
    df = pd.DataFrame(tweets, columns=["Tweet_id", "Text", "Category"])
    df.to_csv("EmotioNL_tweets.csv")

    print("- - - Finished - - -")
