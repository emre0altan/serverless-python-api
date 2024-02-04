from ..handler_db import dynamodb, get_exam_dates_db
from ..handler_request_wrapper import scan_table_wrapper
from ..handler_rule_wrapper import rule_wrapper

exam_dates = get_exam_dates_db()
identifier = "Get Exam Dates"

def query_builder(request_data):
    return {'placeholder_key' : 'placeholder_value'}

def _get_exam_dates(query):
    return scan_table_wrapper(dynamodb.Table(exam_dates), "id", identifier)

def get_exam_dates():
    return rule_wrapper(_get_exam_dates, query_builder, identifier, requ_session=True, requ_admin=False)