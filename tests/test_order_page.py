
import pytest
from pages.order_page import OrderPage
import allure


class TestOrderPage:

    @allure.title('Проверка, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_info(self, driver):
        order_page = OrderPage(driver)
        order_page.click_button_order_feed()
        order_page.click_order()

        assert order_page.check_displaying_order_info()


    @allure.title('Заказы пользователя из раздела История заказов отображаются на странице Лента заказов')
    def test_feed_order_history_order(self, driver, create_user):
        order_page = OrderPage(driver)
        
        order_page.login_to_account(create_user)
        order_page.wait_bun()
        order_page.drag_and_drop_ingredient_to_burger_area()
        order_page.click_create_order()
        order_page.wait_until_text_visible()
        order_page.incorrect_number_invisible()
        order_page.click_order_exit_button()
        order_page.click_button_personal_account()
        order_page.click_history_order()
        order_number_history = order_page.text_history_order_number()
        order_page.click_button_order_feed()
        order_found = order_page.find_order_in_feed_by_number(order_number_history)
        
        assert order_found


    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_feed_order_total_counter(self, driver, create_user):
        order_page = OrderPage(driver)
        order_page.login_to_account(create_user)
        order_page.click_button_order_feed()
        order_all_time = int(order_page.text_order_all_time())
        order_page.click_constructor()
        order_page.wait_bun()
        order_page.drag_and_drop_ingredient_to_burger_area()
        order_page.click_create_order()
        order_page.wait_until_text_visible()
        order_page.incorrect_number_invisible()
        order_page.click_order_exit_button()
        order_page.click_button_order_feed()
        new_order_all_time = int(order_page.text_order_all_time())
        
        assert new_order_all_time > order_all_time


    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_feed_order_today_counter(self, driver, create_user):
        order_page = OrderPage(driver)
        order_page.login_to_account(create_user)
        order_page.click_button_order_feed()
        order_today = int(order_page.text_order_today())
        order_page.click_constructor()
        order_page.wait_bun()
        order_page.drag_and_drop_ingredient_to_burger_area()
        order_page.click_create_order()
        order_page.wait_until_text_visible()
        order_page.incorrect_number_invisible()
        order_page.click_order_exit_button()
        order_page.click_button_order_feed()
        order_page.wait_until_today_counter_increases(order_today)
        new_order_today = int(order_page.text_order_today())
        
        assert new_order_today > order_today


    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_number_appears_in_work_section(self, driver, create_user):
        order_page = OrderPage(driver)
        order_page.login_to_account(create_user)
        order_page.click_constructor()
        order_page.wait_bun()
        order_page.drag_and_drop_ingredient_to_burger_area()
        order_page.click_create_order()
        order_page.wait_until_text_visible()
        order_page.incorrect_number_invisible()
        created_order_number = order_page.text_order_number()
        order_page.click_order_exit_button()
        order_page.click_button_order_feed()
        order_in_work = order_page.is_order_in_work_section(created_order_number)

        assert order_in_work
