from locators.alerts_framed_windows_page_locators import BrowserWindowsPageLocators
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
