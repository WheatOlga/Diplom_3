
from selenium.webdriver.common.by import By

class MainPageLocators:

    LINK_CONSTRUCTOR = (By.XPATH, '//p[text() = "Конструктор"]')
    LINK_FEED = (By.XPATH, '//p[text() = "Лента Заказов"]')
    TITLE_ORDER_FEED = (By.XPATH, '//h1[contains(text(), "Лента")]')

    BUN = (By.XPATH, '//p[text() = "Краторная булка N-200i"]')
    BUN_INFO = (By.XPATH, '//h2[text() = "Детали ингредиента"]')

    MODAL_INGREDIENT = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]')
    MODAL_CLOSE_BUTTON = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]//button[contains(@class, "close")]')    

    BASKET_TOP_DROP_ZONE = (By.XPATH, '//div[contains(@class, "constructor-element_pos_top")]/..')
    BASKET_COUNTER = (By.XPATH, '//div[contains(@class, "counter_counter")]')
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    MODAL_ORDER_SUCCESS = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]//p[contains(text(), "Ваш заказ")]')
    MODAL_ORDER_NUMBER = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]//h2[contains(@class, "text_type_digits-large")]')
    