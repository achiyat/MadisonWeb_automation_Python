# review_required_fields.py
import allure
from pages.common import MensCollection, Items, Note, Message
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Review Functionality')
@allure.story('Review - Required Fields')
class TestReviewRequiredFields(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)

    @allure.title('Submit Review Without Required Fields')
    @allure.description(
        'Verify error messages for required fields when submitting a review without filling in mandatory information.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_review_required_fields(self):
        allure.attach(
            'This test verifies error messages for required fields when submitting a review.',
            'Test Description'
        )
        with allure.step(
                "Navigate to the shirts collection, select an item, and submit review without filling required fields"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)
            self.item_page.click_review_tab()
            self.item_page.click_review_link()
            self.item_page.click_submit_review()

        with allure.step("Verify error messages for each required field"):
            assert self.item_page.get_note(Note.RATING) == Message.RATING
            assert self.item_page.get_note(Note.REVIEW) == Message.REQUIRED_FIELD.upper()
            assert self.item_page.get_note(Note.SUMMARY) == Message.REQUIRED_FIELD.upper()
            assert self.item_page.get_note(Note.NICKNAME) == Message.REQUIRED_FIELD.upper()
            self.screenshot()
