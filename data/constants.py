import os

class Constants:
    try:
        email = os.getenv("AUTH_LOGIN")
        user = os.getenv("AUTH_USER")
        password = os.getenv("AUTH_PASSWORD")
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")

class MainConst:

    CORRECT_TEXT = "Dashboard"
    FAIL_TEXT = "Текст на странице не соответствует ожидаемому"