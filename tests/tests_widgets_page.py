import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage


class TestsWidgetsPage:

    class TestsAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            accordian_page.check_accordian()

    class TestsAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            auto_comlete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_comlete_page.open()
            auto_comlete_page.fill_input_multi()
            auto_comlete_page.fill_input_multi()
            auto_comlete_page.delete_all_values_from_multi()

        def test_fill_single_autocomplete(self, driver):
            auto_comlete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_comlete_page.open()
            auto_comlete_page.fill_input_single()

    class TestsDatePickerPage:

        def test_change_data(self, driver):
            data_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker_page.open()
            data_picker_page.select_date()
            time.sleep(3)

        def test_change_data_and_time(self, driver):
            data_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker_page.open()
            data_picker_page.select_date_and_time()
            time.sleep(3)

