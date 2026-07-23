from playwright.sync_api import Locator, Page


class BasePage:
    """Base Page class providing common navigation and locator utilities."""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, path: str) -> None:
        self.page.goto(path)

    def get_locator(self, selector: str) -> Locator:
        return self.page.locator(selector)
