# © Roel Duijsings
from preprocess import preprocess
from transformers import (
    pipeline,
    RobertaForSequenceClassification,
    RobertaTokenizer,
    AutoModelForSequenceClassification,
)
import torch
import time

# start timer
start_time = time.time()

# PARAMETERS
query = "(Hebe OR hebe) lang:nl until:2022-10-21 since:2022-10-17"
maxTweets = 10000

# PREPROCESS DATA
data = preprocess(query, maxTweets)
print(data.iloc[-1])
# MODEL AND TOKENIZER
# tokenizer = RobertaTokenizer.from_pretrained("pdelobelle/robbert-v2-dutch-base")

# data.to_csv("labels.csv")

# Finished
print("--- %s seconds ---" % (time.time() - start_time))
