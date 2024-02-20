# cart_page.py
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Items, Message
from typing import Type


class Cart(BasePage):
    TITLE_TXT: tuple = (By.CSS_SELECTOR, ".page-title>h1")
    MSG_TXT: tuple = (By.CSS_SELECTOR, "ul.messages span")
    COUNT_INT: tuple = (By.CSS_SELECTOR, "#shopping-cart-table>tbody>tr")
    EMPTY_CART_BTN: tuple = (By.CSS_SELECTOR, "#empty_cart_button")
    CHECKOUT_BTN: tuple = (By.CSS_SELECTOR, ".cart-totals button")
    REMOVE_BTN: tuple = (By.CSS_SELECTOR, ".product-cart-remove a")
    QTY_FIELD: tuple = (By.CSS_SELECTOR, ".product-cart-actions>input")
    UPDATE_BTN: tuple = (By.CSS_SELECTOR, ".product-cart-actions>button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get cart title")
    def get_title(self) -> str:
        return self.get_text(self.TITLE_TXT)

    @allure.step("Get 'Empty' message")
    def get_empty_message(self) -> str:
        return self.get_text(self.TITLE_TXT)

    @allure.step("Get message from 'cart' page")
    def get_cart_message(self) -> str:
        return self.get_text(self.MSG_TXT)

    @allure.step("Get 'Add to cart' Message")
    def get_add_to_cart_msg(self, item: Type[Items]) -> str:
        return Message.ADD_TO_CART.replace("*item*", item)

    @allure.step("Get number of items in the cart")
    def get_number_of_items_in_the_cart(self) -> int:
        return self.get_count_of_elements(self.COUNT_INT)

    @allure.step("Click on 'Empty cart' button")
    def click_empty_cart(self) -> None:
        self.click(self.EMPTY_CART_BTN)

    @allure.step("Click on 'Proceed to Checkout' button")
    def click_checkout(self) -> None:
        self.click(self.CHECKOUT_BTN)

    @allure.step("fill quantity for item in the cart")
    def fill_qty_item(self, item: Type[Items], qty: str) -> None:
        locator = (By.XPATH, f"//tr[.//a[contains(@title, '{item}')]]")
        self.fill_text_with_element(locator, self.QTY_FIELD, qty)
        self.click_with_element(locator, self.UPDATE_BTN)

    @allure.step("Click on 'Remove' button")
    def click_remove(self, item: Type[Items]) -> None:
        locator = (By.XPATH, f"//tr[.//a[contains(@title, '{item}')]]")
        self.click_with_element(locator, self.REMOVE_BTN)
