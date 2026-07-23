import pytest
from playwright.sync_api import Page

from e2e_tests.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    """Fixture providing a clean LoginPage instance per test execution."""
    return LoginPage(page)
