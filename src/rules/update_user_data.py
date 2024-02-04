from ..handler_db import dynamodb, get_user_data_db
from ..handler_request_wrapper import update_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

users = get_user_data_db()
identifier = "Update User Data"

def query_builder(request_data):
    user_id = request_data.get('client_user_id')
    saved_data = request_data.get('saved_data')
    bought_exams = request_data.get('bought_exams')
    finished_exams_data = request_data.get('finished_exams_data')
    ongoing_exams_data = request_data.get('ongoing_exams_data')
    query = { 'user_id': user_id, 'saved_data': saved_data, 'bought_exams': bought_exams, 
             'finished_exams_data': finished_exams_data, 'ongoing_exams_data': ongoing_exams_data }
    return query

def _update_user_data(query):
    return update_item_wrapper(dynamodb.Table(users), 
                               key={'user_id': query['user_id']},
                               upExp="set #did=:d, #fn=:f, #ln=:l, #em=:e",
                               expAttr={
                                   ':d' :  query['saved_data'],
                                   ':f' :  query['bought_exams'],
                                   ':l' :  query['finished_exams_data'],
                                   ':e' :  query['ongoing_exams_data'],
                               },
                               expAttrName={
                                   '#did': 'saved_data', '#fn': 'bought_exams', '#ln': 'finished_exams_data', '#em': 'ongoing_exams_data', 
                               }, identifier=identifier)

def update_user_data():
    return rule_wrapper(_update_user_data, query_builder, identifier, requ_session=True, requ_admin=False)