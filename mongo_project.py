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

def get_record(): # To locate record by only using first &/or last name only # **Helper Function**
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
        
    except:
        print("Error accessing the database")
        
    if not doc:
        print("Error! No results found") # To cover scenario where search renders zero result.
        
    return doc # Returns either a searched record or no record.

def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")
    
    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality} # Dictionary built for database
    
    try:
        coll.insert(new_doc) # True statement that allows document to be inserted
        print("") # Blank line
        print("Document inserted")
    except:
        print("Error accessing database") # False statement creates an error message

def find_record():
    doc = get_record() # sourced from helper function get_record
    if doc:
        print("")
        for k,v in doc.items(): # k = key, v = value
            if k != "_id": # We dont want the Mongo ID to be called here for security purposes.
                print(k.capitalize() + ": " + v.capitalize()) # 1st letter of data field to change to uppercase. 

def edit_record():
    doc = get_record()
    if doc:
        update_doc={}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ") 
                # generates a prompt to show the key and what [value has been set to]
                if update_doc[k] == "": # if no changes made to word, then data base preseves original value 
                    update_doc[k] = v
        try:
            coll.update_one(doc, {'$set': update_doc}) # Updates the document against the parameters set by the Dictionary
            print("")
            print("Document updated!")
            
        except:
            print("Error accessing the database")

def delete_record():
    doc = get_record() # sourced from helper function get_record
    if doc:
        print("")
        for k, v in doc.items(): # k = key, v = value
            if k != "_id": # We dont want the Mongo ID to be called here for security purposes.
                print(k.capitalize() + ": " + v.capitalize()) # 1st letter of data field to change to uppercase.
                
                print("")
                confirmation = input("Is this the document you want to delete?\nY or N > ") # Check with user on deletion accuracy
                print("")
                
                if confirmation.lower() == 'y':
                    try:
                        coll.remove(doc)
                        print("Document deleted!") # If User selected 'Y', then "Document deleted!"
                    except:
                        print("Error accessing the database")
                    
                else:
                    print("Document not deleted!") # Refers to User selecting 'N'

def main_loop(): # Loop ensures the user is returned to the menu
    while True: # The while True loop will ensure an indefinite loop
        option = show_menu() # Result of the 'show_menu' stored under 'option' variable
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close() # Maps to connection (conn) definition on row 44  
            break
        else:
            print("Invalid Option")
        print("") # Blank line

conn = mongo_connect(MONGODB_URI) # Function being called 'conn' & 'MONGO_URI' = argument

coll = conn[DBS_NAME][COLLECTION_NAME] # Collection has been set

main_loop() # call our main_loop, which will continue to display our menu and process the options.

