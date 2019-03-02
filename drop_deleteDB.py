# uncomment and use one by one

import pymongo # importing module
myclient = pymongo.MongoClient("localhost:27017") # connecting to DB


#Important: In MongoDB, a database is not created until it gets content!

# insert
"""nmDB = myclient.nameOfTheDB
collection_nm = myclient.nameOfCollection

_d = { "idno":37 ,"name": "John", "address": "Highway 37" }

x = nmDB.collection_nm.insert_one(_d)"""



# update
"""nmDB = myclient.nameOfTheDB
collection_nm = myclient.nameOfCollection

filtr = {'idno':37}
_d = { "idno":38 ,"name": "John", "address": "Highway 37" }

x = nmDB.collection_nm.update_one(filtr, {'$set':_d})"""


# delete

"""nmDB = myclient.nameOfTheDB
collection_nm = myclient.nameOfCollection
_d = {"name": "John", "address": "Highway 37" }
x = nmDB.collection_nm.delete_one(_d)
print("Deleted sucessfully!")"""

# delete by any key value
"""nmDB = myclient.nameOfTheDB
collection_nm = myclient.nameOfCollection
_d = {'_id':944, 'idno':37, "name": "John", "address": "Highway 37" }
x = nmDB.collection_nm.delete_one({}) # this will delete oldest value from collection
print("Deleted sucessfully!")
"""

# drop
nmDB = myclient.nameOfTheDB
collection_nm = myclient.nameOfCollection
nmDB.collection_nm.drop()

# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
# The drop() method returns true
# if the collection was dropped successfully, and false if the collection does not exist.


