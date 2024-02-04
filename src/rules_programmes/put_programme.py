from ..handler_db import dynamodb, get_programmes_db
from ..handler_request_wrapper import put_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

programmes = get_programmes_db()
identifier = "Put Programme"

def query_builder(request_data):
    id = request_data.get('id')
    name = request_data.get('name')
    query = { 'id': id, 'name': name }
    return query
    
def _put_programme(query):
    return put_item_wrapper(dynamodb.Table(programmes), query, identifier)

def put_programme():
    return rule_wrapper(_put_programme, query_builder, identifier, requ_session=True, requ_admin=True)