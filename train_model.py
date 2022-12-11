from transformers import RobertaTokenizer, RobertaForSequenceClassification
from collect_text_EmotioNL import df

tokenizer = RobertaTokenizer.from_pretrained("pdelobelle/robbert-v2-dutch-base")
model = RobertaForSequenceClassification.from_pretrained(
    "pdelobelle/robbert-v2-dutch-base"
)


def tokenize_function(tweet):
    return tokenizer(tweet["text"], padding="max_length", truncation=True)


dataset = df
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# TODO: train model
