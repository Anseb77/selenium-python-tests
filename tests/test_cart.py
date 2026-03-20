import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:

    def test_cart_is_empty_on_login(self, driver, login_user, base_url):
        cart = CartPage(driver)
        driver.get(f"{base_url}/cart.html")

        assert cart.get_item_count() == 0

    def test_added_item_appears_in_cart(self, driver, login_user):
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(index=0)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.get_item_count() == 1
        assert len(cart.get_item_names()) == 1

    def test_remove_item_from_cart(self, driver, login_user):
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(index=0)
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.remove_item(index=0)

        assert cart.get_item_count() == 0

    def test_continue_shopping_redirects(self, driver, login_user, base_url):
        driver.get(f"{base_url}/cart.html")
        cart = CartPage(driver)
        cart.continue_shopping()

        assert "inventory" in driver.current_url
