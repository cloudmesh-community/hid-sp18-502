import connexion
import six

from swagger_server.models.lof import LOF  # noqa: E501
from swagger_server import util


def dir_get():  # noqa: E501
    """dir_get

    Returns list of files under root directory # noqa: E501


    :rtype: LOF
    """
    return 'do some magic!'


def get_file_by_id(id):  # noqa: E501
    """get_file_by_id

    Returns list of files under given directory # noqa: E501

    :param id: ID of directory to fetch
    :type id: str

    :rtype: LOF
    """
    return 'do some magic!'
