from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    def go_to_site(self):
        self.driver.get(Constants.URL)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((locator)))

    def fill_form(self, locator, name):
        self.driver.find_element(*locator).send_keys(name)

    def get_current_url(self):
        return self.driver.current_url

    def is_element_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False
