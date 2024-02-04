import pprint
from datetime import datetime
from random import randint

class SessionManager:
    session_timeout = 300
    sessions = {}

    def get_new_session_key():
        return randint(100000000, 999999999)

    def get_session(user_id):
        SessionManager.print_session_keys()
        #If there is already a session key then use it if it still applies
        if user_id in SessionManager.sessions:
            (key, start_time) = SessionManager.sessions[user_id]
            current_time = datetime.now()
            difference = (current_time - start_time).total_seconds()
            if difference < SessionManager.session_timeout:
                return {'session_key': SessionManager.sessions[user_id][0], 'start_time': SessionManager.sessions[user_id][1].isoformat()}

        #Create a session key and save it with start time
        session_key = SessionManager.get_new_session_key()
        SessionManager.sessions[user_id] = (session_key, datetime.now())
        return {'session_key': SessionManager.sessions[user_id][0], 'start_time': SessionManager.sessions[user_id][1].isoformat()}

    def check_session_valid(user_id, session_key):
        SessionManager.print_session_keys()
        if user_id in SessionManager.sessions:
            (key, start_time) = SessionManager.sessions[user_id]
            if key != session_key:
                return False
            else:
                current_time = datetime.now()
                difference = (current_time - start_time).total_seconds()
                if difference < SessionManager.session_timeout:
                    return True
                else:
                    del SessionManager.sessions[user_id]
                    return False
        else:
            return False
        
    def print_session_keys():
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(SessionManager.sessions)