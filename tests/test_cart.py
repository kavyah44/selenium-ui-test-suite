import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


@pytest.fixture(autouse=True)
def login(driver):
    """Log in before each test in this module."""
    LoginPage(driver).open().login(VALID_USER, VALID_PASS)
    return HomePage(driver)


class TestCart:
    """Test cases for shopping cart functionality."""

    def test_add_item_to_cart(self, driver, login):
        """Test that adding an item updates the cart badge."""
        home = login
        home.add_first_item_to_cart()
        assert home.get_cart_count() == "1"

    def test_cart_count_increments(self, driver, login):
        """Test cart badge count increases with each item added."""
        home = login
        buttons = driver.find_elements("css selector", "[data-test^='add-to-cart']")
        buttons[0].click()
        buttons[1].click()
        assert home.get_cart_count() == "2"

    def test_page_has_products(self, driver, login):
        """Test that the inventory page displays products."""
        home = login
        assert home.get_product_count() == 6

    def test_page_title_is_products(self, driver, login):
        """Test that the page title is 'Products'."""
        home = login
        assert home.get_page_title() == "Products"

    def test_navigate_to_cart(self, driver, login):
        """Test that clicking cart icon navigates to cart page."""
        home = login
        home.go_to_cart()
        assert "cart" in driver.current_url
