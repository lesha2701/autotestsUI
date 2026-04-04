import pytest
import allure
from pages.base_actions import Base
from data.constants import MainConst
from data.assertions import Assertions
from locators.main import Main


@pytest.mark.regression
@pytest.mark.coursesPage
@pytest.mark.usefixtures("user_login")
class TestCoursesPage:

    @allure.title("Check Title on courses page")
    def test_check_courses_title(self, browser):

        """
        Автотест, проверяющий текст на странице курсов
        
        Шаги:
        - авторизация
        - проверка текста на странице курсов

        """

        page = Base(browser)
        asserts = Assertions(browser)

        page.click(Main.COURSES_BTN)

        asserts.have_text(
            Main.COURSES_TEXT,
            MainConst.CORRECT_TEXT_COURSES,
            MainConst.FAIL_TEXT
        )
