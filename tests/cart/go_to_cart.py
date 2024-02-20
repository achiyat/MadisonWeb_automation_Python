# go_to_cart.py
import allure
from pages.cart_page import Cart
from pages.common import MensCollection, Items, Color, Size, TitlePage
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('cart Management')
@allure.story('Navigating to cart')
class TestGoToCart(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)
        self.cart_page = Cart(self.driver)

    @allure.title('Go to cart')
    @allure.description('Verify navigation to the cart after adding an item.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_cart(self):
        allure.attach(
            'This test verifies the navigation to the cart after adding an item.',
            'Test Description'
        )
        with allure.step("Navigate to the collection and select a specific item"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)

        with allure.step("Select color and size, and add the item to the cart"):
            self.item_page.select_color(Color.CHARCOAL)
            self.item_page.select_size(Size.XL)
            self.item_page.click_add_to_cart()

        with allure.step("Verify the title of the cart page"):
            assert self.cart_page.get_title() == TitlePage.CART
