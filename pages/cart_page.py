from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _REMOVE_BUTTONS = (By.CSS_SELECTOR, "[data-test^='remove']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(*self._CART_ITEMS))

    def get_item_names(self) -> list[str]:
        return [el.text for el in self.driver.find_elements(*self._ITEM_NAMES)]

    def remove_item(self, index: int = 0):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self._REMOVE_BUTTONS)
        )
        if index >= len(buttons):
            raise IndexError(f"No remove button at index {index}; found {len(buttons)}")
        buttons[index].click()

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BUTTON)).click()

    def continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self._CONTINUE_SHOPPING)).click()
