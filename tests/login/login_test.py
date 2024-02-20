# login_test.py
import allure
from pages.common import Message, MessageType
from pages.home_page import Home
from pages.login_page import Login
from tests.base_test import BaseTest


@allure.epic('User Authentication')
@allure.feature('login Functionality')
@allure.story('User login')
class TestLogin(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.login_page = Login(self.driver)

    @allure.title('Test Successful login')
    @allure.description('Verify successful login and welcome message.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self):
        allure.attach(
            'This test verifies successful login and welcome message.',
            'Test Description'
        )
        with allure.step("Click on the 'My Account' link"):
            self.home_page.click_account()
            self.home_page.click_my_account()

        with allure.step("Fill valid login info"):
            self.login_page.fill_info("usertest99@gmail.com", "123456")

        with allure.step("Verify welcome message and Attach screenshot"):
            assert self.login_page.get_message(MessageType.WELCOME) == Message.WELCOME
