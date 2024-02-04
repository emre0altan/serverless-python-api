import pytest
import os

from app import app

from test.calls import _put_user, _delete_user, _get_session
from test.data import TestClient1, TestClient2, TestAdmin

@pytest.fixture()
def pathTestDirectory(request):
    test_dir = os.path.dirname(request.module.__file__)
    return test_dir

@pytest.fixture()
def myapp():
    app.is_cloud_server = 'cloud_server' in os.environ and os.environ['cloud_server'] == '1'
    
    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(myapp):
    client = myapp.test_client()
    client.is_cloud_server = myapp.is_cloud_server
    return client

@pytest.fixture()
def admin_session(client):
    print("Admin Session")
    session_key = _get_session(client, TestAdmin.user_id)['session_key']
    return [TestAdmin.user_id, session_key]

@pytest.fixture()
def user1_no_session(client, admin_session):
    _put_user(client, TestClient1)
    yield [TestClient1.user_id]
    _delete_user(client, TestClient1.user_id, admin_session[0], admin_session[1])

@pytest.fixture()
def user2_no_session(client, admin_session):
    _put_user(client, TestClient2)
    yield [TestClient2.user_id]
    _delete_user(client, TestClient2.user_id, admin_session[0], admin_session[1])

@pytest.fixture()
def user1_with_session(client, admin_session):
    _put_user(client, TestClient1)
    session_key = _get_session(client, TestClient1.user_id)['session_key']
    yield [TestClient1.user_id, session_key]
    _delete_user(client, TestClient1.user_id, admin_session[0], admin_session[1])

@pytest.fixture()
def user2_with_session(client, admin_session):
    _put_user(client, TestClient2)
    session_key = _get_session(client, TestClient2.user_id)['session_key']
    yield [TestClient2.user_id, session_key]
    _delete_user(client, TestClient2.user_id, admin_session[0], admin_session[1])