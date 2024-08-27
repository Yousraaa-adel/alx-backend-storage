/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    documets = list(mongo_collection.find());
    if not documents:
        return []
    else:
        return documents
