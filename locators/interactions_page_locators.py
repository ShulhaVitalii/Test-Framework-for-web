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
    # Simple tab
    TAB_SIMPLE = (By.ID, 'droppableExample-tab-simple')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #draggable')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')
    DROP_HERE_TEXT = (By.XPATH, '//div[@id="droppable"]/p')

    # Accept tab
    ACCEPTABLE = (By.ID, 'acceptable')
    TAB_ACCEPT = (By.ID, 'droppableExample-tab-accept')
    NON_ACCEPTABLE = (By.ID, 'notAcceptable')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#droppableExample-tabpane-accept #droppable')
    DROP_HERE_ACCEPT_TEXT = (By.CSS_SELECTOR, '#droppableExample-tabpane-accept #droppable p')

    # Prevent Propogation
    PP = (By.ID, 'droppableExample-tab-preventPropogation')
    PP_TEXT_LIST = (By.CSS_SELECTOR, '#droppableExample-tabpane-preventPropogation p')
    PP_DRAG_ME = (By.CSS_SELECTOR, '#droppableExample-tabpane-preventPropogation #dragBox')
    PP_NOT_GREEDY_INNER = (By.CSS_SELECTOR, '#droppableExample-tabpane-preventPropogation #notGreedyInnerDropBox')
    PP_GREEDY_INNER = (By.CSS_SELECTOR, '#droppableExample-tabpane-preventPropogation #greedyDropBoxInner')
    PP_GREEDY = (By.CSS_SELECTOR, '#greedyDropBox p')

    # Revert Draggable
    RD = (By.ID, 'droppableExample-tab-revertable')
    RD_WILL_REVERT = (By.ID, 'revertable')
    RD_NOT_REVERT = (By.ID, 'notRevertable')
    RD_DROP_HERE = (By.CSS_SELECTOR, '#revertableDropContainer #droppable p')

class DragabblePageLocators:
    SIMPLE_TAB = (By.XPATH, '//a[@id="draggableExample-tab-simple"]')
    AXIS_RESTRICTED_TAB = (By.ID, 'draggableExample-tab-axisRestriction')
    CONTAINER_RESTRICTED_TAB = (By.ID, 'draggableExample-tab-containerRestriction')
    CURSOR_STYLE_TAB = (By.ID, 'draggableExample-tab-cursorStyle')

    # Simple
    DRAG_ME = (By.ID, 'dragBox')

    # Axis Restricted
    ONLY_X = (By.ID, 'restrictedX')
    ONLY_Y = (By.ID, 'restrictedY')

