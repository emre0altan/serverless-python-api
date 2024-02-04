from ..handler_db import dynamodb, get_questions_db
from ..handler_checkpoint_control import checkpoint_control
from ..handler_bucket import update_question_images, upload_image_archive
from ..handler_request_wrapper import update_item_wrapper
from ..handler_rule_wrapper import rule_wrapper

questions = get_questions_db()
identifier = "Update Question"

def query_builder(request_data):
    question = request_data.get('question')
    question_type = request_data.get('question_type')
    exam_info_id = request_data.get('exam_info_id')
    question_index = request_data.get('question_index')
    image_data = request_data.get('image_data')
    answers = request_data.get('answers')
    correct_answer = request_data.get('correct_answer')
    query = { 'exam_info_id': exam_info_id, 'question_index': question_index, 
               'question': question, 'question_type': question_type, 'answers': answers, 'correct_answer': correct_answer, 'image_data': image_data }
    return query

def _update_question(query):
    image_data = query.pop('image_data')
    (success, response) = update_item_wrapper(dynamodb.Table(questions), 
                                              key={'exam_info_id': query['exam_info_id'], 'question_index': query['question_index']},
                                              upExp="set #a=:q, #s=:w, #f=:r, #t=:y",
                                              expAttr={
                                                  ':q' : query['question'],
                                                  ':w' : query['question_type'],
                                                  ':r' : query['answers'],
                                                  ':y' : query['correct_answer']
                                              },
                                              expAttrName={
                                                  '#a': 'question', '#s': 'question_type',
                                                  '#f': 'answers', '#t': 'correct_answer'
                                              }, identifier=identifier)
    if success:
        (suc, res) = update_question_images(query['exam_info_id'], query['question_index'], image_data)
        print("UPDATE QUESTION IMAGES RETURN: " + str(suc))
        print(res)
        if suc:
            (succ, resp) = upload_image_archive(query['exam_info_id'])
    return (success, response)


def update_question():
    return rule_wrapper(_update_question, query_builder, identifier, requ_session=True, requ_admin=True)
