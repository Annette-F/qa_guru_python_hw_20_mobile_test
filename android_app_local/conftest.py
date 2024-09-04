import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os
from dotenv import load_dotenv
from appium import webdriver

import config

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():

    # login = os.getenv('USER_NAME')
    # access_key = os.getenv('ACCESS_KEY')
    options = UiAutomator2Options().load_capabilities({
        'deviceName': 'SM-M325FV',
        'appWaitActivity': 'org.wikipedia.*',
        'app': '/Users/Anna/Downloads/app-alpha-universal-release.apk',
        # 'app': os.getenv('APP_URL'),

    })

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    attach.add_bstack_screenshot(browser)
    attach.add_bstack_xml_dump(browser)

    # session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()