import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(Hebe OR hebe) lang:nl until:2022-10-20 since:2022-10-17"
tweets = []
limit = 10

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])

df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])
print(df)

# to save to csv
# df.to_csv('tweets.csv')
