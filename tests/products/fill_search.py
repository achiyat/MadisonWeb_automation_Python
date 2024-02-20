# fill_search.py
import allure
from pages.common import Items
from pages.home_page import Home
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Search Functionality')
@allure.story('Filling Search')
class TestFillSearch(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)

    @allure.title('Fill Search')
    @allure.description('Verify filling the search field with a specific item.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_fill_search(self):
        allure.attach(
            f'This test verifies filling the search field with the item "{Items.PANT_FOR_MEN}".',
            'Test Description'
        )
        with allure.step("Fill the search field"):
            self.home_page.fill_search(Items.PANT_FOR_MEN)

        with allure.step("Verify the title of the search results page"):
            assert self.products_page.get_title() == f"SEARCH RESULTS FOR '{Items.PANT_FOR_MEN.upper()}'"
