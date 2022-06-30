from pages.widgets_page import AccordianPage, AutoCompletePage


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


