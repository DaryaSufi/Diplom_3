from selenium.webdriver.common.by import By
class PersonalAccountPageLocators:
    input_email_entrance = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text']")
    input_password_entrance = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password']")
    entrance_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    history_orders_button = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    button_exit = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    sign_entrance = (By.XPATH, "//h2")