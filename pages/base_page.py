from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))


    def fill_form(self, locator, name):
        self.driver.find_element(*locator).send_keys(name)

    def get_current_url(self):
        return self.driver.current_url

    def is_element_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def wait_for_element_to_be_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_invisibility(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait(self):
        self.driver.implicitly_wait(10)
    def wait_until_text_is_not_equal(self, locator, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*locator).text != text
            )
            return True
        except Exception as e:
            return False

    def click_element_via_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)
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