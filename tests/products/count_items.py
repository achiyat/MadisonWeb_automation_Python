# count_items.py
import allure
from pages.common import MensCollection, TitleCollection
from pages.home_page import Home
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Product Counting')
@allure.story('Counting Items')
class TestCountItems(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)

    @allure.title('Navigation to Shirts Collection')
    @allure.description('Verify navigation to the shirts collection.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_shirts_collection(self):
        allure.attach(
            'This test verifies navigation to the shirts collection.',
            'Test Description'
        )
        with allure.step("Navigate to the shirts collection"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)

        with allure.step("Verify the title of the shirts collection"):
            assert self.products_page.get_title() == TitleCollection.SHIRTS

    @allure.title('Counting Items')
    @allure.description('Verify the count of items in the collection.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_count_items(self):
        allure.attach(
            'This test verifies the count of items in the collection.',
            'Test Description'
        )
        with allure.step("Count the items in the collection"):
            assert self.products_page.count_items() == 2
