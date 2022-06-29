from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.ID, 'tabButton')
    NEW_TAB_TEXT = (By.ID, 'sampleHeading')

    NEW_WINDOW_BUTTON = (By.ID, 'windowButton')

    NEW_WINDOW_MESSAGE_BUTTON = (By.ID, 'messageWindowButton')
    NEW_WINDOW_MESSAGE_TEXT = (By.TAG_NAME, 'body')


class AlertPageLocators:
    BUTTON_TO_SE_ALERT = (By.ID, 'alertButton')
    BUTTON_TO_SE_ALERT_AFTER_5_SECONDS = (By.ID, 'timerAlertButton')
    BUTTON_TO_CONFIRM_BOX_WILL_APPEAR = (By.ID, 'confirmButton')
    CONFIRM_RESULT = (By.ID, 'confirmResult')
    BUTTON_TO_PROMPT_BOX_WILL_APPEAR = (By.ID, 'promtButton')
    PROMPT_RESULT = (By.ID, 'promptResult')


class FramesPageLocators:
    FRAME1 = (By.ID, 'frame1')
    FRAME2 = (By.ID, 'frame2')
    TITLE_FRAME = (By.ID, 'sampleHeading')
