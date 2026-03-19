import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:

    def test_successful_login(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        assert inventory.is_loaded(), "Inventory page should be visible after login"

    def test_invalid_credentials(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("invalid_user", "wrong_password")

        assert login.is_error_visible()
        assert "Username and password do not match" in login.get_error_message()

    def test_empty_username(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("", "secret_sauce")

        assert "Username is required" in login.get_error_message()

    def test_empty_password(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "")

        assert "Password is required" in login.get_error_message()

    def test_locked_out_user(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("locked_out_user", "secret_sauce")

        assert "locked out" in login.get_error_message().lower()
