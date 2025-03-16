import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_functional_page_locators import MainFunctionalPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class MainFunctionalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    @allure.step('Нажимаем на конструктор')
    def click_on_constructor(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.designer)))
        self.driver.find_element(*MainFunctionalPageLocators.designer).click()



    @allure.step('Нажимаем на ленту заказов')
    def click_on_order_feed(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.order_feed)))
        self.driver.find_element(*MainFunctionalPageLocators.order_feed).click()



    @allure.step('Открываем окно с деталями ингридиента')
    def open_ingredient_window(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.ingridient)))
        element=self.driver.find_element(*MainFunctionalPageLocators.ingridient)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.ingridient_card)))

    @allure.step('Закрываем окно с деталями ингридиента')
    def close_ingredient_window(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.ingridient_card_close_button)))
        element=self.driver.find_element(*MainFunctionalPageLocators.ingridient_card_close_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.ingridient)))

    @allure.step('Добавляем ингридиент в заказ')
    def adding_ingredients_to_order(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.ingridient)))
        source_element = self.driver.find_element(By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and @href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
        target_element = self.driver.find_element(By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")
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

    @allure.step('Открываем личный кабинет')
    def open_personal_account(self):
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.personal_account_button)))
        element = self.driver.find_element(*MainFunctionalPageLocators.personal_account_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step('Создаем пользователя и авторизуемся')
    def create_user_and_autorization(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((MainFunctionalPageLocators.input_email_entrance)))
        self.fill_form(MainFunctionalPageLocators.input_email_entrance, login_data["email"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((MainFunctionalPageLocators.input_password_entrance)))
        self.fill_form(MainFunctionalPageLocators.input_password_entrance, login_data["password"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((MainFunctionalPageLocators.entrance_button)))
        element = self.driver.find_element(*MainFunctionalPageLocators.entrance_button)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step('Добавляем соус в заказ')
    def adding_sauce_to_order(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.list_of_sauces)))
        element = self.driver.find_element(*MainFunctionalPageLocators.list_of_sauces)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.sauces_ingridient)))
        source_element = self.driver.find_element(By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')and @href='/ingredient/61c0c5a71d1f82001bdaaa72']")
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

    @allure.step('Добавляем начинку в заказ')
    def adding_filling_to_order(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.list_of_fillings)))
        element = self.driver.find_element(*MainFunctionalPageLocators.list_of_fillings)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.filling_ingridient)))
        source_element = self.driver.find_element(By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')and @href='/ingredient/61c0c5a71d1f82001bdaaa6f']")
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

    @allure.step('Нажимаем кнопку оформить заказ')
    def click_chekout_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((MainFunctionalPageLocators.checkout_button)))
        element = self.driver.find_element(*MainFunctionalPageLocators.checkout_button)
        self.driver.execute_script("arguments[0].click();", element)







