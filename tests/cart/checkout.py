# checkout.py
import allure
from pages.billing_page import Billing
from pages.cart_page import Cart
from pages.checkout_page import Checkout
from pages.common import MensCollection, Items, Color, Size, TitlePage, BillingInfo, Message
from pages.home_page import Home
from pages.item_page import Item
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Checkout Process')
@allure.story('Navigating to Checkout and Filling Checkout Information')
class TestCheckout(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)
        self.item_page = Item(self.driver)
        self.cart_page = Cart(self.driver)
        self.checkout_page = Checkout(self.driver)
        self.billing_page = Billing(self.driver)

    @allure.title('Go to Checkout')
    @allure.description('Navigate to checkout after adding an item to the cart.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_checkout(self):
        allure.attach(
            'This test navigates to checkout after adding an item to the cart.',
            'Test Description'
        )
        with allure.step("Add an item to the cart and proceed to checkout"):
            self.home_page.select_mens_collection(MensCollection.SHIRTS)
            self.products_page.select_item(Items.PLAID_COTTON_SHIRT)
            self.item_page.select_color(Color.CHARCOAL)
            self.item_page.select_size(Size.XL)
            self.item_page.click_add_to_cart()
            self.cart_page.click_checkout()

        with allure.step("Verify the title of the checkout page"):
            assert self.checkout_page.get_title() == TitlePage.CHECKOUT

    @allure.title('Fill Checkout Information')
    @allure.description('Fill out billing information during the checkout process.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_fill_checkout_information(self):
        allure.attach(
            'This test fills out billing information during the checkout process.',
            'Test Description'
        )
        with allure.step("Select guest checkout and fill out billing information"):
            self.checkout_page.click_guest()
            self.billing_page.fill_info(BillingInfo)

        with allure.step("Verify the loading message after filling out the information"):
            assert self.billing_page.get_wait_text() == Message.LOADING
            self.screenshot()
