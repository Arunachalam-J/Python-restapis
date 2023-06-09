from pymongo import MongoClient
from functools import cache

# We have singleton class

class Mongo():
    __instance = None    
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self,host,port) -> None:
        self.client = MongoClient(host,port)

    def get_client(self) -> MongoClient:
        return self.client
    
    def __del__(self):
        self.client.close()
        Mongo.__instance == None
        


def get_client(host:str,
               port: int) -> MongoClient:
    return Mongo(host,port).get_client()
