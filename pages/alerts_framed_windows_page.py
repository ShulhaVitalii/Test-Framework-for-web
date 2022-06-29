import time

from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert

from locators.alerts_framed_windows_page_locators import BrowserWindowsPageLocators, AlertPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_tab_is_open(self):
        text = self.check_new_tab(self.locators.NEW_TAB_BUTTON, self.locators.NEW_TAB_TEXT)
        assert text == 'This is a sample page'

    def check_new_window_is_open(self):
        text = self.check_new_tab(self.locators.NEW_WINDOW_BUTTON, self.locators.NEW_TAB_TEXT)
        assert text == 'This is a sample page'

    def check_new_window_message_is_open(self):
        self.element_is_present(self.locators.NEW_WINDOW_MESSAGE_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_present(self.locators.NEW_WINDOW_MESSAGE_TEXT).text
        assert text == 'Knowledge increases by sharing but not by saving. Please share this website with your' \
                       ' friends and in your organization.'


class AlertPage(BasePage):
    locators = AlertPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.BUTTON_TO_SE_ALERT).click()
        # alert = self.driver.switch_to.alert
        alert = Alert(self.driver)
        assert alert.text == 'You clicked a button'

    def check_see_alert_after_5_second(self):
        self.element_is_visible(self.locators.BUTTON_TO_SE_ALERT_AFTER_5_SECONDS).click()
        time.sleep(5)
        try:
            alert = Alert(self.driver)
            assert alert.text == 'This alert appeared after 5 seconds'
        except UnexpectedAlertPresentException:
            assert alert.text == 'This alert appeared after 5 seconds'

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.BUTTON_TO_CONFIRM_BOX_WILL_APPEAR).click()
        try:
            alert = Alert(self.driver)
            alert.accept()
            assert 'Ok' in self.element_is_visible(self.locators.CONFIRM_RESULT).text
        except UnexpectedAlertPresentException:
            assert 'Ok' in self.element_is_visible(self.locators.CONFIRM_RESULT).text

    def check_prompt_alert(self):
        self.element_is_visible(self.locators.BUTTON_TO_PROMPT_BOX_WILL_APPEAR).click()
        try:
            alert = Alert(self.driver)
            alert.send_keys('MyName')
            alert.accept()
            assert 'MyName' in self.element_is_visible(self.locators.PROMPT_RESULT).text
        except UnexpectedAlertPresentException:
            assert 'MyName' in self.element_is_visible(self.locators.PROMPT_RESULT).text
