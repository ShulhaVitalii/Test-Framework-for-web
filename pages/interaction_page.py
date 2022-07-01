import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.element_are_visible(elements)
        return [item.text for item in item_list]

    def change_order(self, locator1, locator2):
        self.element_is_visible(locator1).click()
        order_before = self.get_sortable_items(locator2)

        # get 2 elements from item list
        item_list = random.sample(self.element_are_visible(locator2), k=2)

        self.action_drag_and_drop_to_element(item_list[0], item_list[1])
        order_after = self.get_sortable_items(locator2)
        assert order_after != order_before, 'Order has not changed after sort'


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def get_select_item(self, elements):
        selected_items = self.element_are_visible(elements)
        return selected_items

    def select_elements(self, locator1, locator2, locator3):
        self.element_is_visible(locator1).click()
        # get 3 elements from item list
        items_to_select = random.sample(self.element_are_visible(locator2), k=3)
        for item in items_to_select:
            item.click()
        selected_items = self.get_select_item(locator3)
        assert len(selected_items) == 3, 'Should be 3 selected items'
        assert sorted([item.text for item in items_to_select]) == sorted([item.text for item in selected_items]),\
            'Selected wrong items'


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_box_size(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element).get_attribute('style')
        return size

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.BOX_WITH_RESTRICTION_HANDLE), 400, 200)
        max_size = self.get_box_size(self.get_max_min_size(self.locators.BOX_WITH_RESTRICTION))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.BOX_WITH_RESTRICTION_HANDLE), -500, -300)
        min_size = self.get_box_size(self.get_max_min_size(self.locators.BOX_WITH_RESTRICTION))
        return max_size, min_size

    def change_size_resizable_box_without_restriction(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.BOX_WITHOUT_RESTRICTION_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_box_size(self.get_max_min_size(self.locators.BOX_WITHOUT_RESTRICTION))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.BOX_WITHOUT_RESTRICTION_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_box_size(self.get_max_min_size(self.locators.BOX_WITHOUT_RESTRICTION))
        return max_size, min_size

    def check_resizable_box(self):
        max_size, min_size = self.change_size_resizable_box()
        assert ('500px', '300px') == max_size, 'Max size not equal to 500px, 300px'
        assert ('150px', '150px') == min_size, 'Max size not equal to 150px, 150px'

    def check_resizable_box_without_restriction(self):
        max_size, min_size = self.change_size_resizable_box_without_restriction()
        assert min_size != max_size, 'resizable box without restriction has not been changed'


class DroppablePage(BasePage):
    locators = DroppablePageLocators()


class DragabblePage(BasePage):
    locators = DragabblePageLocators()
