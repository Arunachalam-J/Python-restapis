from pymongo import MongoClient
from app.logging.log import logger
from app.config.config import get_config
# We have singleton class

class Mongo():
    __instance = None    
    
    def __new__(cls,*arg,**karg):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self,host,port) -> None:
        self.client = MongoClient(host=get_config()["mongodbHost"],
                                  port=get_config()["mongodbPort"])

    def get_client(self) -> MongoClient:
        return self.client
    
    def __del__(self):
        self.client.close()
        Mongo.__instance == None
        del(self)
        