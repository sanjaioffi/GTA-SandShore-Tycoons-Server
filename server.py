from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    # classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', top_k=None)
    # prediction = classifier("I love using transformers. The best part is wide range of support and its easy to use", )
    # return prediction[0][0]
    # print(prediction)
    return {"hello": "You Successfully deployed your first api"}

