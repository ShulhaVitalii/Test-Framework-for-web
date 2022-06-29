from pages.alerts_framed_windows_page import BrowserWindowsPage, AlertPage


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
