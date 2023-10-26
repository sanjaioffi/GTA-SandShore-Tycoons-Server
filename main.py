from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "You Successfully deployed your first api"}

