from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Text Box form fields
    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
    SUBMIT = (By.ID, 'submit')

    CREATED_FULL_NAME = (By.ID, 'name')
    CREATED_EMAIL = (By.ID, 'email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    BUTTON_EXPAND_ALL = (By.XPATH, '//button[@title="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonPageLocators:
    RADIO_YES = (By.XPATH, '//label[@for="yesRadio"]')
    RADIO_NO = (By.XPATH, '//label[@for="noRadio"]')
    RADIO_IMPRESSIVE = (By.XPATH, '//label[@for="impressiveRadio"]')
    SELECTED_RADIO = (By.CSS_SELECTOR, 'span[class="text-success"]')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.ID, 'addNewRecordButton')
    FIRSTNAME_INPUT = (By.ID, 'firstName')
    LASTNAME_INPUT = (By.ID, 'lastName')
    EMAIL_INPUT = (By.ID, 'userEmail')
    AGE_INPUT = (By.ID, 'age')
    SALARY_INPUT = (By.ID, 'salary')
    DEPARTMENT_INPUT = (By.ID, 'department')
    SUBMIT = (By.ID, 'submit')

    # tables
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')
    SEARCH_INPUT = (By.ID, 'searchBox')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROWS_FOUND_TEXT = (By.XPATH, '//div[@class="rt-noData"]')
    COUNT_ROW_LIST = (By.XPATH, '//span[@class="select-wrap -pageSizeOptions"]')

    # update
    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

