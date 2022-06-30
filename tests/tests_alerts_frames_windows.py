from pages.alerts_framed_windows_page import BrowserWindowsPage, AlertPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


class TestAlertsFramesWindows:
    class TestBrowserWindowsPage:

        def test_new_tab(self, driver):
            browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows.open()
            browser_windows.check_new_tab_is_open()

        def test_new_window(self, driver):
            browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows.open()
            browser_windows.check_new_window_is_open()

        def test_new_window_message(self, driver):
            browser_windows = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows.open()
            pass

    class TestAlertPage:

        def test_see_alert(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_page.check_see_alert()

        def test_see_alert_after_5_second(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_page.check_see_alert_after_5_second()

        def test_confirm_alert(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_page.check_confirm_alert()

        def test_prompt_alert(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_page.check_prompt_alert()

    class TestFramesPage:

        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            frames_page.check_frame('frame1')
            frames_page.check_frame('frame2')

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            nested_frame_page.check_nested_frame('frame1')
            nested_frame_page.check_nested_frame('frame2')

    class TestModalDialogs:

        def test_modal(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            modal_dialog_page.check_that_small_modal_window_is_open()
            modal_dialog_page.check_that_large_modal_window_is_open()
