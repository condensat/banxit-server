import connexion
import six

from banxit import util


def ping_get():  # noqa: E501
    """Server heartbeat operation

    This operation shows how to override the global security defined above, as we want to open it up for all users. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def user_id_account_delete(id):  # noqa: E501
    """delete a account account

    This operation delete a account account. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_account_get(id):  # noqa: E501
    """retrieve account accounts information

    This operation retrieve the account accounts information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_account_post(id):  # noqa: E501
    """create an account account

    This operation creates a account account with supplied valid information # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_account_put(id):  # noqa: E501
    """update a account account

    This operation update a account account. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_card_txs_get(id):  # noqa: E501
    """retrieve card account information

    This operation retrieve the card account information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_card_txs_post(id):  # noqa: E501
    """create a transaction

    This operation creat a transaction. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_card_txs_txid_get(id, txid):  # noqa: E501
    """retrieve card account information

    This operation retrieve the card account information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str
    :param txid: identifier of the transaction
    :type txid: int

    :rtype: None
    """
    return 'do some magic!'


def user_id_crypto_delete(id):  # noqa: E501
    """delete a crypto account

    This operation delete a crypto account. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_crypto_get(id):  # noqa: E501
    """retrieve crypto account information

    This operation retrieve the crypto account information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_crypto_post(id):  # noqa: E501
    """create an crypto account

    This operation creates a crypto account with supplied valid information # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_crypto_put(id):  # noqa: E501
    """update a crypto account

    This operation update a crypto account. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_crypto_txs_get(id):  # noqa: E501
    """retrieve crypto account information

    This operation retrieve the crypto account information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_crypto_txs_post(id):  # noqa: E501
    """create a transaction

    This operation creat a transaction. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_crypto_txs_txid_get(id, txid):  # noqa: E501
    """retrieve crypto account information

    This operation retrieve the crypto account information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str
    :param txid: identifier of the transaction
    :type txid: int

    :rtype: None
    """
    return 'do some magic!'


def user_id_delete(id):  # noqa: E501
    """delete a user

    delete a user # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_get(id):  # noqa: E501
    """retrieve user informations

    retrieve user informations # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_logout_get(id):  # noqa: E501
    """log a user out

    this operation logs a user out # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_put(id):  # noqa: E501
    """update user informations

    update user informations with a valid json form supplied # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_txs_get(id):  # noqa: E501
    """retrieve account account information

    This operation retrieve the account account information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_txs_post(id):  # noqa: E501
    """create a transaction

    This operation creat a transaction. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def user_id_txs_txid_get(id, txid):  # noqa: E501
    """retrieve account account information

    This operation retrieve the account account information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str
    :param txid: identifier of the transaction
    :type txid: int

    :rtype: None
    """
    return 'do some magic!'


def user_login_get():  # noqa: E501
    """log a user in

    this operation logs a user in with apropriate openid/oauth2 credentials # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def users_id_card_delete(id):  # noqa: E501
    """delete a card account

    This operation delete a card account. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def users_id_card_get(id):  # noqa: E501
    """retrieve card accounts information

    This operation retrieve the card accounts information of the user. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def users_id_card_post(id):  # noqa: E501
    """create an card account

    This operation creates a card account with supplied valid information # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def users_id_card_put(id):  # noqa: E501
    """update a card account

    This operation update a card account. # noqa: E501

    :param id: Name of the user to get
    :type id: str

    :rtype: None
    """
    return 'do some magic!'
