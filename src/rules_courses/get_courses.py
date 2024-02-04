from ..handler_db import dynamodb, get_courses_db
from ..handler_request_wrapper import scan_table_wrapper
from ..handler_rule_wrapper import rule_wrapper

courses = get_courses_db()
identifier = "Get Courses"

def query_builder(request_data):
    return {'placeholder_key' : 'placeholder_value'}

def _get_courses(query):
    return scan_table_wrapper(dynamodb.Table(courses), "id", identifier)

def get_courses():
    return rule_wrapper(_get_courses, query_builder, identifier, requ_session=True, requ_admin=False)