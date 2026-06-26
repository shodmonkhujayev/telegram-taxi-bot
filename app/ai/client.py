from google import genai

from app.config import config


client = genai.Client(
    api_key=config.GEMINI_API_KEY
)
