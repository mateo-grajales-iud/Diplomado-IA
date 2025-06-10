from google import genai
from google.genai import types
from app.utils.AIConstants import GEMENI_2_FLASH
import os

API_KEY = os.getenv("GEMINI_2_FLASH_API_KEY")

def getResponse(data):
    model = GEMENI_2_FLASH
    systemInstruction = data["request"].role
    content = data["prompt"]
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model=model,
        config=types.GenerateContentConfig(
            system_instruction=systemInstruction
        ),
        contents=content
    )
    return response.text