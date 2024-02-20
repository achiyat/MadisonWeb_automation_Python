# billing_page.py
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Billing(BasePage):
    FIRST_NAME_FIELD: tuple = (By.CSS_SELECTOR, 'input[name="billing[firstname]"]')
    LAST_NAME_FIELD: tuple = (By.CSS_SELECTOR, 'input[name="billing[lastname]"]')
    EMAIL_FIELD: tuple = (By.CSS_SELECTOR, 'input[name="billing[email]"]')
    STREET_ADDRESS_FIELD: tuple = (By.CSS_SELECTOR, 'input[id="billing:street1"]')
    CITY_FIELD: tuple = (By.CSS_SELECTOR, 'input[name="billing[city]"]')
    STATE_PROVINCE_SELECT: tuple = (By.CSS_SELECTOR, 'select[name="billing[region_id]"]')
    ZIP_POSTAL_CODE_FIELD: tuple = (By.CSS_SELECTOR, 'input[name="billing[postcode]"]')
    COUNTRY_SELECT: tuple = (By.CSS_SELECTOR, 'select[name="billing[country_id]"]')
    TELEPHONE_FIELD: tuple = (By.CSS_SELECTOR, 'input[name="billing[telephone]"]')
    USE_SAME_ADDRESS_YES_RADIO: tuple = (By.CSS_SELECTOR, 'input[id="billing:use_for_shipping_yes"]')
    USE_SAME_ADDRESS_NO_RADIO: tuple = (By.CSS_SELECTOR, 'input[id="billing:use_for_shipping_no"]')
    CONTINUE_BTN: tuple = (By.CSS_SELECTOR, "#billing-buttons-container button")
    WAIT_TXT: tuple = (By.CSS_SELECTOR, "#billing-please-wait")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Get 'Loading next step...' text")
    def get_wait_text(self) -> str:
        self.click(self.CONTINUE_BTN)
        return self.get_text(self.WAIT_TXT)

    @allure.step("Fill Billing Information")
    def fill_info(self, billing_info: dict) -> None:
        self.fill_text(self.FIRST_NAME_FIELD, billing_info["first_name"])
        self.fill_text(self.LAST_NAME_FIELD, billing_info["last_name"])
        self.fill_text(self.EMAIL_FIELD, billing_info["email"])
        self.fill_text(self.STREET_ADDRESS_FIELD, billing_info["street_address"])
        self.fill_text(self.CITY_FIELD, billing_info["city"])
        self.select_option_by_text(self.STATE_PROVINCE_SELECT, billing_info["state_province"])
        self.fill_text(self.ZIP_POSTAL_CODE_FIELD, billing_info["zip_postal_code"])
        self.select_option_by_text(self.COUNTRY_SELECT, billing_info["country"])
        self.fill_text(self.TELEPHONE_FIELD, billing_info["telephone"])
        self.click(self.USE_SAME_ADDRESS_YES_RADIO)
        self.click(self.CONTINUE_BTN)
