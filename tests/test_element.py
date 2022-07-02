import random
import time
import allure
import pytest

from locators.elements_page_locators import LinksPageLocators
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:
        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            test_box_page.open()
            input_data = test_box_page.fill_all_fields()
            output_data = test_box_page.check_filled_form()
            for i in range(len(input_data)):
                assert input_data[i] == output_data[i], f'data {input_data[i]} does not match'

    @allure.feature('CheckBox')
    class TestCheckBox:
        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_on_random_checkbox_ten_times()
            check_box_page.check_result()
            time.sleep(5)

    @allure.feature('RadioButtonPage')
    class TestRadioButton:
        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_yes_radio()
            radio_button_page.click_on_impressive_radio()
            radio_button_page.click_on_no_radio()

    @allure.feature('WebTablePage')
    class TestWebTable:
        @allure.title('Check WebTable')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.checking_that_new_person_is_in_table()
            time.sleep(5)

        @allure.title('Check WebTable')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key = web_table_page.new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key)
            table_result = web_table_page.check_search_person()
            assert key in table_result, f'Key {key} is not found in the table'

        @allure.title('Check WebTable')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'The person card has not been changed'

        @allure.title('Check WebTable')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleting()
            assert text == 'No rows found', f'Person with email: {email} do not deleted'

        @allure.title('Check WebTable')
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or ' \
                                                      'changed incorrect'

    @allure.feature('ButtonsPage')
    class TestButtons:
        @allure.title('Check Buttons')
        def test_all_buttons_are_working_correctly(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            button_page.click_on_the_buttons()

    @allure.feature('LinksPage')
    class TestLinks:
        @allure.title('Check Links')
        @pytest.mark.parametrize('link', [LinksPageLocators.LINK_HOME, LinksPageLocators.DYNAMIC_LINK])
        def test_new_page_open_after_click_on_link(self, driver, link):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_that_new_page_is_opened(link)

        @allure.title('Check Links')
        @pytest.mark.parametrize('link, code, text', [(LinksPageLocators.LINK_CREATE, 201, 'Created'),
                                                      (LinksPageLocators.LINK_NO_CONTENT, 204, 'No Content'),
                                                      (LinksPageLocators.LINK_MOVED, 301, 'Moved Permanently'),
                                                      (LinksPageLocators.LINK_BAD_REQUEST, 400, 'Bad Request'),
                                                      (LinksPageLocators.LINK_UNAUTHORIZED, 401, 'Unauthorized'),
                                                      (LinksPageLocators.LINK_FORBIDDEN, 403, 'Forbidden'),
                                                      (LinksPageLocators.LINK_NO_FOUND, 404, 'Not Found')])
        def test_api_call_send_correct(self, driver, link, code, text):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            links_page.check_api_call(link, code, text)

    @allure.feature('UploadDownloadPage')
    class TestUploadDownload:
        @allure.title('Check UploadDownload')
        def test_upload(self, driver):
            upload_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            upload_page.upload_file()

        @allure.title('Check UploadDownload')
        def test_download(self, driver):
            download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            download_page.download_file()

    @allure.feature('DynamicPropertiesPag')
    class TestDynamicProperties:
        @allure.title('Check that button is enabled')
        def test_enable_button_after_5_seconds(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            assert dynamic_properties.check_that_button_is_enabled() is True, 'The button is not enabled'

        @allure.title('Check that color is change')
        def test_button_change_color_after_5_seconds(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            dynamic_properties.check_change_of_color()

        @allure.title('Check that button is appear')
        def test_button_appear(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            assert dynamic_properties.check_button_appear() is True, 'The button is not appear'
