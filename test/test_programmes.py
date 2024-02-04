from .calls import _get_programmes, _put_programme, _update_programme, _delete_programme
from .calls import _responsemetadata_check, _get_dict_from_list

def test_programmes(client, admin_session, user1_with_session):
    response = _put_programme(client, 
                              admin_session[0], 
                              admin_session[1],
                              99998,
                              'Test Programme 1')
    assert _responsemetadata_check(response)

    response = _get_programmes(client, user1_with_session[0], user1_with_session[1])
    item = _get_dict_from_list(response, 'id', 99998)
    assert item is not None
    assert item['id'] == 99998
    assert item['name'] == 'Test Programme 1'

    response = _update_programme(client, 
                              admin_session[0], 
                              admin_session[1],
                              99998,
                              'Test Programme 2')
    assert _responsemetadata_check(response)

    response = _get_programmes(client, user1_with_session[0], user1_with_session[1])
    item = _get_dict_from_list(response, 'id', 99998)
    assert item is not None
    assert item['id'] == 99998
    assert item['name'] == 'Test Programme 2'

    response = _delete_programme(client, 
                              admin_session[0], 
                              admin_session[1],
                              99998)
    assert _responsemetadata_check(response)
