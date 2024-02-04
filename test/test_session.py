import time
from .calls import _get_session

def test_session(client, user1_no_session, user2_no_session):
    response = _get_session(client, user1_no_session[0])
    assert 'session_key' in response
    assert 'start_time' in response
    session_key = response['session_key']
    time.sleep(2)

    response = _get_session(client, user1_no_session[0])
    assert 'session_key' in response
    assert 'start_time' in response
    assert session_key == response['session_key']

    response = _get_session(client, user1_no_session[0])
    assert 'session_key' in response
    assert 'start_time' in response
    assert session_key == response['session_key']

    response = _get_session(client, user2_no_session[0])
    assert 'session_key' in response
    assert 'start_time' in response
