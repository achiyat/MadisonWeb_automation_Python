# validation_note.py
import allure
from pages.common import Message, Note
from pages.home_page import Home
from pages.login_page import Login
from tests.base_test import BaseTest


@allure.epic('User Authentication')
@allure.feature('login Functionality')
@allure.story('User login')
class TestValidationLogin(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.login_page = Login(self.driver)

    @allure.title('Test Validation Note')
    @allure.description('Verify validation note when entering a short password.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_validation_note(self):
        allure.attach(
            'This test verifies the validation note when entering a short password.',
            'Test Description'
        )
        with allure.step("Click on the 'My Account' link"):
            self.home_page.click_account()
            self.home_page.click_my_account()

        with allure.step("Fill login info with a short password"):
            self.login_page.fill_info("usertest99@gmail.com", "123")

        with allure.step("Verify validation note and Attach screenshot"):
            assert self.login_page.get_note(Note.PASSWORD_VALIDATION) == Message.VALIDATION_NOTE
