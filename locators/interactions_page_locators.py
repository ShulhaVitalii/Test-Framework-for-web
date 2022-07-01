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
    BOX_WITH_RESTRICTION = (By.ID, 'resizableBoxWithRestriction')
    BOX_WITHOUT_RESTRICTION = (By.ID, 'resizable')
    BOX_WITH_RESTRICTION_HANDLE = (By.XPATH, '//span[@class="react-resizable-handle react-resizable-handle-se"][1]')
    BOX_WITHOUT_RESTRICTION_HANDLE = (By.XPATH, '//div[@id="resizable"]//span[@class="react-resizable-handle'
                                                ' react-resizable-handle-se"]')


class DroppablePageLocators:
    pass


class DragabblePageLocators:
    pass

