import pytest

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.interaction_page import SortablePage, ResizablePage, SelectablePage, DroppablePage, DragabblePage


class TestInteractions:

    class TestSortablePage:
        @pytest.mark.parametrize('locator1, locator2', [(SortablePageLocators.LIST, SortablePageLocators.LIST_ITEMS),
                                                        (SortablePageLocators.GRID, SortablePageLocators.GRID_ITEMS)])
        def test_sortable_list_grid(self, driver, locator1, locator2):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            sortable_page.change_order(locator1, locator2)

    class TestSelectablePage:
        @pytest.mark.parametrize('locator1, locator2, locator3', [(SelectablePageLocators.LIST,
                                                                   SelectablePageLocators.LIST_ITEMS,
                                                                   SelectablePageLocators.SELECTED_LIST_ITEMS),
                                                                  (SelectablePageLocators.GRID,
                                                                  SelectablePageLocators.GRID_ITEMS,
                                                                  SelectablePageLocators.SELECTED_GRID_ITEMS)])
        def test_selectable(self, driver, locator1, locator2, locator3):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            selectable_page.select_elements(locator1, locator2, locator3)

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()

    class TestDroppablePage:

        def test_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()

    class TestDragabblePage:

        def test_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()


