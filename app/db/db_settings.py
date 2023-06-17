from pymongo import MongoClient
from app.logging.log import logger
from app.config.config import get_config
# We have singleton class

class Mongo():
    __instance = None    
    __client = None
    def __new__(cls,*arg,**karg):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self,host,port) -> None:
        if Mongo.__client is None:
            Mongo.__client = MongoClient(host=get_config()["mongodbHost"],
                                  port=get_config()["mongodbPort"])
        

    def get_client(self) -> MongoClient:
        return Mongo.__client
    
    def __del__(self):
        Mongo.__client.close()
        Mongo.__client= None
        Mongo.__instance == None
        del(self)
        