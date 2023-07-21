import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.color import Color

@pytest.fixture
def driver():
    # Инициализируем веб-драйвер для запуска браузера (например, Chrome)
    driver = webdriver.Chrome()
    yield driver
    # Закрываем браузер после выполнения теста
    driver.quit()


def test_background_color(driver):
    # Открываем веб-страницу
    driver.get("file:///D:/work/Python/pytest/test_web_page/index.html")

    # Находим элемент с приветствием и проверяем, что оно правильное
    page = driver.find_element(By.TAG_NAME, "body")
    page_bgcolor_hex = Color.from_string(page.value_of_css_property("background-color")).hex
    assert page_bgcolor_hex == "#8200ff"



def test_greeting_message(driver):
    # Открываем веб-страницу
    driver.get("file:///D:/work/Python/pytest/test_web_page/index.html")

    # Находим поле для ввода имени и вводим имя пользователя
    name_input = driver.find_element(By.ID, "name_input")
    name_input.send_keys("Alice")

    # Находим кнопку "Отправить" и кликаем на нее
    submit_button = driver.find_element(By.ID, "submit_button")
    submit_button.click()

    # Находим элемент с приветствием и проверяем, что оно правильное
    greeting_message = driver.find_element(By.ID, "greeting_message")
    assert greeting_message.text == "Привет, Alice!"


def test_greeting_message_border_size(driver):
    # Открываем веб-страницу
    driver.get("file:///D:/work/Python/pytest/test_web_page/index.html")

    # Находим поле для ввода имени и вводим имя пользователя
    name_input = driver.find_element(By.ID, "name_input")
    name_input.send_keys("Alice")

    # Находим кнопку "Отправить" и кликаем на нее
    submit_button = driver.find_element(By.ID, "submit_button")
    submit_button.click()

    # Находим элемент с приветствием и проверяем, что оно правильное
    greeting_message = driver.find_element(By.ID, "greeting_message")
    assert greeting_message.value_of_css_property("border-width") == "2px"


def test_greeting_message_color(driver):
    # Открываем веб-страницу
    driver.get("file:///D:/work/Python/pytest/test_web_page/index.html")

    # Находим поле для ввода имени и вводим имя пользователя
    name_input = driver.find_element(By.ID, "name_input")
    name_input.send_keys("Alice")

    # Находим кнопку "Отправить" и кликаем на нее
    submit_button = driver.find_element(By.ID, "submit_button")
    submit_button.click()

    # Находим элемент с приветствием и проверяем, что оно правильное
    greeting_message = driver.find_element(By.ID, "greeting_message")
    greeting_message_color_hex = Color.from_string(greeting_message.value_of_css_property("color")).hex
    assert greeting_message_color_hex == "#ffffff"