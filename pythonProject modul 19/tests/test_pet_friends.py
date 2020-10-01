from api import PetFriends
from settings import valid_email, valid_password, unvalid_password, unvalid_email
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_unvalid_user(email=unvalid_email, password=unvalid_password):
    # Проверяем вход при невалидных данных email и пароль, статус запроса не должен быть 200
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' not in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_without_photo(name='pet_1', animal_type='type_1', age='age_1', pet_photo = ''):
    #Проверяем возможность добавления питомца без фото

    #Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_information_about_new_pet_without_photo(auth_key, name, animal_type, age, pet_photo)

    #проверяем статус запроса 200, соответствие имени питомца, вида, возраста и отсутвие фото
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert 'jpg' or 'jpeg' not in result['pet_photo']

def test_add_only_pet_photo(name='', animal_type = '', age = '',pet_photo='images\pet_1_photo.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # проверяем возможность создания питомца только с фото
    # Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet_only_with_photo(auth_key, name, animal_type, age, pet_photo)

    # проверяем статус запроса 200, наличие фото
    assert status == 200
    assert 'jpg' or 'jpeg' in result['pet_photo']
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age

def test_add_new_pet_with_valid_data(name='Stich', animal_type = 'alien', age = '3', pet_photo='images\pet_photo.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    #проверяем добавление питомца с фото и корректными данными
    #Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # проверяем статус запроса 200, соответствие имени питомца, вида и возраста, наличие фото
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert 'jpg' or 'jpeg' in result['pet_photo']

def test_add_new_pet_with_unvalid_data(name='%%%$$', animal_type = '???', age = '<>>'):
    #проверяем добавление питомца с некорректными данными
    #Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_information_about_new_pet_without_photo(auth_key, name, animal_type, age)

    # проверяем статус запроса 200, соответствие имени питомца, вида и возраста, наличие фото
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_photo_of_pet(pet_photo='images\pet_1_photo.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # проверяем возможность добавления фото к питомцу
    # Получаем ключ auth_key и список моих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    # проверяем статус запроса 200, наличие фото
    assert status == 200
    assert 'jpg' or 'jpeg' in result['pet_photo']

def test_successful_delete_self_pet():
    #Проверяем возможность удаления питомца

    # Получаем ключ auth_key и запрашиваем список моих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Отправляем запрос на удаление первого питомца по id
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet_from_database(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Люцифер', animal_type='кот', age=5):
    #Проверяем возможность обновления информации о питомце

    # Получаем ключ auth_key и список моих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_information(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("No results found")





