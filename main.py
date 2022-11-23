# © Roel Duijsings
from preprocess import preprocess
from transformers import pipeline, RobertaForSequenceClassification, RobertaTokenizer

# PARAMETERS
query = "(Hebe OR hebe) lang:nl until:2022-10-21 since:2022-10-17"
maxTweets = 10

# PREPROCESS DATA
# data = preprocess(query, maxTweets)

# MODEL AND TOKENIZER
tokenizer = RobertaTokenizer.from_pretrained("pdelobelle/robbert-v2-dutch-base")
model = RobertaForSequenceClassification.from_pretrained(
    "pdelobelle/robbert-v2-dutch-base", id2label={0: "negative", 1: "positive"} # change labels
)

# COMPUTE EMOTIONS
emotion = pipeline("text-classification", model=model, tokenizer=tokenizer)
# emotion_labels = emotion("Ik ben verdrietig!")

emotion_labels = emotion("Ik ben super boos op jou")
print(emotion_labels)
