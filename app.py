from flask import Flask, jsonify
from flask_cors import CORS
import os

os.environ['testing'] = "0"
os.environ['cloud_db'] = "1"
os.environ['cloud_server'] = "1"

debug = False
app = Flask(__name__)
CORS(app)

def add_rule(url, view_func, methods):
    app.add_url_rule(url, view_func=view_func, methods=methods)

def hello_from_root():
    return jsonify(message='Hello from root!')

def hello():
    return jsonify(message='Hello from path!')

add_rule('/', view_func=hello_from_root, methods=['GET'])
add_rule('/hello', view_func=hello, methods=['GET'])

from src.rules_users.delete_user import delete_user
from src.rules_users.get_user import get_user
from src.rules_users.put_user import put_user
from src.rules_users.update_user import update_user

add_rule('/delete_user', view_func=delete_user, methods=['POST']) #admin
add_rule('/get_user', view_func=get_user, methods=['POST']) #admin
add_rule('/put_user', view_func=put_user, methods=['POST']) #both
add_rule('/update_user', view_func=update_user, methods=['POST']) #admin

from src.rules_session.get_session import get_session

add_rule('/get_session', view_func=get_session, methods=['POST']) #both

from src.rules_programmes.delete_programme import delete_programme
from src.rules_programmes.get_programmes import get_programmes
from src.rules_programmes.put_programme import put_programme
from src.rules_programmes.update_programme import update_programme

add_rule('/delete_programme', view_func=delete_programme, methods=['POST']) #admin
add_rule('/get_programmes', view_func=get_programmes, methods=['POST']) #both
add_rule('/put_programme', view_func=put_programme, methods=['POST']) #admin
add_rule('/update_programme', view_func=update_programme, methods=['POST']) #admin

from src.rules_departments.delete_department import delete_department
from src.rules_departments.get_departments import get_departments
from src.rules_departments.put_department import put_department
from src.rules_departments.update_department import update_department

add_rule('/delete_department', view_func=delete_department, methods=['POST']) #admin
add_rule('/get_departments', view_func=get_departments, methods=['POST']) #both
add_rule('/put_department', view_func=put_department, methods=['POST']) #admin
add_rule('/update_department', view_func=update_department, methods=['POST']) #admin

from src.rules_courses.delete_course import delete_course
from src.rules_courses.get_courses import get_courses
from src.rules_courses.put_course import put_course
from src.rules_courses.update_course import update_course

add_rule('/delete_course', view_func=delete_course, methods=['POST']) #admin
add_rule('/get_courses', view_func=get_courses, methods=['POST']) #both
add_rule('/put_course', view_func=put_course, methods=['POST']) #admin
add_rule('/update_course', view_func=update_course, methods=['POST']) #admin

from src.rules_exam_infos.delete_exam_info import delete_exam_info
from src.rules_exam_infos.get_exam_infos import get_exam_infos
from src.rules_exam_infos.put_exam_info import put_exam_info
from src.rules_exam_infos.update_exam_info import update_exam_info

add_rule('/delete_exam_info', view_func=delete_exam_info, methods=['POST']) #admin
add_rule('/get_exam_infos', view_func=get_exam_infos, methods=['POST']) #both
add_rule('/put_exam_info', view_func=put_exam_info, methods=['POST']) #admin
add_rule('/update_exam_info', view_func=update_exam_info, methods=['POST']) #admin

from src.rules_questions.delete_question import delete_question
from src.rules_questions.get_questions import get_questions
from src.rules_questions.put_question import put_question
from src.rules_questions.update_question import update_question

add_rule('/delete_question', view_func=delete_question, methods=['POST']) #admin
add_rule('/get_questions', view_func=get_questions, methods=['POST']) #both
add_rule('/put_question', view_func=put_question, methods=['POST']) #admin
add_rule('/update_question', view_func=update_question, methods=['POST']) #admin


from src.rules.get_exam_dates import get_exam_dates

add_rule('/get_exam_dates', view_func=get_exam_dates, methods=['POST']) #both

from src.rules.get_announcements import get_announcements

add_rule('/get_announcements', view_func=get_announcements, methods=['POST']) #both

from src.rules.get_user_data import get_user_data
from src.rules.update_user_data import update_user_data

add_rule('/get_user_data', view_func=get_user_data, methods=['POST']) #both
add_rule('/update_user_data', view_func=update_user_data, methods=['POST']) #both