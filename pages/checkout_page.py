# checkout_page.py
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Checkout(BasePage):
    TITLE_TXT: tuple = (By.CSS_SELECTOR, ".page-title>h1")
    GUEST_CHECKBOX: tuple = (By.CSS_SELECTOR, 'input[value="guest"]')
    REGISTER_CHECKBOX: tuple = (By.CSS_SELECTOR, 'input[value="register"]')
    CONTINUE_BTN: tuple = (By.CSS_SELECTOR, "#onepage-guest-register-button")
    EMAIL_FIELD: tuple = (By.CSS_SELECTOR, "#login-email")
    PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "#login-password")
    LOGIN_BTN: tuple = (By.CSS_SELECTOR, "div.col-2 button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get the title of the Checkout page")
    def get_title(self) -> str:
        return self.get_text(self.TITLE_TXT)

    @allure.step("Click on 'checkout' checkbox and 'Continue' Button")
    def click_guest(self) -> None:
        self.click(self.GUEST_CHECKBOX)
        self.click(self.CONTINUE_BTN)

    @allure.step("Click on 'register' checkbox and 'Continue' Button")
    def click_register(self) -> None:
        self.click(self.REGISTER_CHECKBOX)
        self.click(self.CONTINUE_BTN)

    @allure.step("Fill login information with email: {email}, password: {password}")
    def fill_info(self, email: str, password: str) -> None:
        self.fill_text(self.EMAIL_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)
