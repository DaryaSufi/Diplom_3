import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from constants import Constants
from helpers import create_user

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param=='firefox':
        browser=webdriver.Firefox()
    elif request.param=='chrome':
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
    else:
        raise ValueError('Unknown browser type')
    yield browser
    browser.quit()

@pytest.fixture()
def create_and_delete_user_for_login():
    payload = create_user()
    responce = requests.post(f"{Constants.BURGERS_URL}/auth/register", json=payload)
    user_info = responce.json()
    yield responce, payload, user_info
    access_token = user_info["accessToken"]
    headers = {
        "Authorization": access_token
    }
    requests.delete(f"{Constants.BURGERS_URL}/auth/user", headers=headers)
