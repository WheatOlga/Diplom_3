
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from faker import Faker
from urls import Urls

fake = Faker()


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    browser_name = request.param
    
    if browser_name == 'Chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=1440,920")
        browser = webdriver.Chrome(options=options)
    else:  # Firefox
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)
    
    browser.implicitly_wait(10)
    browser.get(Urls.BASE_URL)
    
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def create_user():
    """Фикстура создания пользователя через API"""
    user_data = {
        "name": fake.name(),
        "email": f"test_{fake.random_int(1000, 9999)}@yandex.ru",
        "password": fake.password()
    }
    
    response = requests.post(Urls.CREATE_USER, json=user_data)
    response_data = response.json()
    status_code = response.status_code
    
    yield user_data, response_data, status_code
    
    access_token = response_data.get('accessToken')
    if access_token:
        requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})
