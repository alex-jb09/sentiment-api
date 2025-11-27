from langchain_openai import ChatOpenAI

def analyze_sentiment(text: str):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = f"""
    Analyze the sentiment of the following text.
    Return a JSON object with:

    - sentiment: positive / negative / neutral
    - explanation: short reasoning

    Text: "{text}"
    """

    response = llm.invoke(prompt)
    return response.content
