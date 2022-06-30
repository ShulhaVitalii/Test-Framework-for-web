from selenium.webdriver.common.by import By


class AccordianPageLocators:
    HEADER_SECTION1 = (By.ID, 'section1Heading')
    HEADER_SECTION2 = (By.ID, 'section2Heading')
    HEADER_SECTION3 = (By.ID, 'section3Heading')

    CONTENT_SECTION1 = (By.ID, 'section1Content')
    CONTENT_SECTION2 = (By.ID, 'section2Content')
    CONTENT_SECTION3 = (By.ID, 'section3Content')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.ID, 'autoCompleteMultipleInput')
    MULTI_VALUE = (By.XPATH, '// div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.XPATH, '// div[@class="css-xb97g8 auto-complete__multi-value__remove"]')

    SINGLE_INPUT = (By.ID, 'autoCompleteSingleInput')
    SINGLE_VALUE = (By.XPATH, '// div[@class="auto-complete__single-value css-1uccc91-singleValue"]')

