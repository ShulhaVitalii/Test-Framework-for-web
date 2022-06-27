import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


def test_text_box(driver):
    test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    test_box_page.open()
    input_data = test_box_page.fill_all_fields()
    output_data = test_box_page.check_filled_form()
    for i in range(len(input_data)):
        assert input_data[i] == output_data[i], f'data {input_data[i]} does not match'
