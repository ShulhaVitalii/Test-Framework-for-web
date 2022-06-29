from pages.alerts_framed_windows_page import BrowserWindowsPage


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

