from ..handler_db import dynamodb, get_announcements_db
from ..handler_request_wrapper import scan_table_wrapper
from ..handler_rule_wrapper import rule_wrapper

announcements = get_announcements_db()
identifier = "Get Announcements"

def query_builder(request_data):
    return {'placeholder_key' : 'placeholder_value'}

def _get_announcements(query):
    return scan_table_wrapper(dynamodb.Table(announcements), "id", identifier)

def get_announcements():
    return rule_wrapper(_get_announcements, query_builder, identifier, requ_session=True, requ_admin=False)