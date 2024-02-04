from ..handler_db import dynamodb, get_courses_db
from ..handler_request_wrapper import put_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

courses = get_courses_db()
identifier = "Put Course"

def query_builder(request_data):
    id = request_data.get('id')
    code = request_data.get('code')
    name = request_data.get('name')
    query = { 'id': id, 'code': code, 'name': name }
    return query

def _put_course(query):
    return put_item_wrapper(dynamodb.Table(courses), query, identifier)

def put_course():
    return rule_wrapper(_put_course, query_builder, identifier, requ_session=True, requ_admin=True)