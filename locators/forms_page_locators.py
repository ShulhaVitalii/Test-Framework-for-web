from selenium.webdriver.common.by import By


class TestFormPageLocators:
    FIRSTNAME_INPUT = (By.ID, 'firstName')
    LASTNAME_INPUT = (By.ID, 'lastName')
    EMAIL_INPUT = (By.ID, 'userEmail')

    # GENDER_RADIO
    GENDER = [(By.XPATH, '//label[@for="gender-radio-1"]'), (By.XPATH, '//label[@for="gender-radio-3"]'),
              (By.XPATH, '//label[@for="gender-radio-3"]')]

    MOBILE_INPUT = (By.ID, 'userNumber')
    DATE_OF_BIRTH_INPUT = (By.ID, 'dateOfBirthInput')
    SUBJECT = (By.ID, 'subjectsInput')

    # HOBBIES CHECKBOXES
    # SPORTS = (By.ID, 'hobbies-checkbox-1')
    # READING = (By.ID, 'hobbies-checkbox-2')
    # MUSIC = (By.ID, 'hobbies-checkbox-3')
    HOBBIES = [(By.XPATH, '//label[@for="hobbies-checkbox-1"]'), (By.XPATH, '//label[@for="hobbies-checkbox-2"]'),
               (By.XPATH, '//label[@for="hobbies-checkbox-3"]')]

    UPLOAD_PICTURE = (By.ID, 'uploadPicture')

    CURRENT_ADDRESS_TEXTAREA = (By.ID, 'currentAddress')

    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')

    SUBMIT = (By.ID, 'submit')

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
