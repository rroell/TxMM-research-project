# © Roel Duijsings
from getTweets import getTweets

query = "(Hebe OR hebe) lang:nl until:2022-10-21 since:2022-10-17"
maxTweets = 10
raw_data = getTweets(query, maxTweets)

# Sort dates in chronological order
raw_data.sort_values(by='Date', inplace=True)