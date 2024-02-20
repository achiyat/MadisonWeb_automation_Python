# home_page.py
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import MensCollection, WomensCollection, Items
from typing import Type
import allure


class Home(BasePage):
    ACCOUNT_BTN: tuple = (By.CSS_SELECTOR, ".skip-account")
    CART_BTN: tuple = (By.CSS_SELECTOR, ".skip-cart")
    COUNT_CART_INT: tuple = (By.CSS_SELECTOR, "#header span.count")
    MY_ACCOUNT_BTN: tuple = (By.CSS_SELECTOR, '#header-account a[title="My Account"]')
    SEARCH_INPUT: tuple = (By.CSS_SELECTOR, "#search")
    SEARCH_AUTOCOMPLETE: tuple = (By.CSS_SELECTOR, "#search_autocomplete")
    SEARCH_BTN: tuple = (By.CSS_SELECTOR, ".search-button")

    MEN_LINK: tuple = (By.CSS_SELECTOR, "#nav li.nav-2")
    SHIRTS_LINK: tuple = (By.CSS_SELECTOR, "#nav ul>li.nav-2-2")
    TEES_KNITS_POLOS_LINK: tuple = (By.CSS_SELECTOR, "#nav ul>li.nav-2-3")
    MEN_PANTS_DENIM_LINK: tuple = (By.CSS_SELECTOR, "#nav ul>li.nav-2-4")
    BLAZERS_LINK: tuple = (By.CSS_SELECTOR, "#nav ul>li.nav-2-5")

    WOMEN_LINK: tuple = (By.CSS_SELECTOR, "#nav li.nav-1")
    TOPS_BLOUSES_LINK: tuple = (By.CSS_SELECTOR, "#nav ul>li.nav-1-2")
    WOMEN_PANTS_DENIM_LINK: tuple = (By.CSS_SELECTOR, "#nav ul>li.nav-1-3")
    DRESSES_SKIRTS_LINK: tuple = (By.CSS_SELECTOR, "#nav ul>li.nav-1-4")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get number of items in the cart")
    def get_number_of_items_in_the_cart(self) -> int:
        return int(self.get_text(self.COUNT_CART_INT))

    @allure.step("Click on the 'Account' button")
    def click_account(self) -> None:
        self.click(self.ACCOUNT_BTN)

    @allure.step("Fill search input with text: {text}")
    def fill_search(self, text: Type[Items]) -> None:
        self.fill_text(self.SEARCH_INPUT, str(text))
        self.click(self.SEARCH_BTN)

    @allure.step("Click on the 'cart' button")
    def click_cart(self) -> None:
        self.click(self.CART_BTN)

    @allure.step("Click on the 'My Account' button")
    def click_my_account(self) -> None:
        self.click(self.MY_ACCOUNT_BTN)

    @allure.step("Click on the 'Men' Link")
    def click_men_category(self) -> None:
        self.click(self.MEN_LINK)

    @allure.step("Click on the 'Women' Link")
    def click_women_category(self) -> None:
        self.click(self.WOMEN_LINK)

    @allure.step("Click on the '{collection}' Link")
    def select_mens_collection(self, collection: Type[MensCollection]) -> None:
        self.hover_element(self.MEN_LINK)
        match collection:
            case MensCollection.SHIRTS:
                self.click(self.SHIRTS_LINK)
            case MensCollection.TEES_KNITS_POLOS:
                self.click(self.TEES_KNITS_POLOS_LINK)
            case MensCollection.PANTS_DENIM:
                self.click(self.MEN_PANTS_DENIM_LINK)
            case MensCollection.BLAZERS:
                self.click(self.BLAZERS_LINK)
            case _:
                raise ValueError("Invalid collection name.")

    @allure.step("Click on the '{collection}' Link")
    def select_womens_collection(self, collection: Type[MensCollection]) -> None:
        self.hover_element(self.WOMEN_LINK)
        match collection:
            case WomensCollection.TOPS_BLOUSES:
                self.click(self.TOPS_BLOUSES_LINK)
            case WomensCollection.PANTS_DENIM:
                self.click(self.WOMEN_PANTS_DENIM_LINK)
            case WomensCollection.DRESSES_SKIRTS:
                self.click(self.DRESSES_SKIRTS_LINK)
            case _:
                raise ValueError("Invalid collection name.")
