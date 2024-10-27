from fastapi import APIRouter
from textblob import TextBlob
from fastapi.responses import JSONResponse

router = APIRouter()

# Dictionary for simple responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I’m doing well! And you?",
    "what are you doing": "I’m helping people, just like now 😊.",
    "bye": "Goodbye! It was nice talking to you."
}


def analyze_sentiment(message: str) -> str:
    """Analyzes the sentiment of a message and returns an appropriate response.

    Args:
        message (str): The message provided by the user. Example: "I love this service!"

    Returns:
        str: A response based on the sentiment of the message.
             - Positive sentiment: "I'm glad to hear that!"
             - Negative sentiment: "I'm sorry to hear that."
             - Neutral sentiment: "Thank you for the information! How can I assist you further?"
    """

    blob = TextBlob(message)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "I'm glad to hear that!"
    elif sentiment < 0: 
        return "I'm sorry to hear that."
    else:  
        return "Thank you for the information! How can I assist you further?"


@router.get("/chat")
async def chat(message: str):
    """Processes the user's message and returns a response.

    Args:
        message (str): The user's message sent via a GET request. Example: "Hello"

    Returns:
        JSONResponse: A JSON response containing the bot’s reply. Example:
                       {
                         "response": "Hello! How can I assist you today?"
                       }

    Behavior:
        1. Converts the message to lowercase for keyword matching.
        2. If a predefined keyword from the `responses` dictionary is found,
           it returns the corresponding response.
        3. If no keyword matches, it analyzes the sentiment of the message
           using the `analyze_sentiment()` function and returns a sentiment-based response.
    """
    message_lower = message.lower()

    for keyword, response in responses.items():
        if keyword in message_lower:
            return JSONResponse(content={"response": response})

    sentiment_response = analyze_sentiment(message)
    return JSONResponse(content={"response": sentiment_response})
