import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from locators.personal_account_page_locatos import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.personal_account_button)))
        element=self.driver.find_element(*PasswordRecoveryPageLocators.personal_account_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")


    @allure.step('Создаем пользователя и авторизуемся')
    def create_user_and_autorization(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        WebDriverWait(self.driver, 10).until( EC.element_to_be_clickable((PersonalAccountPageLocators.input_email_entrance)))
        self.fill_form(PersonalAccountPageLocators.input_email_entrance, login_data["email"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PersonalAccountPageLocators.input_password_entrance)))
        self.fill_form(PersonalAccountPageLocators.input_password_entrance, login_data["password"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PersonalAccountPageLocators.entrance_button)))
        element=self.driver.find_element(*PersonalAccountPageLocators.entrance_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step('Открываем раздел история заказов')
    def open_history_orders(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.personal_account_button)))
        element=self.driver.find_element(*PasswordRecoveryPageLocators.personal_account_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PersonalAccountPageLocators.history_orders_button)))
        element2=self.driver.find_element(*PersonalAccountPageLocators.history_orders_button)
        self.driver.execute_script("arguments[0].click();", element2)

    @allure.step('Выходим из аккаунта')
    def exit_personal_account(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PersonalAccountPageLocators.button_exit)))
        element=self.driver.find_element(*PersonalAccountPageLocators.button_exit)
        self.driver.execute_script("arguments[0].click();", element)







