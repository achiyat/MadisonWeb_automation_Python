# products_page.py
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Color, Items, SortBy
from typing import Type
import allure


class Products(BasePage):
    TITLE_TXT: tuple = (By.CSS_SELECTOR, ".page-title>h1")
    ITEM_PRODUCT: tuple = (By.CSS_SELECTOR, ".category-products li.item")
    NAME_TXT: tuple = (By.CSS_SELECTOR, ".product-info>h2.product-name>a")
    PRICE_TXT: tuple = (By.CSS_SELECTOR, ".price-box>.regular-price")
    SORT_BY_DROPDOWN: tuple = (By.CSS_SELECTOR, '.sorter select')
    ARROW: tuple = (By.CSS_SELECTOR, ".sort-by-switcher")
    LIST_VIEW: tuple = (By.CSS_SELECTOR, "a.list")
    GRID_VIEW: tuple = (By.CSS_SELECTOR, "strong.grid")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get 'products' page title")
    def get_title(self) -> str:
        return self.get_text(self.TITLE_TXT)

    @allure.step("Click on the 'Arrow' button")
    def click_arrow(self) -> None:
        self.click(self.ARROW)

    @allure.step("Click on the '{item}' item")
    def select_item(self, item: Type[Items]) -> None:
        self.click((By.CSS_SELECTOR, f'img[alt="{item}"]'))

    @allure.step("Click on the '{color}' item")
    def select_color(self, color: Type[Color]) -> None:
        self.click((By.CSS_SELECTOR, f'img[alt="{color}"]'))

    @allure.step("Counting items")
    def count_items(self) -> int:
        return self.get_count_of_elements(self.ITEM_PRODUCT)

    @allure.step("Getting item names and prices")
    def get_item_names_and_prices(self) -> str:
        items = self.get_list(self.ITEM_PRODUCT)

        item_info = []
        for item in items:
            name = item.find_element(*self.NAME_TXT).text
            price = item.find_element(*self.PRICE_TXT).text
            item_info.append(f"{name}({price})")

        return ",".join(item_info)

    @allure.step("Sorting products by {sort_by}")
    def sort_products(self, sort_by: Type[SortBy]) -> None:
        match sort_by:
            case SortBy.POSITION:
                self.select_option_by_text(self.SORT_BY_DROPDOWN, SortBy.POSITION)
            case SortBy.PRICE:
                self.select_option_by_text(self.SORT_BY_DROPDOWN, SortBy.PRICE)
            case SortBy.NAME:
                self.select_option_by_text(self.SORT_BY_DROPDOWN, SortBy.NAME)
            case _:
                raise ValueError("Invalid sort option provided")
