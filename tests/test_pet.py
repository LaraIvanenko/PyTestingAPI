
from api import Pets


pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    token = pt.get_token()[0]
    assert token
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_create_pet():
    status = pt.create_pet()[1]
    pet_id = pt.create_pet()[0]
    assert status == 200
    assert pet_id


def test_upload_photo():
    status = pt.upload_pet_photo()[0]
    link = pt.upload_pet_photo()[1]
    assert status == 200
    assert link


def test_put_pet_like():
    status = pt.put_pet_like()
    assert status == 200


def test_update_pet():
    status = pt.update_pet()
    assert status == 200

def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200

def test_update_pet_neg():
    status = pt.update_pet_neg()
    assert status != 200

def test_put_pet_like_neg():
    status = pt.put_pet_like_neg()
    assert status != 200

def test_put_pet_like_not_auth():
    status = pt.put_pet_like_not_auth()
    assert status != 200


def test_create_pet_neg():
    status = pt.create_pet_neg()
    assert status != 200
