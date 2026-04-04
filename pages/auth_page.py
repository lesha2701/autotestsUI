from pages.base_actions import Base
from data.constants import Constants
from locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page

from time import sleep


class AuthPage(Base):

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def user_login(self):
        self.open("")
        self.input_by_label(Auth.LABEL_INPUT_EMAIL, Constants.email)
        self.input_by_label(Auth.LABEL_INPUT_USER, Constants.user)
        self.input_by_label(Auth.LABEL_INPUT_PASSOWD, Constants.password)

        self.click(Auth.LOGIN_BTN)
        
        self.page.wait_for_load_state("networkidle", timeout=30000)
