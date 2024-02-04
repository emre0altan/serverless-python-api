from ..handler_db import dynamodb, get_courses_db
from ..handler_request_wrapper import update_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

courses = get_courses_db()
identifier = "Update Course"

def query_builder(request_data):
    id = request_data.get('id')
    code = request_data.get('code')
    name = request_data.get('name')
    query = { 'id': id, 'code': code, 'name': name }
    return query

def _update_course(query):
    return update_item_wrapper(dynamodb.Table(courses), 
                               key={'id': query['id']},
                               upExp="set #cd=:c, #nm=:n",
                               expAttr={
                                       ':c' : query['code'],
                                       ':n' : query['name']
                               }, 
                               expAttrName={
                                    '#cd': 'code',
                                    '#nm': 'name', 
                               },identifier=identifier)

def update_course():
    return rule_wrapper(_update_course, query_builder, identifier, requ_session=True, requ_admin=True)