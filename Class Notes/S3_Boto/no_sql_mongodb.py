from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

db = client['tutorial']
coll = db['articles']

doc = {
    "title": "An article about MongoDB and Python",
    "author": "Marco",
    "publication_date": datetime.utcnow(),
    # more fields
}

doc_id = coll.insert_one(doc).inserted_id