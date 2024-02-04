from flask import jsonify, request

from .handler_checkpoint_control import checkpoint_control

def rule_wrapper(request_func, query_builder, identifier, requ_session=True, requ_admin=True):
    (val, message) = checkpoint_control(require_session_key=requ_session, require_admin_user=requ_admin)
    if(val):
        request_data = request.get_json()
        query = query_builder(request_data)
        if query:
            try:
                (success, result) = request_func(query)
                if success:
                    return jsonify(result)
                else:
                    return jsonify({'error': f'RuleWrapper:  Request returned false for {identifier}! : ' + str(result)})
            except Exception as e:
                return jsonify({'error': f'RuleWrapper:  Exception thrown for {identifier}:\n {str(e)}'})
        else:
            return jsonify({'error': f'RuleWrapper:  Could not build query for {identifier}!'})
    else:
        return message