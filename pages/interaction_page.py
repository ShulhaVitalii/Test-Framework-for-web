import random
import time

import allure

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.step('Getting sortable items')
    def get_sortable_items(self, elements):
        item_list = self.element_are_visible(elements)
        return [item.text for item in item_list]

    @allure.step('Changing order')
    def change_order(self, locator1, locator2):
        self.element_is_visible(locator1).click()
        order_before = self.get_sortable_items(locator2)

        # get 2 elements from item list
        item_list = random.sample(self.element_are_visible(locator2), k=2)

        self.action_drag_and_drop_to_element(item_list[0], item_list[1])
        order_after = self.get_sortable_items(locator2)
        with allure.step(f'Checking that order before: {order_before} != order after: {order_after}'):
            assert order_after != order_before, 'Order has not changed after sort'


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    @allure.step('Getting select item')
    def get_select_item(self, elements):
        selected_items = self.element_are_visible(elements)
        return selected_items

    @allure.step('Select elements')
    def select_elements(self, locator1, locator2, locator3):
        self.element_is_visible(locator1).click()
        # get 3 elements from item list
        items_to_select = random.sample(self.element_are_visible(locator2), k=3)
        for item in items_to_select:
            item.click()
        selected_items = self.get_select_item(locator3)
        with allure.step('Checking elements'):
            assert len(selected_items) == 3, 'Should be 3 selected items'
            assert sorted([item.text for item in items_to_select]) == sorted([item.text for item in selected_items]),\
                'Selected wrong items'


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    @allure.step('Getting box size')
    def get_box_size(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('Getting max and min sizes')
    def get_max_min_size(self, element):
        size = self.element_is_present(element).get_attribute('style')
        return size

    @allure.step('Changing size of resizable box')
    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.BOX_WITH_RESTRICTION_HANDLE), 400, 200)
        max_size = self.get_box_size(self.get_max_min_size(self.locators.BOX_WITH_RESTRICTION))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.BOX_WITH_RESTRICTION_HANDLE), -500, -300)
        min_size = self.get_box_size(self.get_max_min_size(self.locators.BOX_WITH_RESTRICTION))
        return max_size, min_size

    @allure.step('Changing size of resizable box without restriction')
    def change_size_resizable_box_without_restriction(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.BOX_WITHOUT_RESTRICTION_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_box_size(self.get_max_min_size(self.locators.BOX_WITHOUT_RESTRICTION))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.BOX_WITHOUT_RESTRICTION_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_box_size(self.get_max_min_size(self.locators.BOX_WITHOUT_RESTRICTION))
        return max_size, min_size

    @allure.step('Checking resizable box')
    def check_resizable_box(self):
        max_size, min_size = self.change_size_resizable_box()
        assert ('500px', '300px') == max_size, 'Max size not equal to 500px, 300px'
        assert ('150px', '150px') == min_size, 'Max size not equal to 150px, 150px'

    @allure.step('Checking resizable box without restriction')
    def check_resizable_box_without_restriction(self):
        max_size, min_size = self.change_size_resizable_box_without_restriction()
        assert min_size != max_size, 'resizable box without restriction has not been changed'


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    @allure.step('Checking simple tab')
    def check_simple_tab(self):
        self.element_is_visible(self.locators.TAB_SIMPLE).click()
        text_before = self.element_is_visible(self.locators.DROP_HERE_TEXT).text
        element_to_drag = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        element_to_drop = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(element_to_drag, element_to_drop)
        text_after = self.element_is_visible(self.locators.DROP_HERE_TEXT).text
        assert text_before != text_after, "The element don't has been dragged or dropped"
        assert text_after == 'Dropped!', 'Wrong text after dropping'

    @allure.step('Checking accept tab')
    def check_accept_tab(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        text_before = self.element_is_visible(self.locators.DROP_HERE_ACCEPT_TEXT).text
        element_to_drag = self.element_is_visible(self.locators.NON_ACCEPTABLE)
        element_to_drop = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(element_to_drag, element_to_drop)
        text_after = self.element_is_visible(self.locators.DROP_HERE_ACCEPT_TEXT).text
        assert text_before == text_after, "The text should not changed"
        element_to_drag = self.element_is_visible(self.locators.ACCEPTABLE)
        self.action_drag_and_drop_to_element(element_to_drag, element_to_drop)
        text_after = self.element_is_visible(self.locators.DROP_HERE_ACCEPT_TEXT).text
        assert text_before != text_after, "The element don't has been dragged or dropped"
        assert text_after == 'Dropped!', 'Wrong text after dropping'

    @allure.step('Drag and drop')
    def drag_and_drop(self, el_drag, el_drop):
        element_to_drag = self.element_is_visible(el_drag)
        element_to_drop = self.element_is_visible(el_drop)
        self.action_drag_and_drop_to_element(element_to_drag, element_to_drop)
        text_after = []
        for text in self.element_are_visible(self.locators.PP_TEXT_LIST):
            text_after.append(text.text)
        return text_after

    @allure.step('Checking propogation tab')
    def check_prevent_propogation_tab(self):
        self.element_is_visible(self.locators.PP).click()
        text_before = []
        for text in self.element_are_visible(self.locators.PP_TEXT_LIST):
            text_before.append(text.text)
        text_after = self.drag_and_drop(self.locators.PP_DRAG_ME, self.locators.PP_NOT_GREEDY_INNER)
        with allure.step('Checking text after drag and drop'):
            assert text_before != text_after
            assert text_after == ['Dropped!', 'Dropped!', 'Outer droppable', 'Inner droppable (greedy)']

        text_after = self.drag_and_drop(self.locators.PP_DRAG_ME, self.locators.PP_GREEDY_INNER)
        with allure.step('Checking text after drag and drop'):
            assert text_after == ['Dropped!', 'Dropped!', 'Outer droppable', 'Dropped!']

        text_after = self.drag_and_drop(self.locators.PP_DRAG_ME, self.locators.PP_GREEDY)
        with allure.step('Checking text after drag and drop'):
            assert text_after == ['Dropped!', 'Dropped!', 'Dropped!', 'Dropped!']

    @allure.step('Checking draggable tab')
    def check_revert_draggable_tab(self):
        self.element_is_visible(self.locators.RD).click()
        text_before = self.element_is_visible(self.locators.RD_DROP_HERE).text
        element_to_drag = self.element_is_visible(self.locators.RD_NOT_REVERT)
        element_to_drop = self.element_is_visible(self.locators.RD_DROP_HERE)
        self.action_drag_and_drop_to_element(element_to_drag, element_to_drop)
        coord_after_move = self.element_is_visible(self.locators.RD_NOT_REVERT).get_attribute('style')
        time.sleep(1)
        coord_after_1_sec = self.element_is_visible(self.locators.RD_NOT_REVERT).get_attribute('style')
        with allure.step('Checking coordinates after move'):
            assert coord_after_move == coord_after_1_sec, \
                "The coordinates should be the same, the element reversed but shouldn't"

        text_after = self.element_is_visible(self.locators.RD_DROP_HERE).text
        with allure.step('Checking text after move'):
            assert text_before != text_after, "The element don't has been dragged or dropped"

        element_to_drag = self.element_is_visible(self.locators.RD_WILL_REVERT)
        element_to_drop = self.element_is_visible(self.locators.RD_DROP_HERE)
        self.action_drag_and_drop_to_element(element_to_drag, element_to_drop)
        coord_after_move = self.element_is_visible(self.locators.RD_WILL_REVERT).get_attribute('style')
        time.sleep(1)
        coord_after_1_sec = self.element_is_visible(self.locators.RD_WILL_REVERT).get_attribute('style')
        print(coord_after_1_sec, coord_after_move)
        with allure.step('Checking coordinates after move'):
            assert coord_after_move != coord_after_1_sec, "The element was not reversed back"
            assert coord_after_1_sec == 'position: relative; left: 0px; top: 0px;', "The element was not reversed back"


class DragabblePage(BasePage):
    locators = DragabblePageLocators()

    @allure.step('Checking that all tabs are clickable')
    def all_tab_is_clickable(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        assert self.element_is_visible(self.locators.SIMPLE_TAB).get_attribute('aria-selected') == 'true',\
            'The tab is not active'
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        assert self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).get_attribute('aria-selected') == 'true',\
            'The tab is not active'
        self.element_is_visible(self.locators.CONTAINER_RESTRICTED_TAB).click()
        assert self.element_is_visible(self.locators.CONTAINER_RESTRICTED_TAB).get_attribute('aria-selected') == 'true',\
            'The tab is not active'
        self.element_is_visible(self.locators.CURSOR_STYLE_TAB).click()
        assert self.element_is_visible(self.locators.CURSOR_STYLE_TAB).get_attribute('aria-selected') == 'true',\
            'The tab is not active'

    def dragabble_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_me = self.element_is_visible(self.locators.DRAG_ME)
        position_before = drag_me.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_me, 200, 200)
        position_after = drag_me.get_attribute('style')
        with allure.step('Checking element position after move'):
            assert position_before != position_after, "The element doesn't move"

    @allure.step('Checking axis restricted')
    def check_axis_restricted(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        drag_me = self.element_is_visible(self.locators.ONLY_X)
        self.action_drag_and_drop_by_offset(drag_me, 200, 200)
        position = drag_me.get_attribute('style').split(';')[2].split(':')[1]
        with allure.step('Checking that element coordinate changed only in X'):
            assert position == ' 0px', "The element moved on Y but shouldn't be"

        drag_me = self.element_is_visible(self.locators.ONLY_Y)
        self.action_drag_and_drop_by_offset(drag_me, 200, 200)
        position = drag_me.get_attribute('style').split(';')[1].split(':')[1]
        with allure.step('Checking that element coordinate changed only in Y'):
            assert position == ' 0px', "The element moved on X but shouldn't be"
