import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_feed_page_locators import  OrderFeedPageLocators
from pages.base_page import BasePage

import time

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Открываем ленту заказов')
    def open_order_feed(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.order_feed)))
        time.sleep(1)
        self.driver.find_element(*OrderFeedPageLocators.order_feed).click()


    @allure.step('Кликаем на заказ в ленте заказов')
    def click_order(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.order)))
        self.driver.find_element(*OrderFeedPageLocators.order).click()

    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.personal_account_button)))
        element = self.driver.find_element(*OrderFeedPageLocators.personal_account_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step('Открываем раздел история заказов')
    def open_history_orders(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((OrderFeedPageLocators.history_orders_button)))
        element2 = self.driver.find_element(*OrderFeedPageLocators.history_orders_button)
        self.driver.execute_script("arguments[0].click();", element2)

    @allure.step('Создаем пользователя и авторизуемся')
    def create_user_and_autorization(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((OrderFeedPageLocators.input_email_entrance)))
        self.fill_form(OrderFeedPageLocators.input_email_entrance, login_data["email"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((OrderFeedPageLocators.input_password_entrance)))
        self.fill_form(OrderFeedPageLocators.input_password_entrance, login_data["password"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((OrderFeedPageLocators.entrance_button)))
        element = self.driver.find_element(*OrderFeedPageLocators.entrance_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")
    @allure.step('Оформляем заказ')
    def making_an_order(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.ingridient)))
        source_element = self.driver.find_element(By.XPATH,"//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and @href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
        target_element = self.driver.find_element(By.XPATH,"//div[@class='constructor-element constructor-element_pos_top']")
        self.driver.execute_script("""
                        const source = arguments[0];
                        const target = arguments[1];
                        const event = new MouseEvent('mousedown', { bubbles: true });
                        source.dispatchEvent(event);
                        const dragEvent = new DragEvent('dragstart', { bubbles: true });
                        source.dispatchEvent(dragEvent);
                        const dropEvent = new DragEvent('drop', { bubbles: true });
                        target.dispatchEvent(dropEvent);
                        const dragEndEvent = new DragEvent('dragend', { bubbles: true });
                        source.dispatchEvent(dragEndEvent);
                    """, source_element, target_element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.list_of_sauces)))
        element = self.driver.find_element(*OrderFeedPageLocators.list_of_sauces)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.sauces_ingridient)))
        source_element = self.driver.find_element(By.XPATH,"//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')and @href='/ingredient/61c0c5a71d1f82001bdaaa72']")
        target_element = self.driver.find_element(By.XPATH,"//div[@class='constructor-element constructor-element_pos_top']")
        self.driver.execute_script("""
                        const source = arguments[0];
                        const target = arguments[1];
                        const event = new MouseEvent('mousedown', { bubbles: true });
                        source.dispatchEvent(event);
                        const dragEvent = new DragEvent('dragstart', { bubbles: true });
                        source.dispatchEvent(dragEvent);
                        const dropEvent = new DragEvent('drop', { bubbles: true });
                        target.dispatchEvent(dropEvent);
                        const dragEndEvent = new DragEvent('dragend', { bubbles: true });
                        source.dispatchEvent(dragEndEvent);
                    """, source_element, target_element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.list_of_fillings)))
        element = self.driver.find_element(*OrderFeedPageLocators.list_of_fillings)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.filling_ingridient)))
        source_element = self.driver.find_element(By.XPATH,"//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')and @href='/ingredient/61c0c5a71d1f82001bdaaa6f']")
        target_element = self.driver.find_element(By.XPATH,"//div[@class='constructor-element constructor-element_pos_top']")
        self.driver.execute_script("""
                        const source = arguments[0];
                        const target = arguments[1];
                        const event = new MouseEvent('mousedown', { bubbles: true });
                        source.dispatchEvent(event);
                        const dragEvent = new DragEvent('dragstart', { bubbles: true });
                        source.dispatchEvent(dragEvent);
                        const dropEvent = new DragEvent('drop', { bubbles: true });
                        target.dispatchEvent(dropEvent);
                        const dragEndEvent = new DragEvent('dragend', { bubbles: true });
                        source.dispatchEvent(dragEndEvent);
                    """, source_element, target_element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.checkout_button)))
        element = self.driver.find_element(*OrderFeedPageLocators.checkout_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.order_number_from_order_info)))
        time.sleep(3)
        order_number_from_order_info = self.driver.find_element(*OrderFeedPageLocators.order_number_from_order_info)
        text=f"#0{order_number_from_order_info.text}"
        return text

    @allure.step('Получаем список номеров заказов')
    def get_list_order_numbers(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.order_number)))
        elements = self.driver.find_elements(*OrderFeedPageLocators.order_number)
        texts = [element.text for element in elements]
        return texts

    @allure.step('Получаем число количества заказов за все время')
    def get_the_number_of_orders_for_all_time(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.number_of_orders_for_all_time)))
        time.sleep(3)
        elements = self.driver.find_elements(*OrderFeedPageLocators.number_of_orders_for_all_time)
        texts = [element.text for element in elements]
        return texts

    @allure.step('Нажимаем на кнопку конструктор')
    def click_button_constructor(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((OrderFeedPageLocators.constructor_button)))
        element2 = self.driver.find_element(*OrderFeedPageLocators.constructor_button)
        self.driver.execute_script("arguments[0].click();", element2)

    @allure.step('Получаем число количества заказов за сегодня')
    def get_the_number_of_orders_for_today(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.number_of_orders_for_today)))
        time.sleep(3)
        elements = self.driver.find_elements(*OrderFeedPageLocators.number_of_orders_for_today)
        texts = [element.text for element in elements]
        return texts

    @allure.step('Получаем список номеров заказов в работе')
    def get_list_order_numbers_in_work(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.list_of_orders_in_work)))
        time.sleep(3)
        elements = self.driver.find_elements(*OrderFeedPageLocators.list_of_orders_in_work)
        texts = [element.text for element in elements]
        return texts

    @allure.step('Оформляем мини заказ')
    def making_an_mini_order(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.ingridient)))
        source_element = self.driver.find_element(By.XPATH,
                                                  "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and @href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
        target_element = self.driver.find_element(By.XPATH,
                                                  "//div[@class='constructor-element constructor-element_pos_top']")
        self.driver.execute_script("""
                            const source = arguments[0];
                            const target = arguments[1];
                            const event = new MouseEvent('mousedown', { bubbles: true });
                            source.dispatchEvent(event);
                            const dragEvent = new DragEvent('dragstart', { bubbles: true });
                            source.dispatchEvent(dragEvent);
                            const dropEvent = new DragEvent('drop', { bubbles: true });
                            target.dispatchEvent(dropEvent);
                            const dragEndEvent = new DragEvent('dragend', { bubbles: true });
                            source.dispatchEvent(dragEndEvent);
                        """, source_element, target_element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.checkout_button)))
        element = self.driver.find_element(*OrderFeedPageLocators.checkout_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((OrderFeedPageLocators.order_number_from_order_info)))
        time.sleep(5)
        order_number_from_order_info = self.driver.find_element(*OrderFeedPageLocators.order_number_from_order_info)
        text = f"0{order_number_from_order_info.text}"
        return text






        