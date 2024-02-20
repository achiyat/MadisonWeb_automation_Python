# common.py


class Note:
    FIRST_NAME = "First Name"
    LAST_NAME = "Last Name"
    EMAIL = "Email"
    PASSWORD = "Password"
    CONFIRM_PASSWORD = "Confirm Password"
    PASSWORD_VALIDATION = "Password validation"
    CONFIRM_VALIDATION = "Confirm Password validation"
    RATING = "Rating"
    REVIEW = "Review"
    SUMMARY = "Summary"
    NICKNAME = "Nickname"


class MessageType:
    ERROR = "Error"
    SUCCESS = "Success"
    WELCOME = "Welcome"


class Message:
    REQUIRED_FIELD = "This is a required field."
    SELECT = "Please select an option."
    VALIDATION_NOTE = "Please enter 6 or more characters. Leading or trailing spaces will be ignored."
    CONFIRM_NOTE = "Please make sure your passwords match."
    NOT_FOUND = "Invalid login or password."
    WELCOME = "Hello, F_user L_user!"
    RATING = "Please select one of each of the ratings above"
    REVIEW = "Your review has been accepted for moderation."
    AVAILABLE = 'The requested quantity for "*item*" is not available.'
    ADD_TO_CART = "*item* was added to your shopping cart."
    LOADING = "Loading next step..."
    EMPTY_CART = "SHOPPING CART IS EMPTY"
    SUCCESS = ("If there is an account associated with @gmail you will "
               "receive an email with a link to reset your password.")


class TitlePage:
    CREATE_ACCOUNT = "CREATE AN ACCOUNT"
    LOGIN = "LOGIN OR CREATE AN ACCOUNT"
    FORGOT = "FORGOT YOUR PASSWORD?"
    CART = "SHOPPING CART"
    CHECKOUT = "CHECKOUT"


class TitleCollection:
    SHIRTS = "SHIRTS"
    TEES_KNITS_POLOS = "TEES, KNITS AND POLOS"
    PANTS_DENIM = "PANTS & DENIM"
    BLAZERS = "BLAZERS"
    TOPS_BLOUSES = "TOPS & BLOUSES"
    DRESSES_SKIRTS = "DRESSES & SKIRTS"


class MensCollection:
    SHIRTS = "Shirts"
    TEES_KNITS_POLOS = "Tees, Knits and Polos"
    PANTS_DENIM = "Pants & Denim"
    BLAZERS = "Blazers"


class WomensCollection:
    TOPS_BLOUSES = "Tops & Blouses"
    PANTS_DENIM = "Pants & Denim"
    DRESSES_SKIRTS = "Dresses & Skirts"


class Color:
    CHARCOAL = "Charcoal"
    RED = "Red"
    WHITE = "White"
    KHAKI = "Khaki"
    ROYAL_BLUE = "Royal Blue"
    BLACK = "Black"
    BLUE = "Blue"
    INDIGO = "Indigo"


class Size:
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"


class Stock:
    IN_STOCK = "IN STOCK"
    OUT_OF_STOCK = "OUT OF STOCK"


class Items:
    PLAID_COTTON_SHIRT = "Plaid Cotton Shirt"
    CORE_STRIPED_SPORT_SHIRT = "Core Striped Sport Shirt"
    STRETCH_COTTON_BLAZER = "Stretch Cotton Blazer"
    LUDLOW_SHEATH_DRESS = "Ludlow Sheath Dress"
    PANT_FOR_MEN = "Pant for Men"


class SortBy:
    POSITION = "Position"
    NAME = "Name"
    PRICE = "Price"


class RequiredField:
    RATING = "rating"
    REVIEW = "review"
    SUMMARY = "summary"
    NICKNAME = "nickname"


class Review:
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"


BillingInfo = {
    "first_name": "User",
    "last_name": "User1",
    "email": "User@example.com",
    "street_address": "123 Main St",
    "city": "New York City",
    "state_province": "New York",
    "zip_postal_code": "10001",
    "country": "United States",
    "telephone": "+44 1234 05678"
}
