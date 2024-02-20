# checking_required_fields.py
import allure
from pages.common import Note, Message, TitlePage
from pages.create_account_page import CreateAccount
from pages.home_page import Home
from pages.login_page import Login
from tests.base_test import BaseTest


@allure.epic('User Registration')
@allure.feature('Create Account Functionality')
@allure.story('Checking Required Fields')
class TestCheckingRequiredFields(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.login_page = Login(self.driver)
        self.create_account_page = CreateAccount(self.driver)

    @allure.title('Navigation to Create Account Page')
    @allure.description('Verify navigation to the create account page from the My Account section.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_create_account_page(self):
        allure.attach(
            'This test verifies the navigation to the create account page from the My Account section.',
            'Test Description'
        )
        with allure.step("Navigate to the create account page"):
            self.home_page.click_account()
            self.home_page.click_my_account()
            self.login_page.click_create_account()

        with allure.step("Verify the title of the create account page"):
            assert self.create_account_page.get_title() == TitlePage.CREATE_ACCOUNT

    @allure.title('Checking Required Fields')
    @allure.description('Verify error messages for required fields on the create account page.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checking_required_fields(self):
        allure.attach(
            'This test verifies error messages for required fields on the create account page.',
            'Test Description'
        )
        with allure.step("Submit the form without filling in required fields"):
            self.create_account_page.click_register()

        with allure.step("Verify error messages for each required field"):
            assert self.create_account_page.get_note(Note.FIRST_NAME) == Message.REQUIRED_FIELD
            assert self.create_account_page.get_note(Note.LAST_NAME) == Message.REQUIRED_FIELD
            assert self.create_account_page.get_note(Note.EMAIL) == Message.REQUIRED_FIELD
            assert self.create_account_page.get_note(Note.PASSWORD) == Message.REQUIRED_FIELD
            assert self.create_account_page.get_note(Note.CONFIRM_PASSWORD) == Message.REQUIRED_FIELD
            self.screenshot()
