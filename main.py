from fastapi import FastAPI
from pydantic import BaseModel
from sentiment_chain import analyze_sentiment

app = FastAPI(title="Sentiment Analysis API")

class TextInput(BaseModel):
    text: str

@app.post("/analyze-sentiment")
def sentiment_api(input: TextInput):
    response = analyze_sentiment(input.text)
    return {"result": response}
