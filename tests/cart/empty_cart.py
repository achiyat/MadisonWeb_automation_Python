# empty_cart.py
import allure
from pages.cart_page import Cart
from pages.common import MensCollection, Items, Color, Size, Message
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('cart Management')
@allure.story('Empty cart')
class TestEmptyCart(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)
        self.cart_page = Cart(self.driver)

    @allure.title('Empty cart')
    @allure.description('Verify emptying the cart removes all items.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_cart(self):
        allure.attach(
            'This test verifies that emptying the cart removes all items.',
            'Test Description'
        )
        with allure.step("Navigate to the blazers collection and add an item to the cart"):
            self.home_page.select_mens_collection(MensCollection.BLAZERS)
            self.products_page.select_item(Items.STRETCH_COTTON_BLAZER)
            self.item_page.select_color(Color.BLUE)
            self.item_page.select_size(Size.S)
            self.item_page.fill_qty_item("2")
            self.cart_page.click_empty_cart()

        with allure.step("Verify the empty cart message"):
            assert self.cart_page.get_empty_message() == Message.EMPTY_CART
