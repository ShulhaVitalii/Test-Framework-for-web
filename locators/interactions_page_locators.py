from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST = (By.ID, 'demo-tab-list')
    GRID = (By.ID, 'demo-tab-grid')
    LIST_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-list"]//div[@class="list-group-item list-group-item-action"]')
    GRID_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-grid"]//div[@class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    LIST = (By.ID, 'demo-tab-list')
    GRID = (By.ID, 'demo-tab-grid')
    LIST_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-list"]//li[@class="mt-2 list-group-item list-group-item-action"]')
    GRID_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-grid"]//li[@class="list-group-item list-group-item-action"]')
    SELECTED_GRID_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-grid"]//li[@class="list-group-item active '
                                     'list-group-item-action"]')
    SELECTED_LIST_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-list"]//li[@class="mt-2 list-group-item active'
                                     ' list-group-item-action"]')

class ResizablePageLocators:
    pass


class DroppablePageLocators:
    pass


class DragabblePageLocators:
    pass

