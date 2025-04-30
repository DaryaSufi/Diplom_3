import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_feed_page_locators import  OrderFeedPageLocators
from pages.base_page import BasePage
from constants import Constants

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Constants.BASE_URL

    @allure.step('Переходим на сайт для заказа бургеров')
    def open(self):
        self.go_to_site(self.url)

    @allure.step('Открываем ленту заказов')
    def open_order_feed(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.order_feed_2)
        self.wait()
        self.click_element_via_js(OrderFeedPageLocators.order_feed_2)
        self.wait_for_element_to_be_invisibility(OrderFeedPageLocators.inv_element)


    @allure.step('Кликаем на заказ в ленте заказов')
    def click_order(self):
       self.wait_for_element_to_be_clickable(OrderFeedPageLocators.order)
       self.click_element_via_js(OrderFeedPageLocators.order)

    @allure.step('Проверяем видимость окна с информацией о заказе')
    def is_order_info_visible(self):
        return self.is_element_visible(OrderFeedPageLocators.order_info)
    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        self.click_element_via_js(OrderFeedPageLocators.personal_account_button)


    @allure.step('Открываем раздел история заказов')
    def open_history_orders(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.history_orders_button)
        self.click_element_via_js(OrderFeedPageLocators.history_orders_button)


    @allure.step('Создаем пользователя и авторизуемся')
    def create_user_and_autorization(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.input_email_entrance)
        self.fill_form(OrderFeedPageLocators.input_email_entrance, login_data["email"])
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.input_password_entrance)
        self.fill_form(OrderFeedPageLocators.input_password_entrance, login_data["password"])
        self.click_element_via_js(OrderFeedPageLocators.entrance_button)

    @allure.step('Оформляем заказ')
    def making_an_order(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.ingridient)
        self.drag_and_drop(OrderFeedPageLocators.ingridient, OrderFeedPageLocators.ingridient_target)
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.list_of_sauces)
        self.click_element_via_js(OrderFeedPageLocators.list_of_sauces)
        self.drag_and_drop(OrderFeedPageLocators.sauces_ingridient, OrderFeedPageLocators.ingridient_target)
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.list_of_fillings)
        self.click_element_via_js(OrderFeedPageLocators.list_of_fillings)
        self.drag_and_drop(OrderFeedPageLocators.filling_ingridient, OrderFeedPageLocators.ingridient_target)
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.checkout_button)
        self.click_element_via_js(OrderFeedPageLocators.checkout_button)
        self.wait()
        order_number_from_order_info = self.find_element(OrderFeedPageLocators.order_number_from_order_info)
        self.wait_until_text_is_not_equal(OrderFeedPageLocators.order_number_from_order_info, Constants.ORDER_NUMBER)
        text=f"#0{order_number_from_order_info.text}"
        return text

    @allure.step('Получаем список номеров заказов')
    def get_list_order_numbers(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.order_number)
        elements = self.find_elements(OrderFeedPageLocators.order_number)
        self.wait()
        texts = [element.text for element in elements]
        return texts

    @allure.step('Получаем число количества заказов за все время')
    def get_the_number_of_orders_for_all_time(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.number_of_orders_for_all_time)
        self.wait()
        elements = self.find_elements(*OrderFeedPageLocators.number_of_orders_for_all_time)
        self.wait()
        texts = [element.text for element in elements]
        return texts

    @allure.step('Нажимаем на кнопку конструктор')
    def click_button_constructor(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.constructor_button)
        self.click_element_via_js(OrderFeedPageLocators.constructor_button)


    @allure.step('Получаем число количества заказов за сегодня')
    def get_the_number_of_orders_for_today(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.number_of_orders_for_today)
        self.wait()
        elements = self.find_elements(*OrderFeedPageLocators.number_of_orders_for_today)
        self.wait()
        texts = [element.text for element in elements]
        return texts

    @allure.step('Получаем список номеров заказов в работе')
    def get_list_order_numbers_in_work(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.list_of_orders_in_work)
        self.wait()
        elements = self.find_elements(*OrderFeedPageLocators.list_of_orders_in_work)
        self.wait()
        texts = [element.text for element in elements]
        return texts

    @allure.step('Оформляем мини заказ')
    def making_an_mini_order(self):
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.ingridient)
        self.drag_and_drop(OrderFeedPageLocators.ingridient, OrderFeedPageLocators.ingridient_target)
        self.wait_for_element_to_be_clickable(OrderFeedPageLocators.checkout_button)
        self.click_element_via_js(OrderFeedPageLocators.checkout_button)
        self.wait()
        order_number_from_order_info = self.find_element(OrderFeedPageLocators.order_number_from_order_info)
        self.wait_until_text_is_not_equal(OrderFeedPageLocators.order_number_from_order_info, Constants.ORDER_NUMBER)
        text = f"#0{order_number_from_order_info.text}"
        return text


