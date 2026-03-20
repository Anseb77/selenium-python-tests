from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    _INVENTORY_CONTAINER = (By.ID, "inventory_container")
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self) -> bool:
        return self.wait.until(
            EC.visibility_of_element_located(self._INVENTORY_CONTAINER)
        ).is_displayed()

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(*self._INVENTORY_ITEMS))

    def add_item_to_cart(self, index: int = 0):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self._ADD_TO_CART_BUTTONS)
        )
        if index >= len(buttons):
            raise IndexError(f"No add-to-cart button at index {index}; found {len(buttons)}")
        buttons[index].click()

    def get_cart_count(self) -> int:
        try:
            return int(self.driver.find_element(*self._CART_BADGE).text)
        except Exception:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self._CART_LINK).click()
