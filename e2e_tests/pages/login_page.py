from playwright.sync_api import Locator, Page

from e2e_tests.config.settings import settings
from e2e_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the Application Login screen."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Resilient locators prioritizing accessibility roles and explicit IDs
        self.email_input: Locator = page.locator("#email")
        self.password_input: Locator = page.locator("#password")
        self.submit_button: Locator = page.get_by_role("button", name="Login")

        # Dashboard and message feedback elements
        self.welcome_message: Locator = page.locator(".welcome")
        self.flash_message: Locator = page.locator("#flash")

    def open(self) -> None:
        self.navigate_to(f"{settings.BASE_URL}/login")

    def submit_credentials(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
