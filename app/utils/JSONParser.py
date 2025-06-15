import json
import re
import unicodedata

def cleanJson(rawString):
    cleaned = re.sub(r"^```json\s*|\s*```$", "", rawString.strip(), flags=re.IGNORECASE)
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        data = {}
    return data