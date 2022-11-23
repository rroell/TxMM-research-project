from transformers import RobertaTokenizer, RobertaForSequenceClassification


def runModel():
    tokenizer = RobertaTokenizer.from_pretrained(
        "pdelobelle/robbert-v2-dutch-base")
    model = RobertaForSequenceClassification.from_pretrained(
        "pdelobelle/robbert-v2-dutch-base")
    return model


runModel()
