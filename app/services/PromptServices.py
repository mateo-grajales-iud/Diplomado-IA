from flask import current_app
from app.utils.Constants import *

from datetime import datetime

def writePrompt(data, promptWriter):
    current_app.logger.info(f"Writing prompt based on { data }")
    prompt = promptWriter(data)
    data["prompt"] = prompt
    data["status"] = CREATED_PROMPT
    data["status_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_app.logger.info(f"Prompt written: { data }")

def sendPrompt(data, promptSender):
    current_app.logger.info(f"Sending prompt { data }")
    response = promptSender(data)
    data["response"] = response
    data["status"] = COMPLETED
    data["status_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_app.logger.info(f"Response received: { data }")