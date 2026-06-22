
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(BasePage):

    @allure.step("Переход в раздел 'Конструктор'")
    def click_constructor_link(self):
        self.click_element(MainPageLocators.LINK_CONSTRUCTOR)

    @allure.step("Переход в раздел 'Лента заказов'")
    def click_feed_link(self):
        self.click_element(MainPageLocators.LINK_FEED)

    @allure.step("Проверка отображения заголовка 'Лента заказов'")
    def is_feed_title_displayed(self):
        element = self.find_element(MainPageLocators.TITLE_ORDER_FEED)
        return element.is_displayed()

    @allure.step("Ожидание загрузки булки")
    def wait_bun(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(MainPageLocators.BUN)
        )

    @allure.step("Клик по булке")
    def click_bun(self):
        self.wait_bun()
        self.click_element(MainPageLocators.BUN)

    @allure.step("Проверка отображения модального окна ингредиента")
    def is_bun_modal_displayed(self):
        try:
            element = self.find_element(MainPageLocators.BUN_INFO)
            return element.is_displayed()
        except:
            return False

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_INGREDIENT)
        )

    @allure.step("Перетаскивание ингредиента в зону бургера")
    def drag_and_drop_ingredient_to_burger_area(self):
        source_element = self.find_element(MainPageLocators.BUN)
        target_element = self.find_element(MainPageLocators.BASKET_TOP_DROP_ZONE)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step("Получение значения счётчика ингредиентов")
    def get_count_ingredients(self):
        try:
            element = self.find_element(MainPageLocators.BASKET_COUNTER)
            return element.text
        except:
            return '0'

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order(self):
        self.click_element(MainPageLocators.BUTTON_ORDER)

    @allure.step("Проверка успешного оформления заказа")
    def check_order(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.MODAL_ORDER_SUCCESS)
            )
            return True
        except:
            return False

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number(self) -> str:

        try:
            element = self.wait_for_visible(MainPageLocators.MODAL_ORDER_NUMBER)
            return element.text.strip()
        except Exception:
            return ""

    @allure.step("Закрытие модального окна успеха заказа")
    def close_order_modal(self):

        try:
            self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(MainPageLocators.MODAL_ORDER_SUCCESS)
            )
        except:
            pass

    @allure.step("Вход в аккаунт")
    def login_to_account(self, create_user):
        from pages.personal_account_page import PersonalAccountPage
        personal_account_page = PersonalAccountPage(self.driver)

        user_data, response_data, status_code = create_user
        email = user_data["email"]
        password = user_data["password"]

        personal_account_page.click_login_account_button()
        personal_account_page.login(email, password)
