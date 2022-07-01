from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST = (By.ID, 'demo-tab-list')
    GRID = (By.ID, 'demo-tab-grid')
    LIST_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-list"]//div[@class="list-group-item list-group-item-action"]')
    GRID_ITEMS = (By.XPATH, '//div[@id="demo-tabpane-grid"]//div[@class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    pass


class ResizablePageLocators:
    pass


class DroppablePageLocators:
    pass


class DragabblePageLocators:
    pass

