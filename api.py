import json
import requests
import settings


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):

        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {"email": settings.VALID_EMAIL,
                "password": settings.VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        #print(my_token)
        #print(res.json())
        return my_token, status, my_id


    def get_list_users(self):
        """Запрос к Swagger сайта для получения id пользователя по указанным email и password"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json
        return status, amount

    def create_pet(self) -> json:
        """Запрос к Swagger сайта для создания питомца зарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": 0,
                "name": 'Bela', "type": 'dog', "age": 2, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def upload_pet_photo(self):
        """Запрос к Swagger сайта для загрузки фотографии к карточке созданного питомца зарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('viz.jpg', open('tests\\Photo\\viz.jpg', 'rb'), 'image/jpg')}
        #pic = open('tests\\Photo\\viz.jpg', 'rb')
        #files = {pic: pic}

        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def post_pet(self) -> json:
        """Запрос к Swagger сайта для получения id своего питомца зарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {'skip': 0, "num": 1, "user_id": my_id}

        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        pet_id = res.json()['list'][0]['id']
        return status, pet_id

    def put_pet_like(self) -> json:
        """Запрос к Swagger сайта для проставления лайка своему питомцу зарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def delete_pet(self) -> json:
        """Запрос к Swagger сайта для удаления своего питомца зарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {'id': pet_id}

        res = requests.delete(self.base_url + f'pet/{pet_id}', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def update_pet(self) -> json:
        """Запрос к Swagger сайта для изменения имени в карточке своего питомца зарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        pet_id = Pets().post_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id, "type": "dog", "name": 'Alex', "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status


    def update_pet_neg(self) -> json:
        """Запрос к Swagger сайта для изменения имени в карточке питомца другого пользователя зарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        pet_id = 1547
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id, "type": "dog", "name": 'Alex2', "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def put_pet_like_neg(self) -> json:
        """Запрос к Swagger сайта для проставления лайка своему питомцу невалидным запросом PATCH зарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id}
        res = requests.patch(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def put_pet_like_not_auth(self) -> json:
        """Запрос к Swagger сайта для проставления лайка питомцу незарегистрированным пользователем"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[1]
        headers = {'Authorization': 'Bearer'}
        data = {"id": pet_id}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def create_pet_neg(self) -> json:
        """Запрос к Swagger сайта для создания питомца с некорректным токеном"""
        my_token = "Pets().get_token()[0]"
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": 0,
                "name": 'Bela', "type": 'dog', "age": 2, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status


Pets().get_token()
Pets().get_list_users()
Pets().create_pet()
Pets().upload_pet_photo()
Pets().post_pet()
Pets().put_pet_like()
Pets().update_pet()
Pets().delete_pet()
Pets().update_pet_neg()
Pets().put_pet_like_neg()
Pets().put_pet_like_not_auth()
Pets().create_pet_neg()
