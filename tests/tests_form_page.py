import time

from pages.forms_page import FormPage


class TestFormPage:
    class TestFormPage:
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            form_page.check_form_result()
