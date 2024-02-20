# none_email.py
import allure
from pages.common import Message, TitlePage
from pages.forgot_password_page import ForgotPassword
from pages.home_page import Home
from pages.login_page import Login
from tests.base_test import BaseTest


@allure.epic('User Authentication')
@allure.feature('Forgot Password Functionality')
@allure.story('Forgot Password')
class TestNoneEmail(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.login_page = Login(self.driver)
        self.forgot_page = ForgotPassword(self.driver)

    @allure.title('Test Go to Forgot Password Page')
    @allure.description('Verify navigation to the Forgot Password page.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_forgot_password_page(self):
        allure.attach(
            'This test verifies navigation to the Forgot Password page.',
            'Test Description'
        )
        with allure.step("Click on the 'My Account' link"):
            self.home_page.click_account()
            self.home_page.click_my_account()

        with allure.step("Click on the 'Forgot your password?' link"):
            self.login_page.click_forgot_password()

        with allure.step("Verify the title of the Forgot Password page"):
            assert self.forgot_page.get_title() == TitlePage.FORGOT

    @allure.title('Test with None Email')
    @allure.description('Verify error message when trying to submit with no email.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_none_email(self):
        allure.attach(
            'This test verifies the error message when trying to submit with no email.',
            'Test Description'
        )
        with allure.step("Submit form with empty email"):
            self.forgot_page.fill_info("")

        with allure.step("Verify error message and Attach screenshot"):
            assert self.forgot_page.get_email_alert() == Message.REQUIRED_FIELD
