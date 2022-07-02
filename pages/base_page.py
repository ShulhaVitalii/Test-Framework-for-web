import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        with allure.step(f'Open url {self.url}'):
            self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        with allure.step(f'Return element if visible'):
            self.go_to_element(self.element_is_present(locator))
            return wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=10):
        with allure.step(f'Return elements list if visible'):
            return wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
        with allure.step(f'Return element if present'):
            return wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=10):
        with allure.step(f'Return elements if present'):
            return wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        with allure.step(f'Return element if not visible'):
            return wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        with allure.step(f'Return element if clickable'):
            return wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def go_to_element(self, locator):
        with allure.step(f'Go to element with locator {locator}'):
            self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def action_right_click(self, locator):
        with allure.step(f'Right click on element with locator {locator}'):
            action = ActionChains(self.driver)
            action.context_click(locator).perform()

    def action_double_click(self, locator):
        with allure.step(f'Double click on element with locator {locator}'):
            action = ActionChains(self.driver)
            action.double_click(locator).perform()

    def switch_to_new_tab(self):
        with allure.step(f'Switch to new tab'):
            self.driver.switch_to.window(self.driver.window_handles[1])

    def remove_footer(self):
        with allure.step(f'Remove footer'):
            self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
            self.driver.execute_script("document.getElementById('close-fixedban').remove();")
            self.driver.execute_script("document.getElementById('adplus-anchor').remove();")

    def check_new_tab(self, locator1, locator2):
        with allure.step(f'Checking new tab'):
            self.element_is_visible(locator1).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text = self.element_is_visible(locator2).text
            return text

    def action_drag_and_drop_by_offset(self, element, x_coord, y_coord):
        with allure.step(f'Drag and drop by offset x: {x_coord} y: {y_coord}'):
            action = ActionChains(self.driver)
            action.drag_and_drop_by_offset(element, x_coord, y_coord)
            action.perform()

    def action_move_to_element(self, element):
        with allure.step(f'Move to element {element}'):
            action = ActionChains(self.driver)
            action.move_to_element(element)
            action.perform()

    def get_element_from_text(self, text):
        with allure.step(f'Get element from text: {text}'):
            return self.element_is_visible((By.XPATH, f'//*[contains(text(), "{text}")]'))

    def action_drag_and_drop_to_element(self, what, where):
        with allure.step(f'Drag and drop element: {what} to element: {where}'):
            action = ActionChains(self.driver)
            action.drag_and_drop(what, where)
            action.perform()
