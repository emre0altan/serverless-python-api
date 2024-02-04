import boto3
import os
import glob

is_cloud_db = 'cloud_db' in os.environ and os.environ['cloud_db'] == '1'
is_cloud_server = 'cloud_server' in os.environ and os.environ['cloud_server'] == '1'

if is_cloud_server:
    temp_folder = '/tmp'
else:
    temp_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp')

if is_cloud_db:
    s3_client = boto3.client('s3', region_name='us-east-1')
    bucket = 'aofsoru-images'
else:
    s3_client = boto3.client('s3', region_name='us-east-1', endpoint_url='http://127.0.0.1:4566')
    bucket = 'test-images'

from zipfile import ZipFile
import shutil

exam_prefix = 'exam_'
question_prefix = 'question'
file_postfix = ".zip"

def get_downloaded_image_data(exam_info_id):
    exam_key = exam_prefix + exam_info_id
    saved_path = os.path.join(temp_folder, exam_key).replace("\\","/")
    questionFolders = glob.glob(saved_path + '/*')
    examImageData = []
    for qFolder in sorted(questionFolders): 
        print(str(qFolder))
        questionFiles = glob.glob(os.path.join(saved_path, qFolder) + '/*')
        questionImageData = []
        for file in questionFiles:
            print('\t' + str(file))
            f = open(str(file), "r")
            questionImageData.append(f.read())
        examImageData.append(questionImageData)
    return examImageData

def download_image_archive(exam_info_id):
    try:
        exam_key = exam_prefix + exam_info_id
        zip_path = os.path.join(temp_folder, exam_key + file_postfix).replace("\\","/")
        save_path = os.path.join(temp_folder, exam_key).replace("\\","/")

        (success, response) = download_file(exam_key + '.zip', zip_path)
        if success:
            with ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_folder)
            
        return (success, response)
    except Exception as e:
        return (False, {'error': e})

def delete_image_archive(exam_info_id):
    exam_key = exam_prefix + exam_info_id
    return delete_file(exam_key + '.zip')

def delete_question_images(exam_info_id, question_index):
    try:
        res = download_image_archive(exam_info_id)
        if res[0]:
            res = update_question_images(exam_info_id, question_index, [])
            if res[0]:
                res = upload_image_archive(exam_info_id)
        return res
    except Exception as e:
        return (False, {'error': e})

def upload_image_archive(exam_info_id):
    print("UPLOAD IMAGE ARCHIVE")
    try:
        exam_key = exam_prefix + exam_info_id
        saved_path = os.path.join(temp_folder, exam_key).replace("\\","/")

        print("Image saved path:\n " + saved_path)
        if os.path.exists(saved_path):
            print("Saved path exists.")
            shutil.make_archive(saved_path, 'zip', temp_folder, exam_key)
            (success, response) = upload_file(saved_path + '.zip')
            return (success, response)
        else:
            print("Saved path doesn't exists.")
            return (False, {'error': 'Error, image save path is not exist!'})
    except Exception as e:
        return (False, {'error': e})

def update_question_images(exam_info_id, question_index, encoded_images):
    print("UPDATE QUESTION IMAGES")
    try:
        exam_key = exam_prefix + exam_info_id
        saved_path = os.path.join(temp_folder, exam_key).replace("\\","/")
        (success, response) = download_image_archive(exam_info_id)
        if not os.path.exists(saved_path):
            print("NOT EXIST IN S3, CREATING FOLDER")
            print(saved_path)
            os.mkdir(saved_path)
        question_dir = os.path.join(saved_path, question_prefix + str(question_index)).replace("\\","/")
        
        if os.path.exists(question_dir):
            print("Question directory exists.")
            delete_folder_contents(question_dir)
        else:
            print("Question directory doesn't exist.")
            os.mkdir(question_dir)
        i = 1
        for encoded_image in encoded_images:
            with open(os.path.join(question_dir, str(i)),
                        'w+') as output_file:
                output_file.write(encoded_image)
                print("Writing image file to question dir: " + str(i))
            i = i + 1
        return (True, None)
    except Exception as e:
        return (False, {'error': e})


def download_file(key, save_path, identifier='download_file'):
    print("\nHost: " + str(s3_client.meta._endpoint_url))
    print("DOWNLOAD KEY: " + str(key))
    try:
        response = s3_client.download_file(bucket, key, save_path)
        print(identifier + ":\n\t" )
        return (True, response)
    except Exception as e:
        print(e)
        return (False, {'error': e})

def upload_file(file_name, object_name=None, identifier='upload_file'):
    print("\nHost: " + str(s3_client.meta._endpoint_url))
    if object_name is None:
        object_name = os.path.basename(file_name)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(identifier + ":\n\t" + str(response))
        return (True, response)
    except Exception as e:
        print(e)
        return (False, {'error': e})

def delete_file(key, identifier='delete_file'):
    print("\nHost: " + str(s3_client.meta._endpoint_url))
    try:
        response = s3_client.delete_object(Bucket=bucket, Key=key)
        print(identifier + ":\n\t" + str(response))
        return (True, response)
    except Exception as e:
        print(e)
        return (False, {'error': e})
    
def delete_folder_contents(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))