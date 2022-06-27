import random
import time
from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace('\n', '')
        permanent_address = person_info.permanent_address.replace('\n', '')

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_clickable(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.BUTTON_EXPAND_ALL).click()

    def click_random_check_box(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        item = item_list[random.randrange(len(item_list))]
        self.go_to_element(item)
        item.click()

    def click_on_random_checkbox_ten_times(self):
        for _ in range(10):
            self.click_random_check_box()

    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text.lower().replace(' ', '').replace('.doc', ''))
        return data

    def get_output_result(self):
        output_result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in output_result_list:
            data.append(item.text.lower())
        return data

    def check_result(self):
        checked, outputs = self.get_checked_checkboxes(), self.get_output_result()
        assert checked == outputs, f'list {checked} and {outputs} are not equal'


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_yes_radio(self):
        self.element_is_clickable(self.locators.RADIO_YES).click()
        assert self.element_is_present(self.locators.SELECTED_RADIO).text == 'Yes', 'radio Yes is not active'

    def click_on_impressive_radio(self):
        self.element_is_clickable(self.locators.RADIO_IMPRESSIVE).click()
        assert self.element_is_present(self.locators.SELECTED_RADIO).text == 'Impressive',\
            'radio impressive is not active'

    def click_on_no_radio(self):
        self.element_is_clickable(self.locators.RADIO_NO).click()
        assert self.element_is_present(self.locators.SELECTED_RADIO).text == 'No', 'radio No is not active'


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)

            self.element_is_visible(self.locators.SUBMIT).click()

            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_person(self):
        person_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def checking_that_new_person_is_in_table(self):
        assert self.new_person() in self.check_new_person()

    def search_some_person(self, key):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key)

    def check_search_person(self):
        delete_button = self.element_are_present(self.locators.DELETE_BUTTON)
        row = delete_button[0].find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()
