# base_page.py
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from typing import Union, List


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.action = ActionChains(driver)

    def wait_for_element(self, locator) -> Union[WebElement]:
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def wait_for_elements(self, locator) -> Union[List[WebElement]]:
        try:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    def fill_text(self, locator: tuple[By, str], txt: str) -> None:
        self.wait_for_element(locator).clear()
        self.wait_for_element(locator).send_keys(txt)

    def click(self, locator: tuple[By, str]) -> None:
        self.wait_for_element(locator).click()

    def fill_text_with_element(self, parent_locator: tuple[By, str], locator: tuple[By, str], txt: str) -> None:
        element = self.wait_for_element(parent_locator)
        element.find_element(*locator).clear()
        element.find_element(*locator).send_keys(txt)

    def click_with_element(self, parent_locator: tuple[By, str], locator: tuple[By, str]) -> None:
        element = self.wait_for_element(parent_locator)
        element.find_element(*locator).click()

    def get_text(self, locator: tuple[By, str]) -> str:
        return self.wait_for_element(locator).text

    def get_list(self, locator: tuple[By, str]) -> list:
        return self.wait_for_elements(locator)

    def get_count_of_elements(self, locator: tuple[By, str]) -> int:
        return len(self.wait_for_elements(locator))

    def print_text(self, locator: tuple[By, str]) -> None:
        print(self.wait_for_element(locator).text)

    def select_option_by_value(self, locator: tuple[By, str], value: str) -> None:
        Select(self.wait_for_element(locator)).select_by_value(value)

    def select_option_by_text(self, locator: tuple[By, str], text: str) -> None:
        Select(self.wait_for_element(locator)).select_by_visible_text(text)

    def select_option_by_index(self, locator: tuple[By, str], index: int) -> None:
        Select(self.wait_for_element(locator)).select_by_index(index)

    def checkbox_is_selected(self, locator: tuple[By, str]) -> bool | None:
        element = self.wait_for_elements(locator)
        if len(element) == 0:
            return False
        elif len(element) == 1:
            return True
        else:
            return None

    @staticmethod
    def get_date_dot(date: tuple) -> str:
        day, month, year = date
        return f"{day}.{month}.{year}"

    @staticmethod
    def get_date_slash(date: tuple) -> str:
        day, month, year = date
        return f"{day}/{month}/{year}"

    @staticmethod
    def get_date_dash(date: tuple) -> str:
        day, month, year = date
        return f"{day}-{month}-{year}"

    def hover_element(self, locator: tuple[By, str]) -> None:
        element = self.wait_for_element(locator)
        self.action.move_to_element(element).perform()
