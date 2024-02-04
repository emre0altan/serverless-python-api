from ..handler_db import dynamodb, get_programmes_db
from ..handler_request_wrapper import update_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

programmes = get_programmes_db()
identifier = "Update Programme"

def query_builder(request_data):
    id = request_data.get('id')
    name = request_data.get('name')
    query = { 'id': id, 'name': name }
    return query


def _update_programme(query):
    return update_item_wrapper(dynamodb.Table(programmes), 
                               key={'id': query['id']},
                               upExp="set #nm=:d",
                               expAttr={
                                   ':d' :  query['name'],
                               },
                               expAttrName={
                                   '#nm': 'name'
                               }, identifier=identifier)

def update_programme():
    return rule_wrapper(_update_programme, query_builder, identifier, requ_session=True, requ_admin=True)