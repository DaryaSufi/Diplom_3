import allure
from locators.main_functional_page_locators import MainFunctionalPageLocators
from pages.base_page import BasePage
from constants import Constants

class MainFunctionalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Constants.BASE_URL

    @allure.step('Переходим на сайт для заказа бургеров')
    def open(self):
        self.go_to_site(self.url)
    @allure.step('Нажимаем на конструктор')
    def click_on_constructor(self):
        self.find_element(MainFunctionalPageLocators.designer).click()

    @allure.step('Нажимаем на ленту заказов')
    def click_on_order_feed(self):
        self.find_element(MainFunctionalPageLocators.order_feed).click()

    @allure.step('Проверяем видимость надписи "Соберите бургер"')
    def is_collect_burger_inscription_visible(self):
        return self.is_element_visible(MainFunctionalPageLocators.inscription_collect_burger)

    @allure.step('Проверяем видимость надписи "Лента заказов"')
    def is_order_feed_inscription_visible(self):
        return self.is_element_visible(MainFunctionalPageLocators.inscription_order_feed)

    @allure.step('Открываем окно с деталями ингридиента')
    def open_ingredient_window(self):
        self.click_element_via_js(MainFunctionalPageLocators.ingridient)
        self.wait_for_element_to_be_clickable(MainFunctionalPageLocators.ingridient_card)

    @allure.step('Проверяем видимость картоки ингридиента')
    def is_ingridient_card_visible(self):
        return self.is_element_visible(MainFunctionalPageLocators.ingridient_card)

    @allure.step('Закрываем окно с деталями ингридиента')
    def close_ingredient_window(self):
        self.click_element_via_js(MainFunctionalPageLocators.ingridient_card_close_button)
        self.wait_for_element_to_be_clickable(MainFunctionalPageLocators.ingridient)

    @allure.step('Проверяем видимость ингридиента')
    def is_ingridient_visible(self):
        return self.is_element_visible(MainFunctionalPageLocators.ingridient)


    @allure.step('Добавляем ингридиент в заказ')
    def adding_ingredients_to_order(self):
        self.wait_for_element_to_be_clickable(MainFunctionalPageLocators.ingridient)
        self.drag_and_drop(MainFunctionalPageLocators.ingridient, MainFunctionalPageLocators.ingridient_target)

    @allure.step('Проверяем видимость измененного каунтера ингридиента')
    def is_changed_counter_visible(self):
        return self.is_element_visible(MainFunctionalPageLocators.changed_counter)


    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        self.click_element_via_js(MainFunctionalPageLocators.personal_account_button)


    @allure.step('Создаем пользователя и авторизуемся')
    def create_user_and_autorization(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        self.wait_for_element_to_be_clickable(MainFunctionalPageLocators.input_email_entrance)
        self.fill_form(MainFunctionalPageLocators.input_email_entrance, login_data["email"])
        self.wait_for_element_to_be_clickable(MainFunctionalPageLocators.input_password_entrance)
        self.fill_form(MainFunctionalPageLocators.input_password_entrance, login_data["password"])
        self.click_element_via_js(MainFunctionalPageLocators.entrance_button)



    @allure.step('Добавляем соус в заказ')
    def adding_sauce_to_order(self):
        self.click_element_via_js(MainFunctionalPageLocators.list_of_sauces)
        self.drag_and_drop(MainFunctionalPageLocators.sauces_ingridient, MainFunctionalPageLocators.ingridient_target)

    @allure.step('Добавляем начинку в заказ')
    def adding_filling_to_order(self):
        self.click_element_via_js(MainFunctionalPageLocators.list_of_fillings)
        self.drag_and_drop(MainFunctionalPageLocators.filling_ingridient, MainFunctionalPageLocators.ingridient_target)

    @allure.step('Нажимаем кнопку оформить заказ')
    def click_chekout_button(self):
        self.click_element_via_js(MainFunctionalPageLocators.checkout_button)

    @allure.step('Проверяем видимость id заказа')
    def is_orders_id_visible(self):
        return self.is_element_visible(MainFunctionalPageLocators.orders_id)








