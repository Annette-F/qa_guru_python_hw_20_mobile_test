import pytest
from selene import browser
from dotenv import load_dotenv
from appium import webdriver
import config
from selene_in_action.utils import attach


def pytest_addoption(parser):
    parser.addoption('--context', default='bstack', help='Specify the test context')


def pytest_configure(config):
    context = config.getoption('--context')
    env_file_path = f'.env.{context}'
    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture()
def context(request):
    return request.config.getoption('--context')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = config.to_driver_options(context=context)
    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    attach.add_bstack_screenshot(browser)
    attach.add_bstack_xml_dump(browser)

    session_id = browser.driver.session_id

    browser.quit()

    if context == 'bstack':
        attach.add_bstack_video(session_id)
