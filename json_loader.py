# importing json
import json
#importing pymongo library to access mongodb through our python code
from pymongo import MongoClient

# creating a Mongoclient object and connecting to the local mongo database called JAY_VAGHELA
myclient = MongoClient("mongodb://localhost:27017/")

# Assigning the database into a variable db and referring collection name NEW inside it
db = myclient["JAY_VAGHELA"]
Collection = db["NEW"]

# Through open command we are loading the JSON data TASK1 using the load function
# it returns  an iterable list of dictionaries.
with open('Task.json') as file:
    file_data = json.load(file)

# Insert many method will now insert that iterable list into collection NEW in one go
isinstance(file_data, list)
Collection.insert_many(file_data)