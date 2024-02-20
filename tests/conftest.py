# conftest.py
import pytest
import allure
from tests.base_test import BaseTest


@pytest.fixture(scope="class")
def setup(request):
    base_test = BaseTest()
    base_test.setup_class()
    yield base_test
    base_test.teardown_class()


def pytest_exception_interact(report):
    if report.failed:
        allure.attach(
            body=BaseTest.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
