# review.py
import allure
from pages.common import MensCollection, Items, Review, Message
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Review Functionality')
@allure.story('Review Submission')
class TestReview(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)

    @allure.title('Submit Review')
    @allure.description('Verify successful submission of a review for a product.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_review(self):
        allure.attach(
            'This test verifies successful submission of a review for a product.',
            'Test Description'
        )
        with allure.step("Navigate to the shirts collection and select an item"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)

        with allure.step("Navigate to the review tab and click on the review link"):
            self.item_page.click_review_tab()
            self.item_page.click_review_link()

        with allure.step("Fill out the review form with ratings and comments"):
            self.item_page.fill_rating(Review._5, Review._5, Review._5)
            self.item_page.fill_review("good shirt", "I liked it", "user99")

        with allure.step("Verify the success message after submitting the review"):
            assert self.item_page.get_message() == Message.REVIEW
            self.screenshot()
