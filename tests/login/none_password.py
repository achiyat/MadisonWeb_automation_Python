# none_password.py
import allure
from pages.common import Message, Note
from pages.home_page import Home
from pages.login_page import Login
from tests.base_test import BaseTest


@allure.epic('User Authentication')
@allure.feature('login Functionality')
@allure.story('User login')
class TestNonePassword(BaseTest):
    def setup(self):
        self.home_page = Home(self.driver)
        self.login_page = Login(self.driver)

    @allure.title('Test with None Password')
    @allure.description('Verify error message when trying to login with no password.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_none_password(self):
        allure.attach(
            'This test verifies the error message when trying to login with no password.',
            'Test Description'
        )
        with allure.step("Click on the 'My Account' link"):
            self.home_page.click_account()
            self.home_page.click_my_account()

        with allure.step("Fill login info with empty password"):
            self.login_page.fill_info("usertest99@gmail.com", "")

        with allure.step("Verify error message and Attach screenshot"):
            assert self.login_page.get_note(Note.PASSWORD) == Message.REQUIRED_FIELD
