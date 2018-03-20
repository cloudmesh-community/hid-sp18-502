from pymongo import MongoClient
# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient(port=27017)
# Set the db object to point to the business database
db=client.variables
# Showcasing the count() method of find, count the total number of 5 ratings

def get_var():
	l = list()
	for each in db.Var.find():
		l.append((each['name'], each['value'], each['type']))
	return l

def get_var_by_id_mongo(id):
	for each in db.Var.find({'name':id}):
		return (each['name'], each['value'], each['type'])
