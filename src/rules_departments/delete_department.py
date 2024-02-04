from ..handler_db import dynamodb, get_departments_db
from ..handler_request_wrapper import delete_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

departments = get_departments_db()
identifier = "Delete Department"

def query_builder(request_data):
    id = request_data.get('id')
    programme_id = request_data.get('programme_id')
    query = { 'id': id, 'programme_id': programme_id }
    return query

def _delete_department(query):
    return delete_item_wrapper(dynamodb.Table(departments), query, identifier)

def delete_department():
    return rule_wrapper(_delete_department, query_builder, identifier, requ_session=True, requ_admin=True)