
from pages.base_page import BasePage
from urls import Urls
from locators.personal_account_locators import PersonalAccountLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class PersonalAccountPage(BasePage):
    
    @allure.step("Клик по кнопке 'Личный кабинет' на главной странице")
    def click_login_account_button(self):
        self.click_element(PersonalAccountLocators.BUTTON_LOGIN_ACCOUNT)
        WebDriverWait(self.driver, 15).until(
            lambda d: d.current_url != Urls.HOME_URL
        )
    
    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.enter_text(PersonalAccountLocators.INPUT_EMAIL, email)
    
    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.enter_text(PersonalAccountLocators.INPUT_PASSWORD, password)
    
    @allure.step("Клик по кнопке 'Войти'")
    def click_login_button(self):
        self.click_element(PersonalAccountLocators.BUTTON_LOGIN)
        WebDriverWait(self.driver, 15).until(
            lambda d: Urls.CONTAINS_LOGIN not in d.current_url
        )
    
    @allure.step("Авторизация пользователя")
    def login(self, email, password):

        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
    @allure.step("Переход в раздел 'История заказов'")
    def click_order_history_link(self):

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(PersonalAccountLocators.BUTTON_LOGOUT)
        )
        
        link = self.find_element(PersonalAccountLocators.LINK_ORDER_HISTORY)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LINK_ORDER_HISTORY)
        )
        element.click()

        WebDriverWait(self.driver, 15).until(
            EC.url_contains(Urls.CONTAINS_ORDER_HISTORY)
        )
    
    @allure.step("Клик по кнопке 'Выход'")
    def click_logout_button(self):
        self.click_element(PersonalAccountLocators.BUTTON_LOGOUT)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(PersonalAccountLocators.BUTTON_LOGIN_ACCOUNT)
        )
    
    @allure.step("Проверка, что пользователь вышел из аккаунта")
    def is_user_logged_out(self):

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PersonalAccountLocators.BUTTON_LOGIN_ACCOUNT)
            )
            return True
        except:
            return False
        