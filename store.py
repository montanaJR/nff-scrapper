from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.pymongo_test  # or db = client['pymongo_test']
