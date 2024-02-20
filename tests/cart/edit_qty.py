# edit_qty.py
import allure
from pages.cart_page import Cart
from pages.common import MensCollection, Items, Color, Size
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('cart Management')
@allure.story('Edit Quantity')
class TestEditQty(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)
        self.cart_page = Cart(self.driver)

    @allure.title('Add item and Verify Quantity')
    @allure.description('Verify adding an item to the cart and checking the quantity.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_item(self):
        allure.attach(
            'This test verifies adding an item to the cart and checking the quantity.',
            'Test Description'
        )
        with allure.step("Navigate to the blazers collection and add an item to the cart"):
            self.home_page.select_mens_collection(MensCollection.BLAZERS)
            self.products_page.select_item(Items.STRETCH_COTTON_BLAZER)
            self.item_page.select_color(Color.BLUE)
            self.item_page.select_size(Size.S)
            self.item_page.fill_qty_item("2")

        with allure.step("Verify the quantity of items in the cart"):
            assert self.home_page.get_number_of_items_in_the_cart() == 2

    @allure.title('Edit Quantity of item in cart')
    @allure.description('Verify editing the quantity of an item in the cart.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_qty_in_cart(self):
        allure.attach(
            'This test verifies editing the quantity of an item in the cart.',
            'Test Description'
        )
        with allure.step("Edit the quantity of an item in the cart"):
            self.cart_page.fill_qty_item(Items.STRETCH_COTTON_BLAZER, "1")

        with allure.step("Verify the updated quantity of items in the cart"):
            assert self.home_page.get_number_of_items_in_the_cart() == 1
