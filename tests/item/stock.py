# stock.py
import allure
from pages.common import MensCollection, Items, Stock, Color, Size
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Stock Management')
@allure.story('item Stock Status')
class TestStock(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)

    @allure.title('Select item from Shirts Collection')
    @allure.description('Verify selection of an item from the shirts collection.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_select_item(self):
        allure.attach(
            'This test verifies the selection of an item from the shirts collection.',
            'Test Description'
        )
        with allure.step("Navigate to the shirts collection"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)

        with allure.step("Select a specific shirt item"):
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)
            assert self.item_page.get_title() == Items.PLAID_COTTON_SHIRT.upper()

    @allure.title('Verify Out of Stock Status')
    @allure.description('Check if the selected item is marked as out of stock when the variant is unavailable.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_out_of_stock(self):
        allure.attach(
            'This test verifies if the selected item is marked as out of stock when the variant is unavailable.',
            'Test Description'
        )
        with allure.step("Select a color and size for the item that is out of stock"):
            self.item_page.select_color(Color.CHARCOAL)
            self.item_page.select_size(Size.S)

        with allure.step("Verify item status"):
            assert self.item_page.get_stock() == Stock.OUT_OF_STOCK

    @allure.title('Verify In Stock Status')
    @allure.description('Check if the selected item is marked as in stock when the variant is available.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_in_stock(self):
        allure.attach(
            'This test verifies if the selected item is marked as in stock when the variant is available.',
            'Test Description'
        )
        with allure.step("Select a color and size for the item that is in stock"):
            self.item_page.select_color(Color.RED)
            self.item_page.select_size(Size.M)

        with allure.step("Verify item status"):
            assert self.item_page.get_stock() == Stock.IN_STOCK
