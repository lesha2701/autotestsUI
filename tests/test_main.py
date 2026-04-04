import pytest
import allure
from pages.base_actions import Base
from data.constants import MainConst
from data.assertions import Assertions
from locators.main import Main

@pytest.mark.regression
@pytest.mark.mainPage
@pytest.mark.usefixtures("user_login")
class TestMainPage:

    @allure.title("Check Title on main page")
    def test_check_main_title(self, browser):

        """
        Автотест, проверяющий текст на главной странице
        
        Шаги:
        - авторизация
        - проверка текста на главной странице

        """

        asserts = Assertions(browser)

        asserts.have_text(
            Main.MAIN_TEXT,
            MainConst.CORRECT_TEXT_MAIN,
            MainConst.FAIL_TEXT
        )

        
