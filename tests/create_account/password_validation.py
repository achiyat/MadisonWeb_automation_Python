# password_validation.py
import allure
from pages.common import Note, Message, TitlePage
from pages.create_account_page import CreateAccount
from pages.home_page import Home
from pages.login_page import Login
from tests.base_test import BaseTest


@allure.epic('User Authentication')
@allure.feature('Account Creation')
@allure.story('Password Validation')
class TestPasswordValidation(BaseTest):

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

    @allure.title('Password Validation')
    @allure.description('Verify validation message when entering a short password.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_password_validation(self):
        allure.attach(
            'This test verifies the validation message when entering a short password.',
            'Test Description'
        )
        with allure.step("Fill in account information with a short password"):
            self.create_account_page.fill_info("f_name", "l_name", "email@gmail.com",
                                               "123", "123")

        with allure.step("Verify validation note for short password"):
            assert self.create_account_page.get_note(Note.PASSWORD_VALIDATION) == Message.VALIDATION_NOTE
