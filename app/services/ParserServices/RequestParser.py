from app.services.StoreServices.QueryStorageBase import QueryStorageBase
from app.models.Request import Request

def ParseRequest(data):
    validateData(data)
    result = Request(**data)
    return result

def validateData(data):
    #Only a prototype, no need to validate
    pass