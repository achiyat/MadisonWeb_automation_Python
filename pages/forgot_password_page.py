# forgot_password_page.py
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ForgotPassword(BasePage):
    TITLE_TXT: tuple = (By.CSS_SELECTOR, ".page-title>h1")
    EMAIL_FIELD: tuple = (By.CSS_SELECTOR, "#email_address")
    EMAIL_ALERT: tuple = (By.CSS_SELECTOR, "#advice-required-entry-email_address")
    BACK_LINK: tuple = (By.CSS_SELECTOR, ".back-link>a")
    SUBMIT_BTN: tuple = (By.CSS_SELECTOR, ".buttons-set>button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get forgot password page title")
    def get_title(self) -> str:
        return self.get_text(self.TITLE_TXT)

    @allure.step("Fill email address for password reset: {email}")
    def fill_info(self, email: str) -> None:
        self.fill_text(self.EMAIL_FIELD, email)
        self.click(self.SUBMIT_BTN)

    @allure.step("Click 'Submit' Button for password reset")
    def click_submit(self) -> None:
        self.click(self.SUBMIT_BTN)

    @allure.step("Click 'Back to login' link")
    def click_back_to_login(self) -> None:
        self.click(self.BACK_LINK)

    @allure.step("Get email address required field Alert")
    def get_email_alert(self) -> str:
        return self.get_text(self.EMAIL_ALERT)
