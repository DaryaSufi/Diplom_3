from selenium.webdriver.common.by import By
class PasswordRecoveryPageLocators:
    personal_account_button = (By.LINK_TEXT, "Личный Кабинет")
    button_password_recovery = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']")
    input_email_for_pass_recov = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    button_recovery = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    eye_icon = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    input_in_focus = (By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default input__placeholder-focused']")
