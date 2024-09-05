import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os
from dotenv import load_dotenv
from appium import webdriver

import config

from selene_in_action.utils import attach
from selene_in_action import utils


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options()

    if config.deviceName:
        options.set_capability('ddeviceName', config.deviceName)

    if config.appWaitActivity:
        options.set_capability('appWaitActivity', config.appWaitActivity)

    options.set_capability('app', (
        config.app if (config.app.startswith('/') or config.runs_on_bstack)
        else utils.file.abs_path_from_project(config.app)
    ))


    if config.runs_on_bstack:
        options.set_capability('platformVersion', '9.0')
        # login = os.getenv('USER_NAME')
        # access_key = os.getenv('ACCESS_KEY')
        options.set_capability(
        # 'app': config.app_url,
        # 'app': os.getenv('APP_URL'),
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': config.bstack_userName,
                'accessKey': config.bstack_accessKey
        }
    )

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(config.remote_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    attach.add_bstack_screenshot(browser)
    attach.add_bstack_xml_dump(browser)

    session_id = browser.driver.session_id

    with allure.step('Tear down app session with id: ' + session_id):
        browser.quit()


    if config.runs_on_bstack:
        attach.add_bstack_video(session_id)



