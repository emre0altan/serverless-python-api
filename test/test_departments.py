from .calls import _get_departments, _put_department, _update_department, _delete_department
from .calls import _responsemetadata_check, _get_dict_from_list

def test_departments(client, user1_with_session, admin_session):
    response = _put_department(client,
                               admin_session[0],
                               admin_session[1],
                               id=99998,
                               programme_id=99998,
                               name="Test Department 1",
                               courses=[
                                   {'course_id':1, 'term_id':1},
                                   {'course_id':2, 'term_id':1},
                               ])
    assert _responsemetadata_check(response)

    response = _get_departments(client, user1_with_session[0], user1_with_session[1])
    item = _get_dict_from_list(response, 'id', 99998)
    assert item is not None
    assert item['id'] == 99998
    assert item['programme_id'] == 99998
    assert item['name'] == 'Test Department 1'
    assert len(item['courses']) == 2 
    assert item['courses'][0]['course_id'] == 1 
    assert item['courses'][0]['term_id'] == 1 
    assert item['courses'][1]['course_id'] == 2 
    assert item['courses'][1]['term_id'] == 1 

    response = _update_department(client,
                               admin_session[0],
                               admin_session[1],
                               id=99998,
                               programme_id=99998,
                               name="Updated Test Department 1",
                               courses=[
                                   {'course_id':5, 'term_id':1},
                                   {'course_id':6, 'term_id':1},
                               ])
    assert _responsemetadata_check(response)

    response = _get_departments(client, user1_with_session[0], user1_with_session[1])
    item = _get_dict_from_list(response, 'id', 99998)
    assert item is not None
    assert item['id'] == 99998
    assert item['programme_id'] == 99998
    assert item['name'] == 'Updated Test Department 1'
    assert len(item['courses']) == 2 
    assert item['courses'][0]['course_id'] == 5 
    assert item['courses'][0]['term_id'] == 1 
    assert item['courses'][1]['course_id'] == 6 
    assert item['courses'][1]['term_id'] == 1 

    response = _delete_department(client, admin_session[0], admin_session[1], id=1, programme_id=1)
    assert _responsemetadata_check(response)
