from ..handler_db import dynamodb, get_users_db
from ..handler_request_wrapper import update_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

users = get_users_db()
identifier = "Update User"

def query_builder(request_data):
    user_id = request_data.get('client_user_id')
    device_id = request_data.get('device_id')
    first_name = request_data.get('first_name')
    last_name = request_data.get('last_name')
    email = request_data.get('email')
    query = { 'user_id': user_id, 'device_id': device_id, 'first_name': first_name, 'last_name': last_name, 'email': email }
    return query

def _update_user(query):
    return update_item_wrapper(dynamodb.Table(users), 
                               key={'user_id': query['user_id']},
                               upExp="set #did=:d, #fn=:f, #ln=:l, #em=:e",
                               expAttr={
                                   ':d' :  query['device_id'],
                                   ':f' :  query['first_name'],
                                   ':l' :  query['last_name'],
                                   ':e' :  query['email'],
                               },
                               expAttrName={
                                   '#did': 'device_id', '#fn': 'first_name', '#ln': 'last_name', '#em': 'email', 
                               }, identifier=identifier)

def update_user():
    return rule_wrapper(_update_user, query_builder, identifier, requ_session=True, requ_admin=True)