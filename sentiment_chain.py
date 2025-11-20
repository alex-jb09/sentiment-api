from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

def analyze_sentiment(text: str):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a sentiment analysis assistant."),
        ("human", "Analyze the sentiment of this text and return JSON with fields: sentiment, explanation.\nText: {text}")
    ])

    chain = prompt | llm

    result = chain.invoke({"text": text})
    return result.content
