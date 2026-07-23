import pytest
from playwright.sync_api import Page, expect

from e2e_tests.config.settings import settings
from e2e_tests.pages.login_page import LoginPage

VALID_EMAIL = "user@test.com"
VALID_PASSWORD = "password"


def test_successful_login_redirects_to_dashboard(login_page: LoginPage, page: Page):
    # Arrange
    login_page.open()

    # Act
    login_page.submit_credentials(VALID_EMAIL, VALID_PASSWORD)

    # Assert
    expect(page).to_have_url(f"{settings.BASE_URL}/dashboard")
    expect(login_page.welcome_message).to_be_visible()


def test_login_with_invalid_credentials_stays_on_login(login_page: LoginPage, page: Page):
    # Arrange
    login_page.open()

    # Act
    login_page.submit_credentials("invalid@test.com", "wrongpassword")

    # Assert
    expect(page).to_have_url(f"{settings.BASE_URL}/login")
    expect(login_page.submit_button).to_be_visible()
    expect(login_page.welcome_message).to_have_count(0)
