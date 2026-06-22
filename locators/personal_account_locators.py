
from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    BUTTON_LOGIN_ACCOUNT = (By.XPATH, '//p[text() = "Личный Кабинет"]')
    INPUT_EMAIL = (By.XPATH, '//input[@name="name"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')
    

    PROFILE_TITLE = (By.XPATH, '//p[text()="Профиль"]')
    LINK_ORDER_HISTORY = (By.XPATH, '//a[text()="История заказов"]')
    BUTTON_LOGOUT = (By.XPATH, '//button[text()="Выход"]')