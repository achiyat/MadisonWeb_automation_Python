# count_of_review.py
import allure
from pages.common import MensCollection, Items, WomensCollection
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Review Functionality')
@allure.story('Count of Reviews')
class TestCountOfReview(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)

    @allure.title('Counting the amount of reviews for a specific item')
    @allure.description('Verify the amount of reviews on the item')
    @allure.severity(allure.severity_level.NORMAL)
    def test_count(self):
        allure.attach(
            'This test verifies the amount of reviews on the item.',
            'Test Description'
        )
        with allure.step("Navigate to women's dresses and select a specific dress"):
            self.home_page.select_womens_collection(WomensCollection.DRESSES_SKIRTS)
            self.products_page.select_item(Items.LUDLOW_SHEATH_DRESS)

        with allure.step("Click on the review tab and check the amount of reviews"):
            self.item_page.click_review_tab()
            assert self.item_page.get_count_of_review() == 2

    @allure.title('Counting the amount of reviews for a specific item')
    @allure.description('Verify the amount of reviews on the item.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_none_count(self):
        allure.attach(
            'This test verifies the amount of reviews on the item.',
            'Test Description'
        )
        with allure.step("Navigate to men's shirts and select a specific shirt"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)

        with allure.step("Click on the review tab and check the amount of reviews"):
            self.item_page.click_review_tab()
            assert self.item_page.get_count_of_review() == 0
