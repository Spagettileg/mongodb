import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI") # All python constants written in CAPITAL LETT£RS
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url): # **Mongo connection string**
    try:
        conn = pymongo.MongoClient(url) # conn = connection
        print("Mongo is connected!!")
        return conn 
    except pymongo.errors.ConnectionFailure as e: # e = error message
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI) # Function being called 'conn' & 'MONGO_URI' = argument

coll = conn[DBS_NAME][COLLECTION_NAME] # Collection has been set

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}}) # Update_many method applied

""" 
Sending a dictionary with the nationality of american. 
"""
documents = coll.find({'nationality': 'american'}) # New variable called 'documents' & prints everything on the database

for doc in documents: # A MongoDB object will get returned. Repeat process, then print document to screen
    print(doc)
    

    

