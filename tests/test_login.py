import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

BASE_URL = "https://www.saucedemo.com"
VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


class TestLogin:
    """Test cases for the login functionality."""

    def test_valid_login(self, driver):
        """Test that a valid user can log in successfully."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, VALID_PASS)

        home_page = HomePage(driver)
        assert "inventory" in driver.current_url
        assert home_page.get_page_title() == "Products"

    def test_invalid_password(self, driver):
        """Test that an incorrect password shows an error message."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, "wrong_password")

        assert login_page.is_error_displayed()
        assert "Username and password do not match" in login_page.get_error_message()

    def test_empty_username(self, driver):
        """Test that submitting with no username shows an error."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", VALID_PASS)

        assert login_page.is_error_displayed()
        assert "Username is required" in login_page.get_error_message()

    def test_empty_password(self, driver):
        """Test that submitting with no password shows an error."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, "")

        assert login_page.is_error_displayed()
        assert "Password is required" in login_page.get_error_message()

    def test_locked_out_user(self, driver):
        """Test that a locked-out user sees the correct error."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", VALID_PASS)

        assert login_page.is_error_displayed()
        assert "locked out" in login_page.get_error_message()

    def test_logout(self, driver):
        """Test that a logged-in user can log out successfully."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, VALID_PASS)

        home_page = HomePage(driver)
        home_page.logout()

        assert driver.current_url == BASE_URL + "/"
