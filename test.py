from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="pdelobelle/robbert-v2-dutch-base")
res = classifier("Ik ben heel blij om hier met <mask> samen te zijn")

print(res)
