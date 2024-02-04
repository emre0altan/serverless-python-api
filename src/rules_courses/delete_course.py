from ..handler_db import dynamodb, get_courses_db
from ..handler_request_wrapper import delete_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

courses = get_courses_db()
identifier = "Delete Course"

def query_builder(request_data):
    id = request_data.get('id')
    query = { 'id': id }
    return query

def _delete_course(query):
    return delete_item_wrapper(dynamodb.Table(courses), query, identifier)

def delete_course():
    return rule_wrapper(_delete_course, query_builder, identifier, requ_session=True, requ_admin=True)