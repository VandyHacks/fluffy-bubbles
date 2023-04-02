import pymongo
from mongo_config import CLIENT_URI
from datetime import datetime


def getNextNEvents(n):
    """
    Get the list of events from mongodb
    :param n: number of events to return
    """
    # todo: might want to restructure so that client connection is only made once throughout bot run
    client = pymongo.MongoClient(CLIENT_URI)
    db = client["witness-vhix"]
    print("Connection Successful")

    currentTime = datetime.now()

    events = [
        event
        for event in list(db.events.find().sort("startTime", pymongo.ASCENDING))
        if event["startTime"] < currentTime
    ]
    # python should handle things itself if n > number of events left

    client.close()

    return events[:n]
