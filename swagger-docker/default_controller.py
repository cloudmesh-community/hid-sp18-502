import connexion
import six
from pymongo import MongoClient

from swagger_server.models.var import VAR  # noqa: E501
from swagger_server import util

import os
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
def get_database():
	ip = os.environ['MONGO_PORT_27017_TCP_ADDR']
	port = int(os.environ['MONGO_PORT_27017_TCP_PORT'])
	print str(ip) + ":" + str(port)
	client = MongoClient(ip, port)
	#client = MongoClient('localhost', 27017)
	db = client.variable

	n = ['variable1', 'variable2', 'variable3']
	v = ['3', 'Ankita', 'True']
	t = ['int', 'string', 'boolean']

	for x in range(len(n)):
		var = {
			'name': n[x],
			'value': v[x],
			'type': t[x]
		}
		result = db.Var.insert_one(var)
	return db


def get_var_by_id(id):  # noqa: E501
	db = get_database()
	for each in db.Var.find({'name':id}):
		return VAR(each['name'], each['value'], each['type'])


def var_get():  # noqa: E501
	db = get_database()
	listofVar = []
	for each in db.Var.find():
		listofVar.append(VAR(each['name'], each['value'], each['type']))
	return listofVar 
