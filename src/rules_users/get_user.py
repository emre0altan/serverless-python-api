from ..handler_db import dynamodb, get_users_db
from ..handler_request_wrapper import get_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

users = get_users_db()
identifier = "Get User"

def query_builder(request_data):
    user_id = request_data.get('client_user_id')
    query = { 'user_id': user_id }
    return query

def _get_user(query):
    return get_item_wrapper(dynamodb.Table(users), query, identifier)

def get_user():
    return rule_wrapper(_get_user, query_builder, identifier, requ_session=True, requ_admin=True)