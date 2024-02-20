# remove_item.py
import allure
from pages.cart_page import Cart
from pages.common import MensCollection, Items, Color, Size
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('cart Management')
@allure.story('Remove item')
class TestRemoveItem(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)
        self.cart_page = Cart(self.driver)

    @allure.title('Add Items to cart')
    @allure.description('Add multiple items to the cart for removal.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_items_to_cart(self):
        allure.attach(
            'This test adds multiple items to the cart for removal.',
            'Test Description'
        )
        with allure.step("Add first item to cart"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)
            self.item_page.select_color(Color.CHARCOAL)
            self.item_page.select_size(Size.XL)
            self.item_page.click_add_to_cart()

        with allure.step("Add a second item to cart"):
            self.home_page.select_mens_collection(MensCollection.BLAZERS)
            self.products_page.select_item(Items.STRETCH_COTTON_BLAZER)
            self.item_page.select_color(Color.BLUE)
            self.item_page.select_size(Size.S)
            self.item_page.click_add_to_cart()

        with allure.step("Add a third item to cart"):
            self.home_page.select_mens_collection(MensCollection.TEES_KNITS_POLOS)
            self.products_page.select_item(Items.CORE_STRIPED_SPORT_SHIRT)
            self.item_page.select_color(Color.INDIGO)
            self.item_page.select_size(Size.XS)
            self.item_page.click_add_to_cart()

    @allure.title('Remove item from cart')
    @allure.description('Remove an item from the cart and verify the updated number of items.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_item_from_cart(self):
        allure.attach(
            'This test removes an item from the cart and verifies the updated number of items.',
            'Test Description'
        )
        with allure.step("Remove an item from the cart"):
            self.cart_page.click_remove(Items.STRETCH_COTTON_BLAZER)

        with allure.step("Verify the updated number of items in the cart"):
            assert self.cart_page.get_number_of_items_in_the_cart() == 2
