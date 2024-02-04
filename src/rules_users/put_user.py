from ..handler_db import dynamodb, get_users_db
from ..handler_request_wrapper import put_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

users = get_users_db()
identifier = "Put User"

def query_builder(request_data):
    user_id = request_data.get('user_id')
    device_id = request_data.get('device_id')
    first_name = request_data.get('first_name')
    last_name = request_data.get('last_name')
    email = request_data.get('email')
    query = { 'user_id': user_id, 'device_id': device_id, 'first_name': first_name, 'last_name': last_name, 'email': email }
    return query

def _put_user(query):
    return put_item_wrapper(dynamodb.Table(users), query, identifier)

def put_user():
    return rule_wrapper(_put_user, query_builder, identifier, requ_session=False, requ_admin=False)