import os
import random

from selenium.webdriver import Keys

from generator.generator import generated_person, generate_subject_list, generated_file
from locators.forms_page_locators import TestFormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = TestFormPageLocators()

    def filling_out_the_form(self):

        person_info = next(generated_person())
        firstname = person_info.firstname
        lastname = person_info.lastname
        email = person_info.email
        gender = person_info.gender
        mobile = person_info.mobile_number
        data_of_birth = person_info.date_of_birth
        hobbies = person_info.hobbies
        current_address = person_info.current_address

        subjects = generate_subject_list()
        subject = subjects[0]

        file_name, path = generated_file()

        self.remove_footer()

        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_clickable(self.locators.GENDER[gender]).click()
        self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(mobile)
        #self.element_is_visible(self.locators.DATE_OF_BIRTH_INPUT).clear().send_keys(data_of_birth)
        self.element_is_visible(self.locators.SUBJECT).send_keys(subject)
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_clickable(self.locators.HOBBIES[hobbies]).click()
        self.element_is_present(self.locators.UPLOAD_PICTURE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_TEXTAREA).send_keys(current_address)
        self.element_is_present(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(random.choice(['NCR', 'Uttar Pradesh', 'Haryana',
                                                                                     'Rajasthan']))
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()

        return person_info, subject, file_name

    def get_form_result(self):
        data = []
        rows = self.element_are_visible(self.locators.RESULT_TABLE)
        for row in rows:
            data.append(row.text)
        return data

    def check_form_result(self):
        person_data, subject, file_name = self.filling_out_the_form()
        gender = ['Male', 'Female', 'Other']
        hobbies = ['Sports', 'Reading', 'Music']
        result_data = self.get_form_result()

        assert result_data[0] == f'{person_data.firstname} {person_data.lastname}', 'Names not match'
        assert result_data[1] == person_data.email, 'Emails not match'
        assert result_data[3] == person_data.mobile_number, 'Mobile numbers not match'
        assert result_data[2] == gender[person_data.gender], 'Genders not match'
        assert result_data[4] == '29 June,2022', 'Dates not match'
        assert result_data[5] == subject, 'Subjects not match'
        assert result_data[6] == hobbies[person_data.hobbies], 'Hobbies not match'
        assert result_data[7] == file_name, 'File names not match'
        assert result_data[8] == person_data.current_address.replace("\n", " "), 'Addresses not match'

