# base_test.py
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BaseTest:

    driver: WebDriver

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://demo-store.seleniumacademy.com/")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def screenshot(self):
        return allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
