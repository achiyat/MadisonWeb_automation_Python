# create_account_page.py
from typing import Type
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from pages.common import Note


class CreateAccount(BasePage):
    PAGE_TITLE: tuple = (By.CSS_SELECTOR, ".page-title h1")
    ERROR_MESSAGE: tuple = (By.CSS_SELECTOR, ".error-msg span")
    FIRST_NAME_FIELD: tuple = (By.CSS_SELECTOR, "#firstname")
    MIDDLE_NAME_FIELD: tuple = (By.CSS_SELECTOR, "#middlename")
    LAST_NAME_FIELD: tuple = (By.CSS_SELECTOR, "#lastname")
    EMAIL_FIELD: tuple = (By.CSS_SELECTOR, "#email_address")
    PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "#password")
    CONFIRM_PASSWORD_FIELD: tuple = (By.CSS_SELECTOR, "#confirmation")
    NEWSLETTER_CHECKBOX: tuple = (By.CSS_SELECTOR, "#is_subscribed")
    BACK_LINK: tuple = (By.CSS_SELECTOR, ".back-link a")
    REGISTER_BTN: tuple = (By.CSS_SELECTOR, ".buttons-set button")

    FIRST_NAME_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-firstname")
    LAST_NAME_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-lastname")
    EMAIL_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-email_address")
    PASSWORD_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-password")
    CONFIRM_PASSWORD_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-confirmation")
    VALIDATION_NOTE: tuple = (By.CSS_SELECTOR, "#advice-validate-password-password")
    CONFIRM_NOTE: tuple = (By.CSS_SELECTOR, "#advice-validate-cpassword-confirmation")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get create account page title")
    def get_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    @allure.step("Fill information with first name: {first_name}, last name: {last_name}, "
                 "email: {email}, password: {password}, confirm password: {confirm_password}")
    def fill_info(self, first_name: str, last_name: str, email: str, password: str, confirm_password: str) -> None:
        self.fill_text(self.FIRST_NAME_FIELD, first_name)
        self.fill_text(self.LAST_NAME_FIELD, last_name)
        self.fill_text(self.EMAIL_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.fill_text(self.CONFIRM_PASSWORD_FIELD, confirm_password)
        self.click(self.REGISTER_BTN)

    @allure.step("Click 'Register' Button")
    def click_register(self) -> None:
        self.click(self.REGISTER_BTN)

    @allure.step("Click 'Back' link")
    def click_back(self) -> None:
        self.click(self.BACK_LINK)

    @allure.step("Click 'Newsletter' checkbox")
    def click_newsletter(self) -> None:
        self.click(self.NEWSLETTER_CHECKBOX)

    @allure.step("Get error message")
    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    @allure.step("Get note message based on type: {note_type}")
    def get_note(self, note_type: Type[Note]) -> str:
        match note_type:
            case Note.FIRST_NAME:
                return self.get_text(self.FIRST_NAME_NOTE)
            case Note.LAST_NAME:
                return self.get_text(self.LAST_NAME_NOTE)
            case Note.EMAIL:
                return self.get_text(self.EMAIL_NOTE)
            case Note.PASSWORD:
                return self.get_text(self.PASSWORD_NOTE)
            case Note.CONFIRM_PASSWORD:
                return self.get_text(self.CONFIRM_PASSWORD_NOTE)
            case Note.PASSWORD_VALIDATION:
                return self.get_text(self.VALIDATION_NOTE)
            case Note.CONFIRM_VALIDATION:
                return self.get_text(self.CONFIRM_NOTE)
            case _:
                raise ValueError(f"Unsupported note type: {note_type}")
