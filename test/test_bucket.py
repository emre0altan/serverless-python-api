import os
import base64
from src.handler_bucket import download_image_archive, delete_image_archive, update_question_images, upload_image_archive
from src.handler_bucket import download_file, upload_file, delete_file
from .calls import _responsemetadata_check

def test_bucket(pathTestDirectory):
    if os.environ['cloud_server'] == "1":
        return
    test_image_key = "test.png"
    test_image_path = os.path.join(pathTestDirectory, "test.png")
    test_image_download_path = os.path.join(pathTestDirectory, "test_downloaded.png")

    print(pathTestDirectory)
    response = download_file(test_image_key, test_image_download_path)
    assert not response[0]
    assert 'error' in response[1]

    response = upload_file(test_image_path)
    assert response[0]

    response = download_file(test_image_key, test_image_download_path)
    assert response[0]

    response = delete_file(test_image_key)
    assert response[0]
    assert _responsemetadata_check(response[1])

    response = download_file(test_image_key, test_image_download_path)
    assert not response[0]
    assert 'error' in response[1]

def test_bucket_archive(pathTestDirectory):
    if os.environ['cloud_server'] == "1":
        return
    exam_info_id = "1-Vize-2015-1"
    
    response = download_image_archive(exam_info_id)
    assert not response[0]
    print('------------------------------------')
    world = load_encoded(os.path.join(pathTestDirectory, 'world.png'))
    encoded_images = [world]
    response = update_question_images(exam_info_id, 1, encoded_images)

    print('------------------------------------')
    test = load_encoded(os.path.join(pathTestDirectory, 'test.png'))
    gift = load_encoded(os.path.join(pathTestDirectory, 'gift.png'))
    encoded_images = [test, gift]
    response = update_question_images(exam_info_id, 2, encoded_images)
    print(response)
    print('------------------------------------')
    tshirt = load_encoded(os.path.join(pathTestDirectory, 'tshirt.png'))
    encoded_images = [tshirt]
    response = update_question_images(exam_info_id, 3, encoded_images)
    print(response)
    print('------------------------------------')
    response = upload_image_archive(exam_info_id)
    print(response)
    print('------------------------------------')
    response = download_image_archive(exam_info_id)
    print(response)
    assert response[0]
    print('------------------------------------')
    response = delete_image_archive(exam_info_id)
    print('------------------------------------')
    response = download_image_archive(exam_info_id)
    assert not response[0]

def load_encoded(path):
    image_file = open(path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')