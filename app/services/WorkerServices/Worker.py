import threading
import time

from flask import current_app

from app.services.StoreServices.QueryStorageBase import QueryStorageBase
from app.services.QueryServices import GetPendingRequestData, SaveProcessedData, GetPromptCompletedData
from app.services.PromptServices import writePrompt, sendPrompt

def StartPendingWorker(app,promptWriter):
    worker_thread = threading.Thread(target=ProcessPending, args=(app,promptWriter), daemon=True)
    worker_thread.start()

def StartPromptWorker(app, promptSender):
    worker_thread = threading.Thread(target=ProcessPrompt, args=(app,promptSender), daemon=True)
    worker_thread.start()

def ProcessPending(app, promptWriter):
    with app.app_context():
        current_app.logger.info("Starting Pending Worker")
        while True:
            data = GetPendingRequestData()
            if data is None:
                current_app.logger.info("No pending requests. Sleeping")
                time.sleep(2)
            else:
                current_app.logger.info(f"Working on query: {data}")
                writePrompt(data, promptWriter)
                current_app.logger.info("Processed. Saving")
                SaveProcessedData(data)

def ProcessPrompt(app, promptSender):
    with app.app_context():
        current_app.logger.info("Starting Prompt Worker")
        while True:
            data = GetPromptCompletedData()
            if data is None:
                current_app.logger.info("No pending prompts. Sleeping")
                time.sleep(2)
            else:
                current_app.logger.info(f"Sending prompt : {data}")
                sendPrompt(data, promptSender)
                current_app.logger.info(f"Processed. Saving")
                SaveProcessedData(data)