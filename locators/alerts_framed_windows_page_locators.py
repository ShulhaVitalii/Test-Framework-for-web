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


class NestedFramesPageLocators:
    FRAME1 = (By.ID, 'frame1')
    FRAME2 = (By.XPATH, '// iframe[@srcdoc="<p>Child Iframe</p>"]')
    FRAME_TEXT = (By.TAG_NAME, 'body')


class ModalDialogsPageLocators:
    BUTTON_SMALL_MODAL = (By.ID, 'showSmallModal')
    TITLE_SMALL = (By.ID, 'example-modal-sizes-title-sm')
    BUTTON_CLOSE_SMALL_MODAL = (By.ID, 'closeSmallModal')

    BUTTON_LARGE_MODAL = (By.ID, 'showLargeModal')
    TITLE_LARGE = (By.ID, 'example-modal-sizes-title-lg')
    BUTTON_CLOSE_LARGE_MODAL = (By.ID, 'closeLargeModal')

