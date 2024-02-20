# item_page.py
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Color, Size, Review, Note, Message, Items
from typing import Type
import allure


class Item(BasePage):
    TITLE_TXT: tuple = (By.CSS_SELECTOR, ".product-name>span")
    PRICE_INT: tuple = (By.CSS_SELECTOR, ".price-info span.price")
    STOCK: tuple = (By.CSS_SELECTOR, ".availability>.value")
    DESCRIPTION: tuple = (By.CSS_SELECTOR, ".short-description>.std")
    ADD_TO_CART_BTN: tuple = (By.CSS_SELECTOR, ".add-to-cart-buttons>button")
    QTY_FIELD: tuple = (By.CSS_SELECTOR, "#qty")
    WISHLIST_LINK: tuple = (By.CSS_SELECTOR, "a.link-wishlist")
    COMPARE_LINK: tuple = (By.CSS_SELECTOR, "a.link-compare")

    # review
    REVIEW_TAB: tuple = (By.CSS_SELECTOR, ".toggle-tabs>li.last")
    REVIEW_LINK: tuple = (By.CSS_SELECTOR, "#customer-reviews a")
    COUNT_REVIEW: tuple = (By.CSS_SELECTOR, "#customer-reviews dd")
    MSG_TXT: tuple = (By.CSS_SELECTOR, "ul.messages span")

    RATING_NOTE: tuple = (By.CSS_SELECTOR, "#advice-validate-rating-validate_rating")
    REVIEW_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-review_field")
    SUMMARY_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-summary_field")
    NICKNAME_NOTE: tuple = (By.CSS_SELECTOR, "#advice-required-entry-nickname_field")

    REVIEW_FIELD: tuple = (By.CSS_SELECTOR, "#review_field")
    SUMMARY_FIELD: tuple = (By.CSS_SELECTOR, "#summary_field")
    NICKNAME_FIELD: tuple = (By.CSS_SELECTOR, "#nickname_field")
    SUBMIT_REVIEW_BTN: tuple = (By.CSS_SELECTOR, "#review-form button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get item title")
    def get_title(self) -> str:
        return self.get_text(self.TITLE_TXT)

    @allure.step("Get message from 'item' page")
    def get_message(self) -> str:
        return self.get_text(self.MSG_TXT)

    @allure.step("Get available Message")
    def get_available_msg(self, item: Type[Items]) -> str:
        return Message.AVAILABLE.replace("*item*", item)

    @allure.step("Click 'Add to cart' Button")
    def click_add_to_cart(self) -> None:
        self.click(self.ADD_TO_CART_BTN)

    @allure.step("Get item price")
    def get_price(self) -> str:
        return self.get_text(self.PRICE_INT)

    @allure.step("Get status Stock")
    def get_stock(self) -> str:
        return self.get_text(self.STOCK)

    @allure.step("Get item description")
    def get_description(self) -> str:
        return self.get_text(self.DESCRIPTION)

    @allure.step("Click on the '{color}' item")
    def select_color(self, color: Type[Color]) -> None:
        self.click((By.CSS_SELECTOR, f'img[alt="{color}"]'))

    @allure.step("Click on the '{size}' item")
    def select_size(self, size: Type[Size]) -> None:
        self.click((By.CSS_SELECTOR, f'a[title="{size}"]'))

    @allure.step("Click on the 'Wishlist' Link")
    def click_wishlist(self) -> None:
        self.click(self.WISHLIST_LINK)

    @allure.step("Click on the 'Compare' Link")
    def click_compare(self) -> None:
        self.click(self.COMPARE_LINK)

    @allure.step("Click on the 'Review' Tab")
    def click_review_tab(self) -> None:
        self.click(self.REVIEW_TAB)

    @allure.step("Click on the 'Review' Link")
    def click_review_link(self) -> None:
        self.click(self.REVIEW_LINK)

    @allure.step("Click 'Submit Review' Button")
    def click_submit_review(self) -> None:
        self.click(self.SUBMIT_REVIEW_BTN)

    @allure.step("Filling rating: quality={quality}, value={value}, price={price}")
    def fill_rating(self, quality: Type[Review], value: Type[Review], price: Type[Review]) -> None:
        self.click((By.CSS_SELECTOR, f'#Quality_{quality}'))
        self.click((By.CSS_SELECTOR, f'#Value_{value}'))
        self.click((By.CSS_SELECTOR, f'#Price_{price}'))

    @allure.step("Filling review with text: {review_text}, summary: {summary}, and nickname: {nickname}")
    def fill_review(self, review_text: str, summary: str, nickname: str) -> None:
        self.fill_text(self.REVIEW_FIELD, review_text)
        self.fill_text(self.SUMMARY_FIELD, summary)
        self.fill_text(self.NICKNAME_FIELD, nickname)
        self.click(self.SUBMIT_REVIEW_BTN)

    @allure.step("Get {note_type} Required field Note")
    def get_note(self, note_type: Type[Note]) -> str:
        match note_type:
            case Note.RATING:
                return self.get_text(self.RATING_NOTE)
            case Note.REVIEW:
                return self.get_text(self.REVIEW_NOTE)
            case Note.SUMMARY:
                return self.get_text(self.SUMMARY_NOTE)
            case Note.NICKNAME:
                return self.get_text(self.NICKNAME_NOTE)
            case _:
                raise ValueError(f"Unsupported note type: {note_type}")

    @allure.step("Getting count of reviews")
    def get_count_of_review(self) -> int:
        return self.get_count_of_elements(self.COUNT_REVIEW)

    @allure.step("Filling quantity field with: {qty}")
    def fill_qty_item(self, qty: str) -> None:
        self.fill_text(self.QTY_FIELD, qty)
        self.click(self.ADD_TO_CART_BTN)
