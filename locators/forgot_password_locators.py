from selenium.webdriver.common.by import By

class ForgotPasswordLocators:

    BUTTON_LOGIN_ACCOUNT = (By.XPATH, '//p[text() = "Личный Кабинет"]') # кнопка Личный кабинет
    BUTTON_FORGOT_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]') # кнопка Восстановить пароль
    BUTTON_RESTORE = (By.XPATH, '//button[text()="Восстановить"]') # кнопка Восстановить
    INPUT_EMAIL = (By.XPATH, '//input[@name="name"]') # поле ввода email
    ICON_ACTION_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]') # показать пароль
    INPUT_NEW_PASSWORD = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::*') # поле ввода нового пароля
    BUTTON_SAVE = (By.XPATH, '//button[text()="Сохранить"]') # кнопка Сохранить
    MODAL_OVERLAY = (By.XPATH, '//div[contains(@class, "Modal_modal_overlay")]') 