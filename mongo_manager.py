import pymongo
from mongo_config import CLIENT_URI


class MongoSingleton(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("Creating new instance")
            cls.__instance = super(MongoSingleton, cls).__new__(cls)

            # client connection only made once
            cls.client = pymongo.MongoClient(CLIENT_URI)
            cls.db = cls.client["witness-vhix"]
            print("Connection Successful")

        return cls.__instance
