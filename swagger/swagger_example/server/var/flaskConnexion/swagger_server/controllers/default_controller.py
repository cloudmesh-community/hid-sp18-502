import connexion
import six

from var_controller import *
from swagger_server.models.var import VAR  # noqa: E501
from swagger_server import util


def get_var_by_id(id):  # noqa: E501
    """get_var_by_id

    Returns info of variable by that id # noqa: E501

    :param id: name of variable
    :type id: str

    :rtype: VAR
    """
    return VAR(get_var_byid(id))


def var_get():  # noqa: E501
    """var_get

    Returns information of variable # noqa: E501


    :rtype: VAR
    """
    return VAR(get_var())
