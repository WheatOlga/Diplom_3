
from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_FEED_BUTTON = (By.XPATH, '//p[text() = "Лента Заказов"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')
    BUTTON_ORDER_HISTORY = (By.XPATH, '//a[text() = "История заказов"]')

    EMAIL = (By.XPATH, '//input[@name="name"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')

    BUN = (By.XPATH, '//p[text() = "Краторная булка N-200i"]')
    BURGER_AREA = (By.XPATH, '//div[contains(@class, "constructor-element_pos_top")]/..')

    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')

    ORDER_INFO = (By.XPATH, '//p[contains(@class, "text_type_digits-default") and contains(text(), "#")]')
    ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "text_type_digits-default") and contains(text(), "#")]')
    ORDER_EXIT_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")
    INCORRECT_NUMBER = (By.XPATH, '//p[contains(text(), "#9999")]')
    MODAL_GET_ORDER = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]//p[contains(text(), "Ваш заказ начал")]')

    MODAL_SUCCESS = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]')
    MODAL_SUCCESS_NUMBER = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]//h2[contains(@class, "text_type_digits")]')
    MODAL_SUCCESS_CLOSE = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]//button[contains(@class, "close")]')

    ORDER_FEED = (By.XPATH, '(//a[contains(@class, "OrderHistory_link")])[1]')
    ORDER_NUMBER_FEED = (By.XPATH, '(//a[contains(@class, "OrderHistory_link")]//p[contains(@class, "text_type_digits-default")])[1]')
    
    ORDER_BY_NUMBER_TEMPLATE = (By.XPATH, '//a[contains(@class, "OrderHistory_link")]//p[contains(text(), "#{order_number}")]/ancestor::a')
    ORDER_NUMBER_IN_FEED_TEMPLATE = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and text()='{order_number}']")
    ORDER_NUMBER_IN_WORK_TEMPLATE = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')

    ORDER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    ORDER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    ORDER_NUMBER_WORK = (By.XPATH, '//p[contains(text(), "В работе:")]/following-sibling::*//p[contains(@class, "text_type_digits")]')
