from ..handler_db import dynamodb, get_departments_db
from ..handler_request_wrapper import put_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

departments = get_departments_db()
identifier = "Put Department"

def query_builder(request_data):
    id = request_data.get('id')
    programme_id = request_data.get('programme_id')
    name = request_data.get('name')
    courses = request_data.get('courses')
    query = { 'id': id, 'programme_id': programme_id, 'name': name, 'courses': courses }
    return query

def _put_department(query):
    return put_item_wrapper(dynamodb.Table(departments), query, identifier)

def put_department():
    return rule_wrapper(_put_department, query_builder, identifier, requ_session=True, requ_admin=True)