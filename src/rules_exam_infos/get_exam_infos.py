from ..handler_db import dynamodb, get_exam_infos_db
from ..handler_request_wrapper import scan_table_wrapper
from ..handler_rule_wrapper import rule_wrapper

exam_infos = get_exam_infos_db()
identifier = "Get Exam Infos"

def query_builder(request_data):
    return {'placeholder_key' : 'placeholder_value'}

def _get_exam_infos(query):
    return scan_table_wrapper(dynamodb.Table(exam_infos), "id", identifier)

def get_exam_infos():
    return rule_wrapper(_get_exam_infos, query_builder, identifier, requ_session=True, requ_admin=False)