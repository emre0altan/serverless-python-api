import os
import base64

from .calls import _get_questions, _put_question, _update_question, _delete_question
from .calls import _responsemetadata_check

def test_question(client, user1_with_session, pathTestDirectory, admin_session):
    e_i_id = '1-Vize-2077-1'
    question = "@@1@@aaa@@2@@aaaaaa@@3@@aaaaaa@@4@@aaaa@@2@@aaaaaaaaaaaaaaaaaaaaaaaaaadwdawdwadaaaaaaaa"
    answers = [
            {
                "answer" : "answerA_answerA_answer_answer",
                "answer_index" : 1
            },
            {
                "answer" : "answerB_answerB_answer_answer",
                "answer_index" : 2
            },
            {
                "answer" : "answerC_answerC_answer_answer",
                "answer_index" : 3
            },
            {
                "answer" : "answerD_answerD_answer_answer",
                "answer_index" : 4
            },
            {
                "answer" : "answerE_answerE_answer_answer",
                "answer_index" : 5
            },
        ]
    correct_answer = 'A'

    test = load_encoded(os.path.join(pathTestDirectory, 'test.png'))
    gift = load_encoded(os.path.join(pathTestDirectory, 'gift.png'))
    image_data = [test, gift]

    response = _put_question(client, admin_session[0], admin_session[1],
                             exam_info_id=e_i_id, question_index=1, question=question, 
                             question_type=1, answers=answers, correct_answer=correct_answer, image_data=image_data)
    assert _responsemetadata_check(response)

    response = _get_questions(client, user1_with_session[0], user1_with_session[1],
                              exam_info_id=e_i_id, question_index=1)
    assert not 'error' in response
    
    response = _update_question(client, admin_session[0], admin_session[1],
                             exam_info_id=e_i_id, question_index=3, question=question, 
                             question_type=2, answers=answers, correct_answer=correct_answer, image_data=image_data)
    assert _responsemetadata_check(response)

    response = _get_questions(client, user1_with_session[0], user1_with_session[1],
                              exam_info_id=e_i_id, question_index=1)
    assert not 'error' in response

    response = _delete_question(client, admin_session[0], admin_session[1],
                             exam_info_id=e_i_id, question_index=1)
    assert _responsemetadata_check(response)

    response = _delete_question(client, admin_session[0], admin_session[1],
                             exam_info_id=e_i_id, question_index=3)
    assert _responsemetadata_check(response)

def load_encoded(path):
    image_file = open(path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')