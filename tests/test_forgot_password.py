
import pytest
import allure
from pages.forgot_password_page import ForgotPasswordPage
from locators.forgot_password_locators import ForgotPasswordLocators


class TestForgotPassword:
    
    @allure.title("Переход на страницу восстановления пароля по кнопке")
    def test_navigate_to_forgot_password_page(self, driver):

        forgot_page = ForgotPasswordPage(driver)
        forgot_page.click_login_account_button()
        forgot_page.click_forgot_password_button()
        
        assert forgot_page.is_email_field_displayed()
    

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_restore(self, driver, create_user):

        user_data, response_data, status_code = create_user
        email = user_data["email"]
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.click_login_account_button()
        forgot_page.click_forgot_password_button()
        forgot_page.enter_email(email)
        forgot_page.click_restore_button()
        
        assert forgot_page.is_restore_successful()
    

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_button_activates_field(self, driver, create_user):

        user_data, response_data, status_code = create_user
        email = user_data["email"]
        
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.click_login_account_button()
        forgot_page.click_forgot_password_button()
        forgot_page.enter_email(email)
        forgot_page.click_restore_button()
        forgot_page.click_password_icon()
        
        assert forgot_page.is_password_field_active()
        