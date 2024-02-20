# select_color.py
import allure
from pages.common import MensCollection, TitleCollection, Color
from pages.home_page import Home
from pages.products_page import Products
from tests.base_test import BaseTest


@allure.epic('User Shopping')
@allure.feature('Product Selection')
@allure.story('Selecting Colors')
class TestSelectColor(BaseTest):

    def setup(self):
        self.home_page = Home(self.driver)
        self.products_page = Products(self.driver)

    @allure.title('Navigation to Denim Pants Collection')
    @allure.description('Verify navigation to the denim pants collection.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_denim_pants_collection(self):
        allure.attach(
            'This test verifies navigation to the denim pants collection.',
            'Test Description'
        )
        with allure.step("Navigate to the denim pants collection"):
            self.home_page.select_mens_collection(MensCollection.PANTS_DENIM)

        with allure.step("Verify the title of the denim pants collection"):
            assert self.products_page.get_title() == TitleCollection.PANTS_DENIM

    @allure.title('Selecting Color')
    @allure.description('Verify the selection of a specific color from the collection.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_select_color(self):
        allure.attach(
            'This test verifies the selection of a specific color from the collection.',
            'Test Description'
        )
        with allure.step("Count the items before selecting a color"):
            assert self.products_page.count_items() == 4

        with allure.step("Select a specific color"):
            self.products_page.select_color(Color.CHARCOAL)

        with allure.step("Verify the count of items after selecting the color"):
            assert self.products_page.count_items() == 2
