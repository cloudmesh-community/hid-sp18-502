import connexion
import six
from pymongo import MongoClient

from swagger_server.models.var import VAR  # noqa: E501
from swagger_server import util

client = MongoClient('localhost', 27017)
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


def get_var_by_id(id):  # noqa: E501
    """get_var_by_id

    Returns value of a named variable identified by id # noqa: E501

    :param id: name of variable
    :type id: str
    :rtype: VAR
    """
    for each in db.Var.find({'name':id}):
		return VAR(each['name'], each['value'], each['type'])


def var_get():  # noqa: E501
    """var_get

    Returns list of variables # noqa: E501


    :rtype: List[VAR]
   	"""
    listofVar = []
    for each in db.Var.find():
	listofVar.append(VAR(each['name'], each['value'], each['type']))
    return listofVar 
