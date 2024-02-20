# correct_email.py
import allure
from pages.common import MessageType, TitlePage
from pages.forgot_password_page import ForgotPassword
from pages.home_page import Home
from pages.login_page import Login
from tests.base_test import BaseTest


@allure.epic('User Authentication')
@allure.feature('Forgot Password Functionality')
@allure.story('Forgot Password')
class TestCorrectEmail(BaseTest):

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

    @allure.title('Test Correct Email')
    @allure.description('Verify success message when submitting with a correct email.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_correct_email(self):
        allure.attach(
            'This test verifies the success message when submitting with a correct email.',
            'Test Description'
        )
        with allure.step("Fill valid email and submit"):
            user_email = "usertest123@gmail.com"
            self.forgot_page.fill_info(user_email)

        with allure.step("Verify success message and Attach screenshot"):
            assert self.login_page.get_message(MessageType.SUCCESS) == self.login_page.get_success_message(user_email)
