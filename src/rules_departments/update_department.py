from ..handler_db import dynamodb, get_departments_db
from ..handler_request_wrapper import update_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

departments = get_departments_db()
identifier = "Update Department"

def query_builder(request_data):
    id = request_data.get('id')
    programme_id = request_data.get('programme_id')
    name = request_data.get('name')
    courses = request_data.get('courses')
    query = { 'id': id, 'programme_id': programme_id, 'name': name, 'courses': courses }
    return query

def _update_department(query):
    return update_item_wrapper(dynamodb.Table(departments), 
                               key={'id': query['id'], 'programme_id': query['programme_id']},
                               upExp="set #nm=:d, #crs=:f",
                               expAttr={
                                   ':d' : query['name'],
                                   ':f' : query['courses']
                               },
                               expAttrName={
                                   '#nm': 'name',
                                   '#crs': 'courses',
                               },
                               identifier=identifier)

def update_department():
    return rule_wrapper(_update_department, query_builder, identifier, requ_session=True, requ_admin=True)
