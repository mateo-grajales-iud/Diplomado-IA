from app.services.StoreServices.QueryStorageBase import QueryStorageBase
from flask import current_app

from app.utils.Constants import *

class QueryStorageCache(QueryStorageBase):

    def __init__(self):
        self.results = {}

    def storeQuery(self, data):
        id = len(self.results)
        data["id"] = id
        data["status"] = PENDING
        self.results[id] = data

        return data

    def getQuery(self, id):
        return self.results.get(id, None)
    
    def getPendingQuery(self):
        return next((value for value in self.results.values() if value.get("status", None) == PENDING), None)
    
    def getCompletedPrompt(self):
        return next((value for value in self.results.values() if value.get("status", None) == CREATED_PROMPT), None)
    
    def storeExistingQuery(self, data):
        self.results[data["id"]] = data
        pass