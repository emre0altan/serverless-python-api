from ..handler_db import dynamodb, get_programmes_db
from ..handler_request_wrapper import scan_table_wrapper
from ..handler_rule_wrapper import rule_wrapper

programmes = get_programmes_db()
identifier = "Get Programmes"

def query_builder(request_data):
    return {'placeholder_key' : 'placeholder_value'}

def _get_programmes(query):
    return scan_table_wrapper(dynamodb.Table(programmes), "id", identifier)

def get_programmes():
    return rule_wrapper(_get_programmes, query_builder, identifier, requ_session=True, requ_admin=False)