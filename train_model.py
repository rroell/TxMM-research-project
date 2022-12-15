from transformers import (
    RobertaTokenizer,
    RobertaForSequenceClassification,
    Trainer,
    AutoTokenizer,
    AutoModelForSequenceClassification,
)
from collect_text_EmotioNL import preprocess_EmotioNL
from transformers import TrainingArguments
import numpy as np
from datasets.load import load_dataset


def tokenize_function(tweet):
    return tokenizer(tweet["text"], padding="max_length", truncation=True)


tokenizer = AutoTokenizer.from_pretrained("pdelobelle/robbert-v2-dutch-base")
model = AutoModelForSequenceClassification.from_pretrained(
    "pdelobelle/robbert-v2-dutch-base", num_labels=6
)
# tokenizer = RobertaTokenizer.from_pretrained("pdelobelle/robbert-v2-dutch-base")
# model = RobertaForSequenceClassification.from_pretrained(
#     "pdelobelle/robbert-v2-dutch-base", num_labels=1
# )
# dataset = Dataset.from_pandas(preprocess_EmotioNL())
dataset = load_dataset("csv", data_files="EmotioNL_tweets_10.csv", split="train")
# print(dataset[0])


tokenized_dataset = dataset.map(tokenize_function, batched=True)
# tokenized_dataset = tokenized_dataset.remove_columns(dataset["train"].column_names)
# print(tokenized_dataset.column_names)
# print(tokenized_dataset[0:3])
training_args = TrainingArguments(output_dir="test_trainer")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'], #TODO: deze dataset komt niet goed door! check format!
    tokenizer=tokenizer,
)

trainer.train()
# TODO: train model
