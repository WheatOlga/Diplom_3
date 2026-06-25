from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
import allure


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    @allure.step("Поиск элемента с ожиданием")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    @allure.step("Ожидание видимости элемента")
    def wait_visibility_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Ожидание кликабельности элемента")
    def wait_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    @allure.step("Ожидание исчезновения элемента")
    def wait_until_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    @allure.step("Ожидание выполнения условия")
    def wait_until(self, condition, timeout=10):
        WebDriverWait(self.driver, timeout).until(condition)
    
    @allure.step("Клик по элементу")
    def click_element(self, locator, timeout=10):
        element = self.wait_clickable_element(locator, timeout)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста в поле")
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text_element(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Проверка отображения элемента")
    def displaying_element(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False

    @allure.step("Перетаскивает элемент")
    def drag_and_drop_element(self, source_element, target_element):

        browser_name = self.driver.capabilities.get('browserName', '').lower()
        
        if 'firefox' in browser_name:
            self._html5_drag_and_drop(source_element, target_element)
        else:
            actions = ActionChains(self.driver)
            actions.click_and_hold(source_element)
            actions.pause(0.3)
            actions.move_to_element(target_element)
            actions.pause(0.3)
            actions.release()
            actions.perform()
    
    def _html5_drag_and_drop(self, source, target):
        self.driver.execute_script("""
            function createEvent(type) {
                var event = document.createEvent('CustomEvent');
                event.initCustomEvent(type, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(type, val) { this.data[type] = val; },
                    getData: function(type) { return this.data[type]; }
                };
                return event;
            }
            
            function dispatchEvent(el, event) {
                el.dispatchEvent(event);
            }
            
            var dragStart = createEvent('dragstart');
            dispatchEvent(arguments[0], dragStart);
            
            var dragEnter = createEvent('dragenter');
            dispatchEvent(arguments[1], dragEnter);
            
            var dragOver = createEvent('dragover');
            dispatchEvent(arguments[1], dragOver);
            
            var drop = createEvent('drop');
            dispatchEvent(arguments[1], drop);
            
            var dragEnd = createEvent('dragend');
            dispatchEvent(arguments[0], dragEnd);
        """, source, target)
    
    @allure.step("Получение текущего URL")
    def get_url(self):
        return self.driver.current_url
    
    @allure.step("Открытие страницы")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Ожидание, что URL содержит подстроку")
    def wait_url_contains(self, url_part: str, timeout: int = 15):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    @allure.step("Ожидание, что URL не равен указанному")
    def wait_url_not_equal(self, url: str, timeout: int = 15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != url
        )

    @allure.step("Ожидание, что URL не содержит подстроку")
    def wait_url_not_contains(self, url_part: str, timeout: int = 15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: url_part not in d.current_url
        )
        