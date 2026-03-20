import pytest
from pages.inventory_page import InventoryPage


class TestInventory:

    def test_six_products_displayed(self, driver, login_user):
        inventory = InventoryPage(driver)
        assert inventory.is_loaded()
        assert inventory.get_item_count() == 6, "Should display 6 products"

    def test_add_first_item_to_cart(self, driver, login_user):
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(index=0)

        assert inventory.get_cart_count() == 1

    def test_add_two_items_to_cart(self, driver, login_user):
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(index=0)
        inventory.add_item_to_cart(index=1)

        assert inventory.get_cart_count() == 2

    def test_cart_navigation(self, driver, login_user):
        inventory = InventoryPage(driver)
        inventory.go_to_cart()

        assert "cart.html" in driver.current_url
