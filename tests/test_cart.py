import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture(autouse=True)
def login_user(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    yield
    driver.delete_all_cookies()


class TestCart:

    def test_cart_is_empty_on_login(self, driver):
        cart = CartPage(driver)
        driver.get("https://www.saucedemo.com/cart.html")

        assert cart.get_item_count() == 0

    def test_added_item_appears_in_cart(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(index=0)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.get_item_count() == 1

    def test_remove_item_from_cart(self, driver):
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart(index=0)
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.remove_item(index=0)

        assert cart.get_item_count() == 0

    def test_continue_shopping_redirects(self, driver):
        driver.get("https://www.saucedemo.com/cart.html")
        cart = CartPage(driver)
        cart.continue_shopping()

        assert "inventory" in driver.current_url
