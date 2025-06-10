from abc import ABC, abstractmethod

class QueryStorageBase:

    @abstractmethod
    def storeQuery(self, data):
        pass
    
    @abstractmethod
    def getQuery(self, id):
        pass

    @abstractmethod
    def getPendingQuery(self):
        pass

    @abstractmethod
    def getCompletedPrompt(self):
        pass

    @abstractmethod
    def storeExistingQuery(self, data):
        pass