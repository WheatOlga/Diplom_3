
from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ForgotPasswordPage(BasePage):
    
    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_login_account_button(self):
        self.click_element(ForgotPasswordLocators.BUTTON_LOGIN_ACCOUNT)
    
    @allure.step("Переход на страницу восстановления пароля")
    def click_forgot_password_button(self):
        self.click_element(ForgotPasswordLocators.BUTTON_FORGOT_PASSWORD)
    
    @allure.step("Ввод email")
    def enter_email(self, email):
        self.enter_text(ForgotPasswordLocators.INPUT_EMAIL, email)
    
    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click_element(ForgotPasswordLocators.BUTTON_RESTORE)
        self.wait_until_element_invisible(ForgotPasswordLocators.BUTTON_RESTORE)
    
    @allure.step("Клик по иконке показать/скрыть пароль")
    def click_password_icon(self):
        try:
            self.wait_until_element_invisible(ForgotPasswordLocators.MODAL_OVERLAY)
        except Exception:
            pass  
        self.wait_clickable_element(ForgotPasswordLocators.ICON_ACTION_PASSWORD)
        self.click_element(ForgotPasswordLocators.ICON_ACTION_PASSWORD)
    
    @allure.step("Ввод нового пароля")
    def enter_new_password(self, password):
        self.enter_text(ForgotPasswordLocators.INPUT_NEW_PASSWORD, password)
    
    @allure.step("Клик по кнопке 'Сохранить'")
    def click_save_button(self):
        self.click_element(ForgotPasswordLocators.BUTTON_SAVE)

    @allure.step("Проверка активности поля пароля")    
    def is_password_field_active(self):
        password_parent = self.find_element(ForgotPasswordLocators.INPUT_NEW_PASSWORD)
        class_attr = password_parent.get_attribute("class")
        return "active" in class_attr or "input_status-active" in class_attr

    @allure.step("Проверка активности поля email")    
    def is_email_field_displayed(self):
        element = self.find_element(ForgotPasswordLocators.INPUT_EMAIL)
        return element.is_displayed()
    
    @allure.step("Проверка успешного восстановления пароля")
    def is_restore_successful(self) -> bool:
        try:
            email_displayed = self.displaying_element(ForgotPasswordLocators.INPUT_EMAIL)
            if email_displayed:
                return True
            
            save_displayed = self.displaying_element(ForgotPasswordLocators.BUTTON_SAVE)
            return save_displayed
        except Exception:
            return False
    