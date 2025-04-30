import allure
from constants import Constants
from pages.password_recovery_page import PasswordRecoveryPage

class TestPasswordRecoveryPage:
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль")
    def test_go_to_password_recovery_page_by_click_recovery_button(self, driver):
        self.recovery=PasswordRecoveryPage(driver)
        self.recovery.open()
        self.recovery.open_personal_account()
        self.recovery.click_password_recovery_buton()
        url = self.recovery.get_current_url()
        assert url == Constants.URL_RECOVER

    @allure.title("Проверка ввода почты и клика по кнопке Восстановить")
    def test_enter_email_and_click_recover_button(self, driver):
        self.recovery = PasswordRecoveryPage(driver)
        self.recovery.open()
        self.recovery.open_personal_account()
        self.recovery.click_password_recovery_buton()
        self.recovery.fill_email_form() 
        url = self.recovery.get_current_url()
        assert url == Constants.URL_RECOVER

    @allure.title("Проверка подсветки поля пароля при клике по кнопке показать/скрыть")
    def test_click_show_hide_buttonn(self, driver):
        self.recovery = PasswordRecoveryPage(driver)
        self.recovery.open()
        self.recovery.open_personal_account()
        self.recovery.click_password_recovery_buton()
        self.recovery.fill_email_form()
        url = self.recovery.get_current_url()
        self.recovery.click_eye_icon()
        assert self.recovery.is_input_in_focus_visible()
        



