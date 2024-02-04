from flask import request
from .handler_session_manager import SessionManager
from .handler_db import dynamodb, get_admin_users_db
from .handler_request_wrapper import get_item_wrapper

admin_users = get_admin_users_db()
identifier = "Checkpoint Get Admin User"

def is_admin_user(user_id):
    (success, result) = get_item_wrapper(dynamodb.Table(admin_users), 
                                           { 'user_id': user_id }, identifier)
    return success

def checkpoint_control(require_session_key=True, require_admin_user=True): 
    request_data = request.get_json()
    if require_admin_user and not is_admin_user(request_data['user_id']):
        return (False, {'authentication-error': 'Access denied!'})
    elif require_session_key:
        if "session_key" not in request_data:
            return (False, {'session-error': 'Access denied! Session key is not valid!'})
        if "user_id" not in request_data:
            print("#################-NO ACCESS-##################")
            return (False, {'session-error': 'Access denied! Google id is not exist!'})
        if not SessionManager.check_session_valid(request_data['user_id'], request_data['session_key']):
            return (False, {'session-error': 'Access denied! Session key is not valid!'})
    return (True, {})