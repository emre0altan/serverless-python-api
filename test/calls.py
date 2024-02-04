import requests
from .data import cloud_address

def _call_wrapper(client, json, target, print_it=True):
    if print_it:
        print('\n\n' + str(client) + '\n' + str(json) + '\n' + str(target))
    if client.is_cloud_server:
        response = requests.post(cloud_address + target, json=json).json()
    else:
        response = client.post(target, json=json).json
    if print_it:
        print(f"\n\n{target}  is_cloud_server:  {client.is_cloud_server}:\n\n" + str(response))
    return response

def _responsemetadata_check(response):
    return ('ResponseMetadata' in response) \
        and ('HTTPStatusCode' in response['ResponseMetadata']) \
        and (200 == response['ResponseMetadata']['HTTPStatusCode'] or 204 == response['ResponseMetadata']['HTTPStatusCode'])

def _get_dict_from_list(list, match_key1, value):
    return next((item for item in list if item[match_key1] == value), None)

def _get_dict_from_list_2(list, match_key1, match_key2, value, value2):
    return next((item for item in list if item[match_key1] == value and item[match_key2] == value2), None)

def _put_user(client, TestClient):
    json = {
        "user_id": TestClient.user_id,
        "device_id": TestClient.device_id,
        "first_name": TestClient.first_name,
        "last_name": TestClient.last_name,
        "email": TestClient.email
    }
    return _call_wrapper(client, json, "/put_user")

def _update_user(client, TestClient, admin_user_id, admin_session_key):
    json = {
        "user_id": admin_user_id,
        "session_key": admin_session_key,
        "client_user_id": TestClient.user_id,
        "device_id": TestClient.device_id,
        "first_name": TestClient.first_name,
        "last_name": TestClient.last_name,
        "email": TestClient.email
    }
    return _call_wrapper(client, json, "/update_user")

def _delete_user(client, user_id, admin_user_id, admin_session_key):
    json = {
        "user_id": admin_user_id,
        "session_key": admin_session_key,
        "client_user_id": user_id
    }
    return _call_wrapper(client, json, "/delete_user")

def _get_user(client, user_id, admin_user_id, admin_session_key):
    json = {
        "user_id": admin_user_id,
        "session_key": admin_session_key,
        "client_user_id": user_id
    }
    return _call_wrapper(client, json, "/get_user")

def _get_session(client, user_id):
    json = {
        "user_id": user_id
    }
    return _call_wrapper(client, json, "/get_session")

def _get_programmes(client, user_id, session_key):
    json={
        "user_id": user_id,
        "session_key": session_key,
    }
    return _call_wrapper(client, json, "/get_programmes")

def _put_programme(client, user_id, session_key, id, name):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
        'name': name,
    }
    return _call_wrapper(client, json, "/put_programme")

def _update_programme(client, user_id, session_key, id, name):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
        'name': name,
    }
    return _call_wrapper(client, json, "/update_programme")

def _delete_programme(client, user_id, session_key, id):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
    }
    return _call_wrapper(client, json, "/delete_programme")

def _get_departments(client, user_id, session_key):
    json={
        "user_id": user_id,
        "session_key": session_key,
    }
    return _call_wrapper(client, json, "/get_departments")

def _put_department(client, user_id, session_key, id, programme_id, name, courses):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
        'programme_id': programme_id,
        'name': name,
        'courses': courses,
    }
    return _call_wrapper(client, json, "/put_department")

def _update_department(client, user_id, session_key, id, programme_id, name, courses):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
        'programme_id': programme_id,
        'name': name,
        'courses': courses,
    }
    return _call_wrapper(client, json, "/update_department")

def _delete_department(client, user_id, session_key, id, programme_id):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
        'programme_id': programme_id
    }
    return _call_wrapper(client, json, "/delete_department")

def _get_courses(client, user_id, session_key):
    json={
        "user_id": user_id,
        "session_key": session_key,
    }
    return _call_wrapper(client, json, "/get_courses")

def _put_course(client, user_id, session_key, id, code, name):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
        'code': code,
        'name': name,
    }
    return _call_wrapper(client, json, "/put_course")

def _update_course(client, user_id, session_key, id, code, name):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
        'code': code,
        'name': name,
    }
    return _call_wrapper(client, json, "/update_course")

def _delete_course(client, user_id, session_key, id):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'id': id,
    }
    return _call_wrapper(client, json, "/delete_course")

def _get_exam_infos(client, user_id, session_key):
    json={
        "user_id": user_id,
        "session_key": session_key,
    }
    return _call_wrapper(client, json, "/get_exam_infos")

def _put_exam_info(client, user_id, session_key, course_id, exam_type, exam_year, exam_term, exam_duration):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'course_id': course_id,
        'exam_type': exam_type,
        'exam_year': exam_year,
        'exam_term': exam_term,
        'exam_duration': exam_duration,
    }
    return _call_wrapper(client, json, "/put_exam_info")

def _update_exam_info(client, user_id, session_key, course_id, exam_type, exam_year, exam_term, exam_duration):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'course_id': course_id,
        'exam_type': exam_type,
        'exam_year': exam_year,
        'exam_term': exam_term,
        'exam_duration': exam_duration,
    }
    return _call_wrapper(client, json, "/update_exam_info")

def _delete_exam_info(client, user_id, session_key, course_id, exam_type, exam_year, exam_term):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'course_id': course_id,
        'exam_type': exam_type,
        'exam_year': exam_year,
        'exam_term': exam_term,
    }
    return _call_wrapper(client, json, "/delete_exam_info")

def _get_questions(client, user_id, session_key, exam_info_id, question_index):
    json={
        "user_id": user_id,
        "session_key": session_key,
        "exam_info_id": exam_info_id,
        "question_index": question_index,
    }
    return _call_wrapper(client, json, "/get_questions")

def _put_question(client, user_id, session_key, exam_info_id, question_index, question, question_type, answers, correct_answer, image_data):
    json={
        "user_id": user_id,
        "session_key": session_key,
        'exam_info_id': exam_info_id,
        'question_index': question_index,
        'question': question,
        'question_type': question_type,
        'answers': answers,
        'correct_answer': correct_answer,
        'image_data': image_data,
    }
    return _call_wrapper(client, json, "/put_question", print_it=False)

def _update_question(client, user_id, session_key, exam_info_id, question_index, question, question_type, answers, correct_answer, image_data):
    print("UPDATE QUESTION")
    json={
        "user_id": user_id,
        "session_key": session_key,
        'exam_info_id': exam_info_id,
        'question_index': question_index,
        'question': question,
        'question_type': question_type,
        'answers': answers,
        'correct_answer': correct_answer,
        'image_data': image_data,
    }
    return _call_wrapper(client, json, "/update_question", print_it=False)

def _delete_question(client, user_id, session_key, exam_info_id, question_index):
    json={
        "user_id": user_id,
        "session_key": session_key,
        "exam_info_id": exam_info_id,
        "question_index": question_index,
    }
    return _call_wrapper(client, json, "/delete_question")