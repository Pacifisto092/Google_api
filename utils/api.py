from utils.http_metod import HttpMethods
from utils.json import *

"""Методы для тестирования Google_maps_api"""

BASE_URL = "https://rahulshettyacademy.com"              # Базовая URL
KEY = "?key=qaclick123"                                  # Параметр для всех запросов
POST_RESOURSE = "/maps/api/place/add/json"               # Ресурс метода POST
GET_RESOURSE = "/maps/api/place/get/json"                # Ресурс метода GET
PUT_RESOURSE = "/maps/api/place/update/json"             # Ресурс метода PUT
DELETE_RESOURSE = "/maps/api/place/delete/json"       # Ресурс метода DELETE

class GoogleMapsApi:


    @staticmethod
    def create_new_place():
        """Метод для созданияя новой локации"""

        post_url = BASE_URL + POST_RESOURSE + KEY
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post


    @staticmethod
    def get_new_place(place_id):
        """Метод для проверки новой локации"""

        get_url = BASE_URL + GET_RESOURSE + KEY + "&place_id={}".format(place_id)
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get


    @staticmethod
    def put_new_place(place_id):
        """Метод для изменения локации"""

        put_url = BASE_URL + PUT_RESOURSE + KEY
        print(put_url)
        json_for_update_place["place_id"] = place_id
        result_put = HttpMethods.put(put_url, json_for_update_place)
        print(result_put.text)
        return result_put


    @staticmethod
    def delete_new_place(place_id):
        """Метод удаления локации"""

        delete_url = BASE_URL + DELETE_RESOURSE + KEY
        print(delete_url)
        json_for_delete_place["place_id"] = place_id
        result_delete = HttpMethods.delete(delete_url, json_for_delete_place)
        print(result_delete.text)
        return result_delete
