
import pytest
import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from urls import Urls


class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_link()

        assert Urls.CONSTRUCTOR_URL in main_page.get_url()


    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigate_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_link()

        assert main_page.is_feed_title_displayed()
        assert main_page.get_url() == Urls.FEED_URL


    @allure.title("Клик по ингредиенту открывает модальное окно")
    def test_click_bun_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_bun()

        assert main_page.is_bun_modal_displayed()


    @allure.title("Модальное окно закрывается кликом по крестику")
    def test_modal_closes_on_cross_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_bun()
        main_page.close_ingredient_modal()

        assert not main_page.is_bun_modal_displayed()


    @allure.title("При добавлении ингредиента в заказ, увеличивается количество данного ингредиента")
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.wait_bun()
        main_page.drag_and_drop_ingredient_to_burger_area()
        
        assert main_page.get_count_ingredients() == '2'


    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_order(self, driver, create_user):
        user_data, _, _ = create_user
        email = user_data["email"]
        password = user_data["password"]
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_login_account_button()
        personal_account_page.login(email, password)
        main_page.wait_bun()
        main_page.drag_and_drop_ingredient_to_burger_area()
        main_page.click_order()

        assert main_page.check_order()
