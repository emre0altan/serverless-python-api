from ..handler_db import dynamodb, get_departments_db
from ..handler_request_wrapper import scan_table_wrapper
from ..handler_rule_wrapper import rule_wrapper

departments = get_departments_db()
identifier = "Get Departments"

def query_builder(request_data):
    return {'placeholder_key' : 'placeholder_value'}

def _get_departments(query):
    return scan_table_wrapper(dynamodb.Table(departments), "id", identifier)

def get_departments():
    return rule_wrapper(_get_departments, query_builder, identifier, requ_session=True, requ_admin=False)