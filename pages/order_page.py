
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure


class OrderPage(BasePage):

    @allure.step('Вход в аккаунт')
    def login_to_account(self, create_user):
        user_data, _, _ = create_user
        email = user_data["email"]
        password = user_data["password"]

        self.wait_visibility_element(OrderPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element(OrderPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.wait_visibility_element(OrderPageLocators.EMAIL)
        self.enter_text(OrderPageLocators.EMAIL, email)
        self.enter_text(OrderPageLocators.PASSWORD, password)
        self.click_element(OrderPageLocators.BUTTON_LOGIN)
        self.wait_visibility_element(OrderPageLocators.BUN)

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_button_order_feed(self):
        self.wait_visibility_element(OrderPageLocators.ORDER_FEED_BUTTON)
        self.click_element(OrderPageLocators.ORDER_FEED_BUTTON)
        self.wait_visibility_element(OrderPageLocators.ORDER_FEED)

    @allure.step('Клик по заказу')
    def click_order(self):
        self.wait_visibility_element(OrderPageLocators.ORDER_FEED)
        self.click_element(OrderPageLocators.ORDER_FEED)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderPageLocators.ORDER_INFO)
        )

    @allure.step('Проверить наличие на странице окна заказа')
    def check_displaying_order_info(self):
        return self.displaying_element(OrderPageLocators.ORDER_INFO)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_burger_area(self):
        source_element = self.find_element(OrderPageLocators.BUN)
        target_element = self.find_element(OrderPageLocators.BURGER_AREA)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Ожидание булочки')
    def wait_bun(self):
        self.wait_clickable_element(OrderPageLocators.BUN)

    @allure.step('Оформить заказ')
    def click_create_order(self):
        self.click_element(OrderPageLocators.CREATE_ORDER)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_button_personal_account(self):
        self.wait_clickable_element(OrderPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element(OrderPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.wait_visibility_element(OrderPageLocators.BUTTON_ORDER_HISTORY)

    @allure.step('Клик кнопки «История заказов»')
    def click_history_order(self):
        self.wait_visibility_element(OrderPageLocators.BUTTON_ORDER_HISTORY)
        self.click_element(OrderPageLocators.BUTTON_ORDER_HISTORY)
        self.wait_visibility_element(OrderPageLocators.ORDER_NUMBER)

    @allure.step('Закрытия окна с заказом')
    def click_order_exit_button(self):
        self.wait_clickable_element(OrderPageLocators.ORDER_EXIT_BUTTON)
        self.click_element(OrderPageLocators.ORDER_EXIT_BUTTON)

    @allure.step("Получить номер заказа из Истории заказов")
    def text_history_order_number(self) -> str:
        """Получает номер первого заказа из Истории заказов"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_NUMBER)
        )
        return element.text.strip()
    
    @allure.step('Получить количество заказов за всё время')
    def text_order_all_time(self):
        self.wait_visibility_element(OrderPageLocators.ORDER_ALL_TIME)
        return self.get_text_element(OrderPageLocators.ORDER_ALL_TIME)

    @allure.step('Получить количество заказов за сегодня')
    def text_order_today(self):
        self.wait_visibility_element(OrderPageLocators.ORDER_TODAY)
        return self.get_text_element(OrderPageLocators.ORDER_TODAY)

    @allure.step('Клик по Конструктор')
    def click_constructor(self):
        self.wait_clickable_element(OrderPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(OrderPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получить номер заказа после оформления')
    def text_order_number(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderPageLocators.MODAL_SUCCESS)
        )

        WebDriverWait(self.driver, 15).until(
            lambda d: self.get_text_element(OrderPageLocators.MODAL_SUCCESS_NUMBER) != "9999"
        )
        return self.get_text_element(OrderPageLocators.MODAL_SUCCESS_NUMBER)

    @allure.step('Получить номер заказа в работе')
    def text_order_number_work(self):
        self.wait_visibility_element(OrderPageLocators.ORDER_NUMBER_WORK)
        return self.get_text_element(OrderPageLocators.ORDER_NUMBER_WORK)

    @allure.step("Убеждаемся, что номер заказа не 9999")
    def incorrect_number_invisible(self):
        self.wait_until_element_invisible(OrderPageLocators.INCORRECT_NUMBER)

    @allure.step("Ожидаем видимости текста в модальном окне")
    def wait_until_text_visible(self):
        self.wait_visibility_element(OrderPageLocators.MODAL_GET_ORDER)

    @allure.step('Клик по заказу с номером {order_number} в ленте')
    def click_order_by_number(self, order_number):

        locator = (By.XPATH, f'//a[contains(@class, "OrderHistory_link")]//p[contains(text(), "#{order_number}")]/ancestor::a')
        
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator)
        )
        
        self.click_element(locator)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderPageLocators.ORDER_INFO)
        )

    @allure.step('Получить номер заказа со страницы деталей')
    def get_order_number_from_details(self):

        self.wait_visibility_element(OrderPageLocators.ORDER_NUMBER)
        text = self.get_text_element(OrderPageLocators.ORDER_NUMBER)

        return text.replace('#', '').strip()
    
    @allure.step("Найти заказ по номеру в Ленте заказов")
    def find_order_in_feed_by_number(self, order_number: str) -> bool:
        try:
            # ✅ ИСПРАВЛЕНО: используем ORDER_NUMBER_IN_FEED_TEMPLATE
            locator = (By.XPATH, OrderPageLocators.ORDER_NUMBER_IN_FEED_TEMPLATE.format(order_number=order_number))
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            return False
        
    @allure.step("Проверить наличие заказа в разделе 'В работе'")
    def is_order_in_work_section(self, order_number: str) -> bool:

        try:
            locator = (By.XPATH, OrderPageLocators.ORDER_NUMBER_IN_WORK_TEMPLATE.format(order_number=order_number))
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

            return element.is_displayed()
        except TimeoutException:
            return False
        
    @allure.step("Ожидание увеличения счётчика 'Выполнено за сегодня'")
    def wait_until_today_counter_increases(self, initial_value: int, timeout: int = 30):

        WebDriverWait(self.driver, timeout).until(
            lambda d: int(self.text_order_today()) > initial_value
        )
        