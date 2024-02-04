from ..handler_db import dynamodb, get_questions_db
from ..handler_checkpoint_control import checkpoint_control
from ..handler_bucket import delete_question_images
from ..handler_request_wrapper import get_item_wrapper, delete_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

questions = get_questions_db()
identifier = "Delete Question"

def query_builder(request_data):
    exam_info_id = request_data.get('exam_info_id')
    question_index = request_data.get('question_index')
    query = { 'exam_info_id': exam_info_id, 'question_index': question_index }
    return query

def _delete_question(query):
    (success, response) = delete_item_wrapper(dynamodb.Table(questions), query, identifier)
    if success:
        (suc, res) = delete_question_images(query['exam_info_id'], query['question_index'])
    return (success, response)

def delete_question():
    return rule_wrapper(_delete_question, query_builder, identifier, requ_session=True, requ_admin=True)