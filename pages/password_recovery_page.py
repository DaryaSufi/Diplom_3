import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.personal_account_button)))
        element=self.driver.find_element(*PasswordRecoveryPageLocators.personal_account_button)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Нажимаем кнопку восстановления пароля')
    def click_password_recovery_buton(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.button_password_recovery)))
        element=self.driver.find_element(*PasswordRecoveryPageLocators.button_password_recovery)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Заполняем поле email и нажимаем кнопку Восстановить')
    def fill_email_form(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.input_email_for_pass_recov)))
        self.fill_form(PasswordRecoveryPageLocators.input_email_for_pass_recov, Constants.EMAIL)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.button_recovery)))
        element=self.driver.find_element(*PasswordRecoveryPageLocators.button_recovery)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step('Кликаем по кнопке показать/скрыть пароль')
    def click_eye_icon(self):
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.eye_icon)))
        element=self.driver.find_element(*PasswordRecoveryPageLocators.eye_icon)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.input_in_focus)))


