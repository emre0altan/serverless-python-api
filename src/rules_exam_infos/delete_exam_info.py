from ..handler_db import dynamodb, get_exam_infos_db
from ..handler_request_wrapper import delete_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

exam_infos = get_exam_infos_db()
identifier = "Delete Exam Info"

def query_builder(request_data):
    course_id = request_data.get('course_id')
    exam_type = request_data.get('exam_type')
    exam_year = request_data.get('exam_year')
    exam_term = request_data.get('exam_term')
    query = { 'course_id': course_id, 'exam_type': exam_type, 'exam_year': exam_year, 'exam_term': exam_term }
    return query

def _delete_exam_info(query):
    query['id'] = str(query['course_id']) + "-" + query['exam_type'] + "-" + query['exam_year'] + "-" + query['exam_term']
    updated_query = {'id':query['id']}
    return delete_item_wrapper(dynamodb.Table(exam_infos), updated_query, identifier)

def delete_exam_info():
    return rule_wrapper(_delete_exam_info, query_builder, identifier, requ_session=True, requ_admin=True)