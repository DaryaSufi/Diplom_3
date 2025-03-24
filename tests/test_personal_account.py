import allure
from constants import Constants
from pages.pesonal_account_page import PersonalAccountPage

class TestPersonalAccountPage:
    @allure.title("Проверка перехода по клику на Личный кабинет")
    def test_click_through_to_personal_account(self, driver):
        self.recovery = PersonalAccountPage(driver)
        self.recovery.open()
        self.recovery.open_personal_account()
        url = self.recovery.get_current_url()
        assert url == Constants.LOGIN_URL

    @allure.title("Проверка перехода в раздел История заказов")
    def test_go_to_order_history_section(self, driver, create_and_delete_user_for_login):
        self.recovery = PersonalAccountPage(driver)
        self.recovery.open()
        self.recovery.open_personal_account()
        self.recovery.create_user_and_autorization(create_and_delete_user_for_login)
        self.recovery.open_history_orders()
        url = self.recovery.get_current_url()
        assert url == Constants.ORDER_HISTORY_URL

    @allure.title("Проверка выхода из аккаунта")
    def test_exit_personal_account(self, driver, create_and_delete_user_for_login):
        self.recovery = PersonalAccountPage(driver)
        self.recovery.open()
        self.recovery.open_personal_account()
        self.recovery.create_user_and_autorization(create_and_delete_user_for_login)
        self.recovery.open_personal_account()
        self.recovery.exit_personal_account()
        assert self.recovery.is_sign_entrance_visible()





