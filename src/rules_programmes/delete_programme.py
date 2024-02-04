from ..handler_db import dynamodb, get_programmes_db
from ..handler_request_wrapper import delete_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

programmes = get_programmes_db()
identifier = "Delete Programme"

def query_builder(request_data):
    id = request_data.get('id')
    query = { 'id': id }
    return query

def _delete_programme(query):
    return delete_item_wrapper(dynamodb.Table(programmes), query, identifier)

def delete_programme():
    return rule_wrapper(_delete_programme, query_builder, identifier, requ_session=True, requ_admin=True)