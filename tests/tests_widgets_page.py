from pages.widgets_page import AccordianPage


class TestsWidgetsPage:

    class TestsAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            accordian_page.check_accordian()
