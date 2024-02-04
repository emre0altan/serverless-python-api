from .calls import _get_courses, _put_course, _update_course, _delete_course
from .calls import _responsemetadata_check, _get_dict_from_list

def test_courses(client, user1_with_session, admin_session):
    response = _put_course(client, admin_session[0], admin_session[1],
                           id=99998, 
                           code="test101", 
                           name="Test Course 1")
    assert _responsemetadata_check(response)

    response = _get_courses(client, user1_with_session[0], user1_with_session[1])
    item = _get_dict_from_list(response, 'id', 99998)
    assert item is not None
    assert item['id'] == 99998
    assert item['code'] == 'test101'
    assert item['name'] == 'Test Course 1'

    response = _update_course(client, admin_session[0], admin_session[1],
                           id=99998, 
                           code="test102", 
                           name="Test Course 2")
    assert _responsemetadata_check(response)

    response = _get_courses(client, user1_with_session[0], user1_with_session[1])
    item = _get_dict_from_list(response, 'id', 99998)
    assert item is not None
    assert item['id'] == 99998
    assert item['code'] == 'test102'
    assert item['name'] == 'Test Course 2'

    response = _delete_course(client, admin_session[0], admin_session[1], 
                              id=99998)
    assert _responsemetadata_check(response)
