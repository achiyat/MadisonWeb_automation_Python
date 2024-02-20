# test_main.py
import pytest

from tests.forgot_password.correct_email import TestCorrectEmail
from tests.forgot_password.none_email import TestNoneEmail
from tests.create_account.checking_required_fields import TestCheckingRequiredFields
from tests.create_account.confirm_pass_validation import TestConfirmValidation
from tests.create_account.password_validation import TestPasswordValidation
from tests.cart.add_to_cart import TestAddToCart
from tests.cart.checkout import TestCheckout
from tests.cart.edit_qty import TestEditQty
from tests.cart.empty_cart import TestEmptyCart
from tests.cart.go_to_cart import TestGoToCart
from tests.cart.remove_item import TestRemoveItem
from tests.item.count_of_review import TestCountOfReview
from tests.item.qty_limit import TestQtyLimit
from tests.item.review import TestReview
from tests.item.review_required_fields import TestReviewRequiredFields
from tests.item.stock import TestStock
from tests.login.login_test import TestLogin
from tests.login.none_password import TestNonePassword
from tests.login.none_username import TestNoneUserName
from tests.login.validation_alert import TestValidationLogin
from tests.products.arrow_sort import TestArrowSort
from tests.products.count_items import TestCountItems
from tests.products.fill_search import TestFillSearch
from tests.products.select_color import TestSelectColor
from tests.products.select_item import TestSelectItem
from tests.products.sort_by_price import TestSortByPrice

# Define a dictionary to map folder names to their test classes
test_classes = {
    "cart": [TestAddToCart, TestCheckout, TestEditQty, TestEmptyCart, TestGoToCart, TestRemoveItem],
    "create_account": [TestCheckingRequiredFields, TestConfirmValidation, TestPasswordValidation],
    "forgot_password": [TestCorrectEmail, TestNoneEmail],
    "item": [TestCountOfReview, TestQtyLimit, TestReview, TestReviewRequiredFields, TestStock],
    "login": [TestLogin, TestNonePassword, TestNoneUserName, TestValidationLogin],
    "products": [TestArrowSort, TestCountItems, TestFillSearch, TestSelectColor, TestSelectItem, TestSortByPrice]
}


@pytest.mark.parametrize("test_classes_list", test_classes.values())
def run_tests(test_classes_list):
    for test_class in test_classes_list:
        for method_name in dir(test_class):
            if method_name.startswith("test_"):
                method = getattr(test_class(), method_name)
                method()


if __name__ == '__main__':
    pytest.main()
