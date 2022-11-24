# © Roel Duijsings
from preprocess import preprocess
from transformers import pipeline, RobertaForSequenceClassification, RobertaTokenizer, AutoModelForSequenceClassification
import torch

# PARAMETERS
query = "(Hebe OR hebe) lang:nl until:2022-10-21 since:2022-10-17"
maxTweets = 10

# PREPROCESS DATA
data = preprocess(query, maxTweets)

# MODEL AND TOKENIZER
tokenizer = RobertaTokenizer.from_pretrained("pdelobelle/robbert-v2-dutch-base")
model = RobertaForSequenceClassification.from_pretrained(
    "pdelobelle/robbert-v2-dutch-base", problem_type="multi_label_classification")#, id2label={0: "negative", 1: "positive"}) # change labels

print("Numlabels:", model.config.num_labels)  
# inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")

# with torch.no_grad():
#     logits = model(**inputs).logits

# predicted_class_id = logits.argmax().item()
# model.config.id2label[predicted_class_id]

# # COMPUTE EMOTIONS
emotion = pipeline('sentiment-analysis', model="pdelobelle/robbert-v2-dutch-base",top_k=None)
# emotion_labels = emotion("Ik ben verdrietig!")
# for tweet in 
label_scores = emotion("I love you")[0]  # type: ignore
print(label_scores)
print([(label_score['label'],label_score['score']) for label_score in label_scores])  # type: ignore
