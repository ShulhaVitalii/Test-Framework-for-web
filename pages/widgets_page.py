import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generate_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
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
