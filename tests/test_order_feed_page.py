import allure
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_page_locators import OrderFeedPageLocators
class TestOrderFeedPage:
    @allure.title("Проверка открытияя окна с деталями о заказе, при клике на закал в ленте заказов ")
    def test_popup_window_with_ored_details(self, driver):
        self.recovery = OrderFeedPage(driver)
        self.recovery.go_to_site()
        self.recovery.open_order_feed()
        self.recovery.click_order()
        assert self.recovery.is_element_visible(OrderFeedPageLocators.order_info)

    @allure.title("Проверка появления заказа пользователя на странице «Лента заказов»")
    def test_appearance_users_order_from_order_history_on_the_order_feed_page(self, driver, create_and_delete_user_for_login):
        self.recovery = OrderFeedPage(driver)
        self.recovery.go_to_site()
        self.recovery.open_personal_account()
        self.recovery.create_user_and_autorization(create_and_delete_user_for_login)
        order_number = self.recovery.making_an_order()
        self.recovery.go_to_site()
        self.recovery.open_order_feed()
        order_numbers = self.recovery.get_list_order_numbers()
        assert order_number in order_numbers

    @allure.title("Проверка увеличения счетчика Выполнено за все время при создании нового заказа")
    def test_counter_was_completed_entire_time_when_creating_a_new_order(self, driver,create_and_delete_user_for_login):
        self.recovery = OrderFeedPage(driver)
        self.recovery.go_to_site()
        self.recovery.open_personal_account()
        self.recovery.create_user_and_autorization(create_and_delete_user_for_login)
        self.recovery.open_order_feed()
        number_of_orders = self.recovery.get_the_number_of_orders_for_all_time()
        self.recovery.click_button_constructor()
        self.recovery.making_an_order()
        self.recovery.go_to_site()
        self.recovery.open_order_feed()
        new_number_of_orders = self.recovery.get_the_number_of_orders_for_all_time()
        assert new_number_of_orders > number_of_orders

    @allure.title("Проверка увеличения счетчика Выполнено за сегодня при создании нового заказа")
    def test_counter_was_completed_today_when_creating_a_new_order(self, driver, create_and_delete_user_for_login):
        self.recovery = OrderFeedPage(driver)
        self.recovery.go_to_site()
        self.recovery.open_personal_account()
        self.recovery.create_user_and_autorization(create_and_delete_user_for_login)
        self.recovery.open_order_feed()
        number_of_orders = self.recovery.get_the_number_of_orders_for_today()
        self.recovery.click_button_constructor()
        self.recovery.making_an_order()
        self.recovery.go_to_site()
        self.recovery.open_order_feed()
        new_number_of_orders = self.recovery.get_the_number_of_orders_for_today()
        assert new_number_of_orders > number_of_orders

    @allure.title("Проверка появления номера заказа в списке В работе после его оформления")
    def test_order_number_appears_in_the_work_list_after_it_is_completed(self, driver, create_and_delete_user_for_login):
        self.recovery = OrderFeedPage(driver)
        self.recovery.go_to_site()
        self.recovery.open_personal_account()
        self.recovery.create_user_and_autorization(create_and_delete_user_for_login)
        order_number = self.recovery.making_an_mini_order()
        self.recovery.go_to_site()
        self.recovery.open_order_feed()
        order_numbers = self.recovery.get_list_order_numbers_in_work()
        assert order_number in order_numbers








