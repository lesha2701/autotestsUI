from playwright.sync_api import Page
from data.environment import host
from playwright.sync_api import expect
from pages.base_actions import Base

class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def check_url(self, url, msg):
        expect(self.page).to_have_url(f"{host.get_base_url()}{url}", timeout=10000), msg

    def check_presence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=10000), msg

    def check_absence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_hidden(timeout=10000), msg

    def have_text(self, locator, data, msg):
        loc = self.page.locator(locator)
        expect(loc).to_have_text(data), msg