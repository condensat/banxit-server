import connexion
from connexion import NoContent

from banxit.app.extensions import db
from banxit.models.user import User  # noqa: E501


def user_post(user):  # noqa: E501
    """Creates a user

    This operation creates a user with a valid json form supplied # noqa: E501

    :param user: user informations
    :type user: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    db.session.add(user)
    return NoContent, 201
