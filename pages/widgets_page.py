import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generate_color, generate_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, TooltipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self):
        self.element_is_visible(self.locators.HEADER_SECTION2).click()
        text = self.element_is_visible(self.locators.CONTENT_SECTION2).text
        assert 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those ' \
               'interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are' \
               ' also reproduced in their exact original form, accompanied by English versions from the 1914 ' \
               'translation by H. Rackham.' in text
        self.element_is_visible(self.locators.HEADER_SECTION3).click()
        text = self.element_is_visible(self.locators.CONTENT_SECTION3).text
        assert text == "It is a long established fact that a reader will be distracted by the readable content of a" \
                       " page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less" \
                       " normal distribution of letters, as opposed to using 'Content here, content here', making it " \
                       "look like readable English. Many desktop publishing packages and web page editors now use" \
                       " Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many" \
                       " web sites still in their infancy. Various versions have evolved over the years, sometimes by" \
                       " accident, sometimes on purpose (injected humour and the like)."
        self.element_is_visible(self.locators.HEADER_SECTION1).click()
        text = self.element_is_visible(self.locators.CONTENT_SECTION1).text
        assert text == "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has " \
                       "been the industry's standard dummy text ever since the 1500s, when an unknown printer took a " \
                       "galley of type and scrambled it to make a type specimen book. It has survived not only five" \
                       " centuries, but also the leap into electronic typesetting, remaining essentially unchanged." \
                       " It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum " \
                       "passages, and more recently with desktop publishing software like Aldus PageMaker including" \
                       " versions of Lorem Ipsum."


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        color = random.sample(next(generate_color()).color_name, k=1)
        input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
        input_multi.send_keys(color)
        input_multi.send_keys(Keys.ENTER)
        value = self.element_are_visible(self.locators.MULTI_VALUE)
        colors = []
        for v in value:
            colors.append(v.text)
        assert color[0] in colors, "Color don't be added"

    def delete_all_values_from_multi(self):
        count_value_before = len(self.element_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.element_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for button in remove_button_list:
            button.click()
        try:
            count_value_after = len(self.element_are_visible(self.locators.MULTI_VALUE))
        except TimeoutException:
            count_value_after = 0
        assert count_value_before != count_value_after, "Colors don't be removed"
        assert count_value_after == 0, "Colors don't be removed"

    def fill_input_single(self):
        color = random.sample(next(generate_color()).color_name, k=1)
        input = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input.send_keys(color)
        input.send_keys(Keys.ENTER)
        value = self.element_is_visible(self.locators.SINGLE_VALUE)
        assert color[0] == value.text, "Color don't be added"


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generate_date())
        input_date = self.element_is_visible(self.locators.INPUT_DATE)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.DATA_SELECT_MONTH, date.month)
        self.select_date_by_text(self.locators.DATA_SELECT_YEAR, date.year)
        self.select_date_item_from_list(self.locators.DATA_SELECT_DAY, date.day)
        input_date.send_keys(Keys.ENTER)
        value_date_after = input_date.get_attribute('value')
        assert value_date_before != value_date_after, 'The date has not changed'

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, elements, value):
        item_list = self.element_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_date_and_time(self):
        date = next(generate_date())
        input_date = self.element_is_visible(self.locators.INPUT_DATE_AND_TIME)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATA_AND_TIME_SELECT_MONTH).click()
        self.select_date_item_from_list(self.locators.DATA_AND_TIME_SELECT_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATA_AND_TIME_SELECT_YEAR).click()
        self.select_date_item_from_list(self.locators.DATA_AND_TIME_SELECT_YEAR_LIST, date.year)
        self.select_date_item_from_list(self.locators.DATA_AND_TIME_SELECT_TIME, date.time)
        input_date.send_keys(Keys.ENTER)
        value_date_after = input_date.get_attribute('value')
        assert value_date_before != value_date_after, 'The date and the time has not changed'


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def check_move_slider(self):
        slider_value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        slider_value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        assert slider_value_before != slider_value_after, 'The value of the slider has not changed'


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def check_progress(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        self.element_is_visible(self.locators.START_STOP_BUTTON).click()
        time.sleep(2)
        self.element_is_visible(self.locators.START_STOP_BUTTON).click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        assert value_after != value_before, 'The value of the progress bar has not changed'


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self):
        what_button = self.element_is_visible(self.locators.TAB_WHAT)
        origin_button = self.element_is_visible(self.locators.TAB_ORIGIN)
        use_button = self.element_is_visible(self.locators.TAB_USE)
        more_button = self.element_is_visible(self.locators.TAB_MORE)

        what_text = self.get_content(what_button, self.locators.WHAT_CONTENT)
        assert 'unchanged. It was popularised in the 1960s with ' in what_text, 'What text is wrong'
        origin_text = self.get_content(origin_button, self.locators.ORIGIN_CONTENT)
        assert ' sections 1.10.32 and 1.10.33 of "de Finibus B' in origin_text
        use_text = self.get_content(use_button, self.locators.USE_CONTENT)
        assert ' readable English. Many desktop publishing packages ' in use_text
        more_text = self.get_content(more_button, self.locators.MORE_CONTENT)
        assert more_text

    def get_content(self, button, locator):
        button.click()
        text = self.element_is_visible(locator).text
        return text


class TooltipsPage(BasePage):
    locators = TooltipsPageLocators()

    def check_too_tip(self):
        self.action_move_to_element(self.element_is_visible(self.locators.BUTTON))
        text = self.get_tool_tip_text()
        assert text == 'You hovered over the Button', "You don't hovered over the Button"

        self.action_move_to_element(self.element_is_visible(self.locators.INPUT))
        text = self.get_tool_tip_text()
        assert text == 'You hovered over the text field', "You don't hovered over the text field"

        self.action_move_to_element(self.element_is_visible(self.locators.LINK1))
        text = self.get_tool_tip_text()
        assert text == 'You hovered over the Contrary', "You don't hovered over the Contrary"

        self.action_move_to_element(self.element_is_visible(self.locators.LINK2))
        text = self.get_tool_tip_text()
        assert text == 'You hovered over the 1.10.32', "You don't hovered over the 1.10.32"

    def get_tool_tip_text(self):
        time.sleep(0.5)
        return self.element_is_visible(self.locators.TOOL_TIP).text


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        items = self.element_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in items:
            self.action_move_to_element(item)
            data.append(item.text)
        assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »',
                        'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], 'The menu opens incorrectly'


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def check_select_menu(self):
        self.element_is_visible(self.locators.SELECT_VALUE).click()
        text = random.choice(['Group 1, option 2', 'Group 1, option 2', 'Group 2, option 1', 'Group 2, option 2',
                              'A root option', 'Another root option'])
        self.get_element_from_text(text).click()
        result_text = self.element_is_visible(self.locators.SELECT_VALUE_TEXT).text
        assert text == result_text

    def check_select_one_menu(self):
        self.element_is_visible(self.locators.SELECT_ONE).click()
        text = random.choice(['Dr.', 'Mr.', 'Mrs.', 'Ms.', 'Prof.', 'Other'])
        self.get_element_from_text(text).click()
        result_text = self.element_is_visible(self.locators.SELECT_ONE_TEXT).text
        assert text == result_text

    def check_old_style_select_menu(self):
        color = random.sample(next(generate_color()).color_name, k=1)
        el = self.element_is_visible(self.locators.OLD_STYLE_SELECT_MENU)
        el.click()
        self.get_element_from_text(color[0]).click()
        self.get_element_from_text('Old Style Select Menu').click()
        assert self.get_element_from_text(color[0]), 'The color is not selected or wrong color selected'

