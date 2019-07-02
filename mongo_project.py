import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI") # All python constants written in CAPITAL LETT£RS
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url): # **Mongo connection string**
    try:
        conn = pymongo.MongoClient(url) # conn = connection
        return conn 
    except pymongo.errors.ConnectionFailure as e: # e = error message
        print("Could not connect to MongoDB: %s") % e
        
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    
    option = input("Enter Option: ") # New variable called option
    return option
    
def main_loop(): # Loop ensures the user is returned to the menu
    while True: # The while True loop will ensure an indefinite loop
        option = show_menu() # Result of the 'show_menu' stored under 'option' variable
        if option == "1":
            print("You have selected Option 1")
        elif option == "2":
            print("You have selected Option 2")
        elif option == "3":
            print("You have selected Option 3")
        elif option == "4":
            print("You have selected Option 4")
        elif option == "5":
            conn.close() # Maps to connection (conn) definition on row 44  
            break
        else:
            print("Invalid Option")
        print("") # Blank line

conn = mongo_connect(MONGODB_URI) # Function being called 'conn' & 'MONGO_URI' = argument

coll = conn[DBS_NAME][COLLECTION_NAME] # Collection has been set

main_loop() # call our main_loop, which will continue to display our menu and process the options.

