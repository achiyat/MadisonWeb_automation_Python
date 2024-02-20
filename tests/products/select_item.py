# select_item.py
import allure
from pages.common import MensCollection, TitleCollection, Items
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Product Selection')
@allure.story('Selecting Items')
class TestSelectItem(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)

    @allure.title('Navigation to Blazers Collection')
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

    @allure.title('Choosing an item from the Blazers Collection')
    @allure.description('Verify selection of an item from the blazers collection.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_select_item_from_blazers(self):
        allure.attach(
            'This test verifies the selection of an item from the blazers collection.',
            'Test Description'
        )
        with allure.step("Choose an item from the blazers collection"):
            self.products_page.select_item(Items.STRETCH_COTTON_BLAZER)

        with allure.step("Verify the title of the selected item"):
            assert self.item_page.get_title() == Items.STRETCH_COTTON_BLAZER.upper()
