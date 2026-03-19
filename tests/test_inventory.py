import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture(autouse=True)
def login_user(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    yield
    driver.delete_all_cookies()


class TestInventory:

    def test_six_products_displayed(self, driver):
        inventory = InventoryPage(driver)
        assert inventory.is_loaded()
        assert inventory.get_item_count() == 6, "Should display 6 products"

    def test_add_first_item_to_cart(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(index=0)

        assert inventory.get_cart_count() == 1

    def test_add_two_items_to_cart(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(index=0)
        inventory.add_item_to_cart(index=1)

        assert inventory.get_cart_count() == 2

    def test_cart_navigation(self, driver):
        inventory = InventoryPage(driver)
        inventory.go_to_cart()

        assert "cart.html" in driver.current_url
