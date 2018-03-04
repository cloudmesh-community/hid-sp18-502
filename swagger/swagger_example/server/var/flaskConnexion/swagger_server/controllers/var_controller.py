from pymongo import MongoClient
# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient(port=27017)
# Set the db object to point to the business database
db=client.variables
# Showcasing the count() method of find, count the total number of 5 ratings

def get_var():
	for item in db.Var.find().limit(1):
		return [item['name'], item['value'], item['type']]

def get_var_byid(id):
	for item in db.Var.find({'name':id}).limit(1):
		return [item['name'], item['value'], item['type']]
