from ..handler_db import dynamodb, get_exam_infos_db
from ..handler_request_wrapper import update_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

exam_infos = get_exam_infos_db()
identifier = "Update Exam Info"

def query_builder(request_data):
    course_id = request_data.get('course_id')
    exam_type = request_data.get('exam_type')
    exam_year = request_data.get('exam_year')
    exam_term = request_data.get('exam_term')
    exam_duration = request_data.get('exam_duration')
    query = { 'course_id': course_id, 'exam_type': exam_type, 'exam_year': exam_year, 'exam_duration': exam_duration, 'exam_term': exam_term }
    return query

def _update_exam_info(query):
    query['id'] = str(query['course_id']) + "-" + query['exam_type'] + "-" + query['exam_year'] + "-" + query['exam_term']
    return update_item_wrapper(dynamodb.Table(exam_infos),
                               key={'id': query['id']},
                               upExp="set #cid=:c, #et=:d, #ey=:e, #ed=:f, #etr=:g",
                               expAttr={
                                   ':c' : query['course_id'],
                                   ':d' : query['exam_type'],
                                   ':e' : query['exam_year'],
                                   ':f' : query['exam_duration'],
                                   ':g' : query['exam_term'],
                               },
                               expAttrName={
                                   '#cid': 'course_id', '#et': 'exam_type', '#ey': 'exam_year', 
                                   '#ed': 'exam_duration', '#etr': 'exam_term' 
                               }, identifier=identifier)

def update_exam_info():
    return rule_wrapper(_update_exam_info, query_builder, identifier, requ_session=True, requ_admin=True)