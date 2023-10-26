from fastapi import FastAPI
app = FastAPI()
from transformers import pipeline

@app.get("/")
def hello():
    classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
    prediction = classifier("I love using transformers. The best part is wide range of support and its easy to use", )
    return prediction
    # print(prediction)
    # return {"hello": "You Successfully deployed your first api"}

