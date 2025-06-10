from datetime import datetime

from app.services.StoreServices.QueryStorageBase import QueryStorageBase
from flask import current_app
from app.models.Request import Request
from app.services.ParserServices import RequestParser

RESULT_STORAGE : QueryStorageBase = None

def ParseRequestData(dataRaw):
    current_app.logger.info("Parsing payload")
    request = RequestParser.ParseRequest(dataRaw)
    data = { "request": request , "status": "PENDING", "status_time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    current_app.logger.info("Parsing complete")
    current_app.logger.info("Storing request")
    data = RESULT_STORAGE.storeQuery(data)
    current_app.logger.info("Storing complete")
    return data

def GetRequestData(id):
    return RESULT_STORAGE.getQuery(id)
    
def GetPendingRequestData():
    return RESULT_STORAGE.getPendingQuery()

def GetPromptCompletedData():
    return RESULT_STORAGE.getCompletedPrompt()
    

def SaveProcessedData(data):
    RESULT_STORAGE.storeExistingQuery(data)