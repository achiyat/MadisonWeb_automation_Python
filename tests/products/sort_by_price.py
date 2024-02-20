# sort_by_price.py
import allure
from pages.common import MensCollection, TitleCollection, SortBy
from pages.home_page import Home
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Sorting Functionality')
@allure.story('Sort by Price')
class TestSortByPrice(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)

    @allure.title('Go to Blazers Collection')
    @allure.description('Verify navigation to the blazers collection.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_blazers_collection(self):
        allure.attach(
            'This test verifies navigation to the blazers collection.',
            'Test Description'
        )
        with allure.step("Navigate to the blazers collection"):
            self.home_page.select_mens_collection(MensCollection.BLAZERS)

        with allure.step("Verify the title of the blazers collection"):
            assert self.products_page.get_title() == TitleCollection.BLAZERS

    @allure.title('Sort products by Price')
    @allure.description('Verify sorting products by price.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sort_products(self):
        allure.attach(
            'This test verifies sorting products by price.',
            'Test Description'
        )
        with allure.step("Get the list of item names and prices before sorting"):
            list1 = self.products_page.get_item_names_and_prices()

        with allure.step("Sort the products by price"):
            self.products_page.sort_products(SortBy.PRICE)

        with allure.step("Get the list of item names and prices after sorting"):
            list2 = self.products_page.get_item_names_and_prices()

        with allure.step("Verify the products are sorted"):
            print(f"{list1}\n!=\n{list2}")
            assert list1 != list2
