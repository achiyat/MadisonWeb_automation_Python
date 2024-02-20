# qty_limit.py
import allure
from pages.common import MensCollection, Items, Color, Size
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Product Quantity')
@allure.story('Quantity Limit')
class TestQtyLimit(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)

    @allure.title('Verify Quantity Limit')
    @allure.description('Verify that the quantity limit of a product is enforced.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_qty_limit(self):
        allure.attach(
            'This test verifies that the quantity limit of a product is enforced.',
            'Test Description'
        )
        with allure.step("Navigate to the shirts collection and select an item"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)

        with allure.step("Select color and size, and set the quantity to 5"):
            self.item_page.select_color(Color.CHARCOAL)
            self.item_page.select_size(Size.XL)
            self.item_page.fill_qty_item("5")

        with allure.step("Verify the message stating if the quantity is available"):
            assert self.item_page.get_message() == self.item_page.get_available_msg(Items.PLAID_COTTON_SHIRT)
