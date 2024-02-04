from .data import TestClient1, UpdatedTestClient1
from .data import TestClient2, UpdatedTestClient2
from .calls import _get_user, _put_user, _update_user, _delete_user
from .calls import _responsemetadata_check

def test_user1(client, admin_session):
    run_user(client, TestClient1, UpdatedTestClient1, admin_session)

def test_user2(client, admin_session):
    run_user(client, TestClient2, UpdatedTestClient2, admin_session)

def run_user(client, test_client, updated_test_client, admin_session):
    response = _get_user(client, test_client.user_id, admin_session[0], admin_session[1])
    assert response is not None
    assert 'error' in response

    response = _put_user(client, test_client)
    assert _responsemetadata_check(response)

    response = _get_user(client, test_client.user_id, admin_session[0], admin_session[1])
    assert response['user_id'] == test_client.user_id
    assert response['device_id'] == test_client.device_id
    assert response['first_name'] == test_client.first_name
    assert response['last_name'] == test_client.last_name
    assert response['email'] == test_client.email

    response = _update_user(client, updated_test_client, admin_session[0], admin_session[1])
    assert _responsemetadata_check(response)

    response = _get_user(client, test_client.user_id, admin_session[0], admin_session[1])
    assert response['user_id'] == test_client.user_id
    assert response['device_id'] == updated_test_client.device_id
    assert response['first_name'] == updated_test_client.first_name
    assert response['last_name'] == updated_test_client.last_name
    assert response['email'] == updated_test_client.email

    response = _delete_user(client, test_client.user_id, admin_session[0], admin_session[1])
    assert _responsemetadata_check(response)

    response = _get_user(client, test_client.user_id, admin_session[0], admin_session[1])
    assert response is not None
    assert 'error' in response

