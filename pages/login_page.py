# login_page.py
from typing import Type
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from pages.common import Note, MessageType, Message


class Login(BasePage):
    TITLE_TXT: tuple = (By.CSS_SELECTOR, ".page-title>h1")
    ERROR_MSG_TXT: tuple = (By.CSS_SELECTOR, ".error-msg span")
    SUCCESS_MSG_TXT: tuple = (By.CSS_SELECTOR, ".success-msg>ul>li>span")
    WELCOME_MSG_TXT: tuple = (By.CSS_SELECTOR, "p.hello")
    EMAIL_FIELD: tuple = (By.CSS_SELECTOR, "#email")
    PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "#pass")
    EMAIL_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-email")
    PASSWORD_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-pass")
    VALIDATION_NOTE: tuple = (By.CSS_SELECTOR, "#advice-validate-password-pass")
    FORGOT_PASSWORD_LINK: tuple = (By.CSS_SELECTOR, "li>a.f-left")
    CREATE_ACCOUNT_BTN: tuple = (By.CSS_SELECTOR, ".buttons-set>a")
    LOGIN_BTN: tuple = (By.CSS_SELECTOR, "#send2")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get login title")
    def get_title(self) -> str:
        return self.get_text(self.TITLE_TXT)

    @allure.step("Fill login information with email: {email}, password: {password}")
    def fill_info(self, email: str, password: str) -> None:
        self.fill_text(self.EMAIL_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)

    @allure.step("Click 'login' Button")
    def click_login(self) -> None:
        self.click(self.LOGIN_BTN)

    @allure.step("Click 'Forgot Password' Link")
    def click_forgot_password(self) -> None:
        self.click(self.FORGOT_PASSWORD_LINK)

    @allure.step("Click 'Create Account' Button")
    def click_create_account(self) -> None:
        self.click(self.CREATE_ACCOUNT_BTN)

    @allure.step("Get Success Message")
    def get_success_message(self, email: str) -> str:
        return Message.SUCCESS.replace("@gmail", email)

    @allure.step("Get {message_type} Message")
    def get_message(self, message_type: Type[MessageType]) -> str:
        match message_type:
            case MessageType.ERROR:
                return self.get_text(self.ERROR_MSG_TXT)
            case MessageType.SUCCESS:
                return self.get_text(self.SUCCESS_MSG_TXT)
            case MessageType.WELCOME:
                return self.get_text(self.WELCOME_MSG_TXT)
            case _:
                raise ValueError(f"Unsupported message type: {message_type}")

    @allure.step("Get {note_type} Required field Note")
    def get_note(self, note_type: Type[Note]) -> str:
        match note_type:
            case Note.EMAIL:
                return self.get_text(self.EMAIL_NOTE)
            case Note.PASSWORD:
                return self.get_text(self.PASSWORD_NOTE)
            case Note.PASSWORD_VALIDATION:
                return self.get_text(self.VALIDATION_NOTE)
            case _:
                raise ValueError(f"Unsupported note type: {note_type}")
