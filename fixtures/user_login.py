import pytest
from pages.auth_page import AuthPage

import time

@pytest.fixture(scope="class")
def user_login(browser):
    m = AuthPage(browser)
    m.user_login()