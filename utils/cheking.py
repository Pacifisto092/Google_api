"""Методы для проверки ответов наших запросов"""
import json


class Cheking:

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response, status_code):
        if response.status_code == status_code:
            print("Успешно! Статус код ={}".format(response.status_code))
        else:
            print("Провал! Статус код ={}".format(response.status_code))
        assert response.status_code == status_code



    """Метод для проверки обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")


    """Метод для проверки значения полей в ответе запроса"""
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("{} - верно!!!".format(field_name))


    """Метод для проверки значения полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово {} присутствует".format(search_word))
        else:
            print("Слово {} отсутствует".format(search_word))
        assert search_word in check_info

