from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()

def test_show_my_pets():
    # enter email
    pytest.driver.find_element_by_id('email').send_keys('test.mail')
    # enter password
    pytest.driver.find_element_by_id('pass').send_keys('123')
    # press the button
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

#тест по данным карточек всех питомцев
def test_check_info_all():
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    description = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        # проверяем, что у всех карточек есть картинки
        assert images[i].get_attribute('src') != ''
        # проверяем, что все питомцы с именем
        assert names[i] != ''
        # проверяем, что у всех есть описание (порода и возвраст)
        assert description[i] !=''
        # проверяем, что данные породы и возраста разделены запятой
        assert ', ' in description[i]
        # проверяем каждую часть описания - порода и возвраст не пустые
        parts = description[i].text.split(', ')
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

# тест из модуля, почему-то все переменные изображения, имени и описания с одним css селектором
# def test_check_info_all_pets():
#     images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
#     names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
#     descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
#
#     for i in range(len(names)):
#         assert images[i].get_attribute('src') != ''
#         assert names[i].text != ''
#         assert descriptions[i].text != ''
#         assert ', ' in descriptions[i]
#         parts = descriptions[i].text.split(", ")
#         assert len(parts[0]) > 0
#         assert len(parts[1]) > 0