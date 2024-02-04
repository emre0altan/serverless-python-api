from flask import request, jsonify

from ..handler_session_manager import SessionManager
from ..handler_checkpoint_control import checkpoint_control
from ..handler_db import dynamodb, get_users_db
from ..handler_request_wrapper import get_item_wrapper

users = get_users_db()
identifier = "Get User"

def _get_user(user_id):
    if user_id:
        try:
            query = { 'user_id': user_id }
            print(query)
            (success, result) = get_item_wrapper(dynamodb.Table(users), query, identifier)
            print(result)
            if success:
                return jsonify(result)
            else:
                return jsonify({'error': 'User not found'})
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'})
    else:
        return jsonify({'error': 'User google id not provided'})

def get_session():
    (val, message) = checkpoint_control(require_session_key=False, require_admin_user=False)
    if(val):
        request_data = request.get_json()
        user_id = request_data.get('user_id')
        print(user_id)
        result = _get_user(user_id).json
        if 'error' in result:
            return result
        else:
            return jsonify(SessionManager.get_session(user_id))
    else:
        return message