from transformers import pipeline
    
classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', top_k=None)
prediction = classifier("It has been a tough week. I lost my job, and the bills keep piling up. The rainy weather outside seems to mirror my mood. I miss the days when everything was going well. Sometimes life can be so unfair.", )
print(prediction[0][0])