import datetime
import os

import allure
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True, scope='function')
def driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())

    if os.getenv('INSIDE_DOCKER', 'False').capitalize() == 'True':
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    options.add_argument('windows-size=1920x1080')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'screenshot={datetime.datetime.today()}', attachment_type=allure.attachment_type.PNG)
    driver.quit()

