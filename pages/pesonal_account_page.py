import allure
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from locators.personal_account_page_locatos import PersonalAccountPageLocators
from constants import Constants

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Constants.BASE_URL

    @allure.step('Переходим на сайт для заказа бургеров')
    def open(self):
        self.go_to_site(self.url)

    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        self.click_element_via_js(PasswordRecoveryPageLocators.personal_account_button)


    @allure.step('Создаем пользователя и авторизуемся')
    def create_user_and_autorization(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        self.wait_for_element_to_be_clickable(PersonalAccountPageLocators.input_email_entrance)
        self.fill_form(PersonalAccountPageLocators.input_email_entrance, login_data["email"])
        self.wait_for_element_to_be_clickable(PersonalAccountPageLocators.input_password_entrance)
        self.fill_form(PersonalAccountPageLocators.input_password_entrance, login_data["password"])
        self.click_element_via_js(PersonalAccountPageLocators.entrance_button)

    @allure.step('Открываем раздел история заказов')
    def open_history_orders(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryPageLocators.personal_account_button)
        self.click_element_via_js(PasswordRecoveryPageLocators.personal_account_button)
        self.wait_for_element_to_be_clickable(PersonalAccountPageLocators.history_orders_button)
        self.click_element_via_js(PersonalAccountPageLocators.history_orders_button)

    @allure.step('Выходим из аккаунта')
    def exit_personal_account(self):
        self.wait_for_element_to_be_clickable(PersonalAccountPageLocators.button_exit)
        self.click_element_via_js(PersonalAccountPageLocators.button_exit)

    @allure.step('Проверяем видимость входа в систему')
    def is_sign_entrance_visible(self):
        return self.is_element_visible(PersonalAccountPageLocators.sign_entrance)








