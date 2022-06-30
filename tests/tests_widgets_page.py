import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    TooltipsPage, MenuPage, SelectMenuPage


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

    class TestsSliderPage:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            slider_page.check_move_slider()

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            progress_bar_page.check_progress()

    class TestTabsPage:
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            tabs_page.check_tabs()

    class TestsToolTipsPage:
        def test_tool_tips(self, driver):
            tool_tips_page = TooltipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            tool_tips_page.check_too_tip()

    class TestMenuPage:
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            menu_page.check_menu()

    class TestSelectMenu:
        def test_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            select_menu_page.check_select_menu()

        def test_select_one_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            select_menu_page.check_select_one_menu()

        def test_old_style_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            select_menu_page.check_old_style_select_menu()
