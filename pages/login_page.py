from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com"

    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str = None):
        self.driver.get(url or self.URL)

    def login(self, username: str, password: str):
        username_el = self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT))
        username_el.clear()
        username_el.send_keys(username)
        password_el = self.wait.until(EC.visibility_of_element_located(self._PASSWORD_INPUT))
        password_el.clear()
        password_el.send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()

    def get_error_message(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MESSAGE)
        ).text

    def is_error_visible(self) -> bool:
        try:
            return self.driver.find_element(*self._ERROR_MESSAGE).is_displayed()
        except Exception:
            return False
