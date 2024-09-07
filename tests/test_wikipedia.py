import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.tag('Mobile')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('App-mobile test on "Wikipedia"')
@allure.story('Verify onboarding screen on "Wikipedia"')
def test_verify_onboarding_screen():
    with allure.step('Verify first onboarding screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('The Free Encyclopedia\n…in over 300 languages'))
    with allure.step('Verify second onboarding screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))
    with allure.step('Verify third onboarding screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))
    with allure.step('Verify forth onboarding screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Data & Privacy'))
    with allure.step('Search screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Java')
