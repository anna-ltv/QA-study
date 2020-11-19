from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from collections import Counter

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield
    pytest.driver.quit()

def test_all_pets_in_list():

    pytest.driver.find_element_by_id('email').send_keys('test.qap@yandex.ru')
        # enter password
    pytest.driver.find_element_by_id('pass').send_keys('123cd-123')
        # press the button
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
        # переходим на страницу мои питомцы
    pytest.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[1]/a').click()

    pet_list = pytest.driver.find_elements_by_xpath('//tbody/tr')
    assert len(pet_list) > 0
    assert len(pet_list) == 2

def test_half_pets_with_photo():
    # тест на проверку наличия изображений как min у половины питомцев
    pytest.driver.find_element_by_id('email').send_keys('test.qap@yandex.ru')
    # enter password
    pytest.driver.find_element_by_id('pass').send_keys('123cd-123')
    # press the button
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # переходим на страницу мои питомцы
    pytest.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[1]/a').click()

    images_list = WebDriverWait(pytest.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,"//th/img")))

    for i in range(len(images_list)//2):
        assert images_list[i].get_attribute('src') != ''

def test_all_pets_with_full_data():
    # тест проверяет наличие имен у всех питомцев
    pytest.driver.find_element_by_id('email').send_keys('test.qap@yandex.ru')
    # enter password
    pytest.driver.find_element_by_id('pass').send_keys('123cd-123')
    # press the button
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # переходим на страницу мои питомцы
    pytest.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[1]/a').click()

    names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//tr/td[1]")))
    breeds = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//tr/td[2]")))
    ages = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//tr/td[3]")))

    # проверяем, что у всех питомцев указаны имена
    for i in range(len(names)):
        assert names[i] != ''
        assert len(names[i].text) > 0

    # проверяем, что у всех питомцев указана порода
    for i in range(len(breeds)):
        assert breeds[i] != ''
        assert len(breeds[i].text) > 0

    # проверяем, что у всех питомцев указан возраст
    for i in range(len(ages)):
        assert ages[i] != ''

def test_no_same_names():
    # тест проверяет, что у питомцев разные имена

    pytest.driver.find_element_by_id('email').send_keys('test.qap@yandex.ru')
    # enter password
    pytest.driver.find_element_by_id('pass').send_keys('123cd-123')
    # press the button
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # переходим на страницу мои питомцы
    pytest.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[1]/a').click()

    names = pytest.driver.find_elements_by_xpath("//tr/td[1]")
    # проверяем, что все имена уникальны и не повторяются

    names_list = []
    for name in names:
        name = name.text
        clear_name = ""
        for letter in name:
    # проверяем, что каждое имя состоит из букв алфавита и добавляем его в список, предварительно сделав все буквы одного регистра
            if letter.isalpha():
                clear_name += letter.lower()
            else:
                print("Имя содержит недопустимые знаки")
        names_list.append(clear_name)
    # через библиотеку Counter подсчитываем количество значений, если значение равно 1 - passed
    for k,v in Counter(names_list).items():
        assert v == 1
