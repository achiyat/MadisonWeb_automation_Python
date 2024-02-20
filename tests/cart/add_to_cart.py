# add_to_cart.py
import allure
from pages.cart_page import Cart
from pages.common import MensCollection, Items, Color, Size
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('cart Management')
@allure.story('Adding Items to cart')
class TestAddToCart(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)
        self.cart_page = Cart(self.driver)

    @allure.title('Add item to cart')
    @allure.description('Verify adding an item to the cart.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart(self):
        allure.attach(
            'This test verifies the process of adding an item to the cart.',
            'Test Description'
        )
        with allure.step("Navigate to the collection and select a specific item"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)

        with allure.step("Select color and size, and add the item to the cart"):
            self.item_page.select_color(Color.CHARCOAL)
            self.item_page.select_size(Size.XL)
            self.item_page.click_add_to_cart()

        with allure.step("Verify the success message"):
            assert self.cart_page.get_cart_message() == self.cart_page.get_add_to_cart_msg(Items.PLAID_COTTON_SHIRT)
