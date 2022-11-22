from getTweets import getTweets


# © Roel Duijsings

print("Start main.py")

query = "(Hebe OR hebe) lang:nl until:2022-10-21 since:2022-10-17"
maxTweets = 10
df = getTweets(query, maxTweets)
print(df)
