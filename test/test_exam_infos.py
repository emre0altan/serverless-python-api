from .calls import _get_exam_infos, _put_exam_info, _update_exam_info, _delete_exam_info
from .calls import _responsemetadata_check, _get_dict_from_list

def test_exam_infos(client, user1_with_session, admin_session):
    response = _put_exam_info(client, admin_session[0], admin_session[1],
                              course_id=1, exam_type='Vize', exam_year='2013', exam_term='1', exam_duration='1800')
    assert _responsemetadata_check(response)
    
    response = _get_exam_infos(client, user1_with_session[0], user1_with_session[1])
    item = _get_dict_from_list(response, 'id', '1-Vize-2013-1')
    assert item is not None
    assert item['id'] == '1-Vize-2013-1'
    assert item['course_id'] == 1
    assert item['exam_duration'] == '1800'
    assert item['exam_term'] == '1'
    assert item['exam_type'] == 'Vize'
    assert item['exam_year'] == '2013'

    response = _update_exam_info(client, admin_session[0], admin_session[1],
                              course_id=1, exam_type='Vize', exam_year='2013', exam_term='1', exam_duration='2400')
    assert _responsemetadata_check(response)

    response = _get_exam_infos(client, user1_with_session[0], user1_with_session[1])
    item = _get_dict_from_list(response, 'id', '1-Vize-2013-1')
    assert item is not None
    assert item['id'] == '1-Vize-2013-1'
    assert item['course_id'] == 1
    assert item['exam_duration'] == '2400'
    assert item['exam_term'] == '1'
    assert item['exam_type'] == 'Vize'
    assert item['exam_year'] == '2013'

    response = _delete_exam_info(client, admin_session[0], admin_session[1],
                                 course_id=1, exam_type='Vize', exam_year='2013', exam_term='1')
    assert _responsemetadata_check(response)