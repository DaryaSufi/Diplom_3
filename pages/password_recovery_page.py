import allure
from constants import Constants
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Constants.BASE_URL

    @allure.step('Переходим на сайт для заказа бургеров')
    def open(self):
        self.go_to_site(self.url)

    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        self.click_element_via_js(PasswordRecoveryPageLocators.personal_account_button)

    @allure.step('Нажимаем кнопку восстановления пароля')
    def click_password_recovery_buton(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryPageLocators.button_password_recovery)
        self.click_element_via_js(PasswordRecoveryPageLocators.button_password_recovery)


    @allure.step('Заполняем поле email и нажимаем кнопку Восстановить')
    def fill_email_form(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryPageLocators.input_email_for_pass_recov)
        self.fill_form(PasswordRecoveryPageLocators.input_email_for_pass_recov, Constants.EMAIL)
        self.wait_for_element_to_be_clickable(PasswordRecoveryPageLocators.button_recovery)
        self.click_element_via_js(PasswordRecoveryPageLocators.button_recovery)
        self.wait()

    @allure.step('Кликаем по кнопке показать/скрыть пароль')
    def click_eye_icon(self):
        self.wait()
        self.wait_for_element_to_be_clickable(PasswordRecoveryPageLocators.eye_icon)
        self.click_element_via_js(PasswordRecoveryPageLocators.eye_icon)
        self.wait_for_element_to_be_clickable(PasswordRecoveryPageLocators.input_in_focus)

    @allure.step('Проверяем видимость поля ввода пароля в фокусе')
    def is_input_in_focus_visible(self):
        return self.is_element_visible(PasswordRecoveryPageLocators.input_in_focus)


