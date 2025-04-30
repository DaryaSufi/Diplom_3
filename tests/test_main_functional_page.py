import allure
from pages.main_functional_page import MainFunctionalPage
class TestMainFunctionalPage:
    @allure.title("Проверка перехода по клику на Конструктор")
    def test_click_through_to_constructor(self, driver):
        self.recovery = MainFunctionalPage(driver)
        self.recovery.open()
        self.recovery.click_on_order_feed()
        self.recovery.click_on_constructor()
        assert self.recovery.is_collect_burger_inscription_visible()

    @allure.title("Проверка перехода по клику на ленту заказов")
    def test_click_through_to_order_feed(self, driver):
        self.recovery = MainFunctionalPage(driver)
        self.recovery.open()
        self.recovery.click_on_order_feed()
        assert self.recovery.is_order_feed_inscription_visible()

    @allure.title("Проверка появления окна с деталями при клике на ингридиент")
    def test_appear_window_with_ingridients_details(self, driver):
        self.recovery = MainFunctionalPage(driver)
        self.recovery.open()
        self.recovery.open_ingredient_window()
        assert self.recovery.is_ingridient_card_visible()

    @allure.title("Проверка закрытия окна с деталями при клике на крестик")
    def test_closing_details_window_by_clicking_on_the_cross(self, driver):
        self.recovery = MainFunctionalPage(driver)
        self.recovery.open()
        self.recovery.open_ingredient_window()
        self.recovery.close_ingredient_window()
        assert self.recovery.is_ingridient_visible()

    @allure.title("Проверка увеличения каунтера ингридиента, при добавлении его в заказ")
    def test_increase_counter_of_ingredient_when_adding_it_to_order(self, driver):
        self.recovery = MainFunctionalPage(driver)
        self.recovery.open()
        self.recovery.adding_ingredients_to_order()
        assert self.recovery.is_changed_counter_visible()

    @allure.title("Проверка возможности оформления заказа авторизованным пользователем")
    def test_possibility_of_placing_an_order_by_authorized_user(self, driver, create_and_delete_user_for_login):
        self.recovery = MainFunctionalPage(driver)
        self.recovery.open()
        self.recovery.open_personal_account()
        self.recovery.create_user_and_autorization(create_and_delete_user_for_login)
        self.recovery.adding_ingredients_to_order()
        self.recovery.adding_sauce_to_order()
        self.recovery.adding_filling_to_order()
        self.recovery.click_chekout_button()
        assert self.recovery.is_orders_id_visible()










