import pytest
from pages.base_actions import Base
from data.constants import MainConst
from data.assertions import Assertions
from locators.main import Main

@pytest.mark.regression
@pytest.mark.mainPage
@pytest.mark.usefixtures("user_login")
class TestMainPage:

    def test_main_text(self, browser):

        """
        Автотест, проверяющий текст на главной странице
        
        Шаги:
        - авторизация
        - проверка текста на главной странице

        """

        asserts = Assertions(browser)

        asserts.have_text(
            Main.MAIN_TEXT,
            MainConst.CORRECT_TEXT,
            MainConst.FAIL_TEXT
        )

        
