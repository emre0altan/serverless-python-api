import boto3
import os

is_cloud_db = 'cloud_db' in os.environ and os.environ['cloud_db'] == '1'

if is_cloud_db:
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
else:
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url='http://127.0.0.1:4566')

programmes = "aofsoru_programmes"
departments = "aofsoru_departments"
courses = "aofsoru_courses"
admin_users = "aofsoru_admin_users"
users = "aofsoru_users"
exam_infos = "aofsoru_examinfos"
questions = "aofsoru_questions"
user_data = "aofsoru_user_data"
exam_dates = "aofsoru_exam_dates"
announcements = "aofsoru_announcements"

test_programmes = "test_programmes"
test_departments = "test_departments"
test_courses = "test_courses"
test_admin_users = "test_admin_users"
test_users = "test_users"
test_examinfos = "test_examinfos"
test_questions = "test_questions"

def get_users_db():
    if not is_cloud_db:
        return test_users
    return users

def get_admin_users_db():
    if not is_cloud_db:
        return test_admin_users
    return admin_users

def get_programmes_db():
    if not is_cloud_db:
        return test_programmes
    return programmes

def get_departments_db():
    if not is_cloud_db:
        return test_departments
    return departments

def get_courses_db():
    if not is_cloud_db:
        return test_courses
    return courses

def get_exam_infos_db():
    if not is_cloud_db:
        return test_examinfos
    return exam_infos

def get_questions_db():
    if not is_cloud_db:
        return test_questions
    return questions

def get_user_data_db():
    return user_data

def get_exam_dates_db():
    return exam_dates

def get_announcements_db():
    return announcements