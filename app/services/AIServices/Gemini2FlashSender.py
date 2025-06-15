from google import genai
from google.genai import types
from app.utils.AIConstants import GEMENI_2_FLASH
import os
from datetime import datetime

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
    saveRequestResponse(data["prompt"], response.text, data["id"])
    return response.text

def saveRequestResponse(request, response, id):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"prompt_response_id_{id}_{timestamp}.txt"
    folder_name = "prompt log"
    folder_path = os.path.join(root_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    filepath = os.path.join(folder_path, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=== PROMPT ===\n")
        f.write(str(request) + "\n\n")
        f.write("=== RESPONSE ===\n")
        f.write(str(response))

    print(f"Archivo guardado en: {filepath}")