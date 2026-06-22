
import pytest
import allure
from pages.personal_account_page import PersonalAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_navigate_to_profile(self, driver, create_user):

        user_data, response_data, status_code = create_user
        email = user_data["email"]
        password = user_data["password"]
        
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_login_account_button()
        personal_account_page.login(email, password)
        
        personal_account_page.click_login_account_button()
        WebDriverWait(driver, 15).until(EC.url_contains(Urls.CONTAINS_ACCOUNT))
        current_url = personal_account_page.get_url()

        assert Urls.CONTAINS_ACCOUNT in current_url
    

    @allure.title("Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, driver, create_user):

        user_data, response_data, status_code = create_user
        email = user_data["email"]
        password = user_data["password"]
        
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_login_account_button()
        personal_account_page.login(email, password)
        personal_account_page.click_login_account_button()
        personal_account_page.click_order_history_link()
        WebDriverWait(driver, 15).until(EC.url_contains(Urls.CONTAINS_ORDER_HISTORY))
        
        assert personal_account_page.get_url() == Urls.ORDER_HISTORY_URL
    

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, create_user):

        user_data, response_data, status_code = create_user
        email = user_data["email"]
        password = user_data["password"]
        
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_login_account_button()
        personal_account_page.login(email, password)
        personal_account_page.click_login_account_button()
        personal_account_page.click_logout_button()
        
        assert personal_account_page.is_user_logged_out()
        