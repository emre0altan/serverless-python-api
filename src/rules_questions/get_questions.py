from boto3.dynamodb.conditions import Key

from ..handler_db import dynamodb, get_questions_db
from ..handler_bucket import download_image_archive, get_downloaded_image_data
from ..handler_request_wrapper import query_table_wrapper
from ..handler_rule_wrapper import rule_wrapper

questions = get_questions_db()
identifier = "Get Question"

def query_builder(request_data):
    exam_info_id = request_data.get('exam_info_id')
    question_index = request_data.get('question_index')
    query = {'exam_info_id': exam_info_id, 'question_index': question_index}
    return query

def _get_question(query):
    exam_info_id = query['exam_info_id']
    (success, result) = query_table_wrapper(dynamodb.Table(questions), 
                                            Key('exam_info_id').eq(exam_info_id), "question_index", "Get Question")
    
    if success:
        (suc, res) = download_image_archive(exam_info_id)
        if suc:
            print("DOWNLOAD IMAGE ARCHIVE RESULTED SUCCESS")
            image_data = get_downloaded_image_data(exam_info_id)
            print("IMAGE DATA:")
            print(image_data)
            i = 0
            for question in result:
                question['image_data'] = image_data[i]
                i = i+1
        else:
            print("DOWNLOAD IMAGE ARCHIVE RESULTED FAILURE")
        print("@@")
        print("@@")
        print(result)
    return (success, result)

def get_questions():
    return rule_wrapper(_get_question, query_builder, identifier, requ_session=True, requ_admin=False)
    