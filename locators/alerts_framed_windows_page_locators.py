from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.ID, 'tabButton')
    NEW_TAB_TEXT = (By.ID, 'sampleHeading')

    NEW_WINDOW_BUTTON = (By.ID, 'windowButton')

    NEW_WINDOW_MESSAGE_BUTTON = (By.ID, 'messageWindowButton')
    NEW_WINDOW_MESSAGE_TEXT = (By.TAG_NAME, 'body')
