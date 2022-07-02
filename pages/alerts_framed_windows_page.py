import time

import allure
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert

from locators.alerts_framed_windows_page_locators import BrowserWindowsPageLocators, AlertPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_tab_is_open(self):
        with allure.step(f'Checking that new tab is open'):
            text = self.check_new_tab(self.locators.NEW_TAB_BUTTON, self.locators.NEW_TAB_TEXT)
            assert text == 'This is a sample page'

    def check_new_window_is_open(self):
        with allure.step(f'Checking that new window is open'):
            text = self.check_new_tab(self.locators.NEW_WINDOW_BUTTON, self.locators.NEW_TAB_TEXT)
            assert text == 'This is a sample page'

    def check_new_window_message_is_open(self):
        with allure.step(f'Checking that new message window is open'):
            self.element_is_present(self.locators.NEW_WINDOW_MESSAGE_BUTTON).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text = self.element_is_present(self.locators.NEW_WINDOW_MESSAGE_TEXT).text
            assert text == 'Knowledge increases by sharing but not by saving. Please share this website with your' \
                           ' friends and in your organization.'


class AlertPage(BasePage):
    locators = AlertPageLocators()

    def check_see_alert(self):
        with allure.step(f'Checking alert'):
            self.element_is_visible(self.locators.BUTTON_TO_SE_ALERT).click()
            # alert = self.driver.switch_to.alert
            alert = Alert(self.driver)
            assert alert.text == 'You clicked a button'

    def check_see_alert_after_5_second(self):
        self.element_is_visible(self.locators.BUTTON_TO_SE_ALERT_AFTER_5_SECONDS).click()
        time.sleep(5)
        with allure.step(f'Checking alert after 5 seconds'):
            try:
                alert = Alert(self.driver)
                assert alert.text == 'This alert appeared after 5 seconds'
            except UnexpectedAlertPresentException:
                assert alert.text == 'This alert appeared after 5 seconds'

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.BUTTON_TO_CONFIRM_BOX_WILL_APPEAR).click()
        with allure.step(f'Checking confirm alert'):
            try:
                alert = Alert(self.driver)
                alert.accept()
                assert 'Ok' in self.element_is_visible(self.locators.CONFIRM_RESULT).text
            except UnexpectedAlertPresentException:
                assert 'Ok' in self.element_is_visible(self.locators.CONFIRM_RESULT).text

    def check_prompt_alert(self):
        self.element_is_visible(self.locators.BUTTON_TO_PROMPT_BOX_WILL_APPEAR).click()
        with allure.step(f'Checking prompt alert'):
            try:
                alert = Alert(self.driver)
                alert.send_keys('MyName')
                alert.accept()
                assert 'MyName' in self.element_is_visible(self.locators.PROMPT_RESULT).text
            except UnexpectedAlertPresentException:
                assert 'MyName' in self.element_is_visible(self.locators.PROMPT_RESULT).text


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('Checking frame')
    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FRAME1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            with allure.step(f'Checking that frame width = 500px'):
                assert width == '500px', 'The frame does not exist'
            with allure.step(f'Checking that frame height = 350px'):
                assert height == '350px', 'The frame does not exist'
            with allure.step(f'Checking that text: {text} = This is a sample page'):
                assert text == 'This is a sample page', 'The frame does not exist'

        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.FRAME2)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            with allure.step(f'Checking that frame width = 100px'):
                assert width == '100px', 'The frame does not exist'
            with allure.step(f'Checking that frame height = 100px'):
                assert height == '100px', 'The frame does not exist'
            with allure.step(f'Checking that text: {text} = This is a sample page'):
                assert text == 'This is a sample page', 'The frame does not exist'


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FRAME1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            with allure.step(f'Checking that frame width = 500px'):
                assert width == '500px', 'The frame does not exist'
            with allure.step(f'Checking that frame height = 350px'):
                assert height == '350px', 'The frame does not exist'
            with allure.step(f'Checking that text: {text} = Parent frame'):
                assert text == 'Parent frame', 'The frame does not exist'

        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.FRAME2)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.driver.switch_to.default_content()
            with allure.step(f'Checking that frame width = Null'):
                assert width == '', 'The frame does not exist'
            with allure.step(f'Checking that frame height = Null'):
                assert height == '', 'The frame does not exist'
            with allure.step(f'Checking that text: {text} = Child Iframe'):
                assert text == 'Child Iframe', 'The frame does not exist'


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_that_small_modal_window_is_open(self):
        self.element_is_visible(self.locators.BUTTON_SMALL_MODAL).click()
        title = self.element_is_visible(self.locators.TITLE_SMALL).text
        self.element_is_visible(self.locators.BUTTON_CLOSE_SMALL_MODAL).click()
        with allure.step(f'Checking that small modal window is open'):
            assert title == 'Small Modal', 'This is wrong modal window'

    def check_that_large_modal_window_is_open(self):
        self.element_is_visible(self.locators.BUTTON_LARGE_MODAL).click()
        title = self.element_is_visible(self.locators.TITLE_LARGE).text
        self.element_is_visible(self.locators.BUTTON_CLOSE_LARGE_MODAL).click()
        with allure.step(f'Checking that large modal window is open'):
            assert title == 'Large Modal', 'This is wrong modal window'

