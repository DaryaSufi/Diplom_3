from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
import allure
class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((PasswordRecoveryPageLocators.personal_account_buttom)))
        self.driver.find_element(*PasswordRecoveryPageLocators.personal_account_buttom).click()