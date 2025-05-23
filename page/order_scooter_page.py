from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderScooterPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_to_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_order_scooter(self, locators_class, name, last_name, address, phone, data):
        self.click_to_element(locators_class.ORDER_BUTTON)
        self.input_text(locators_class.NAME_LOCATOR, name)
        self.input_text(locators_class.LAST_NAME_LOCATOR, last_name)
        self.input_text(locators_class.ADDRESS_LOCATOR, address)
        self.click_to_element(locators_class.SUBWAY_STATION_LOCATOR)
        self.click_to_element(locators_class.CHOOSE_STATION_LOCATOR)
        self.input_text(locators_class.PHONE_LOCATOR, phone)
        self.click_to_element(locators_class.NEXT_BUTTON)
        self.input_text(locators_class.DATA_LOCATOR, data)
        self.click_to_element(locators_class.CLICK_LOCATOR)
        self.click_to_element(locators_class.RENTAL_PERIOD_LOCATOR)
        self.click_to_element(locators_class.TIME_LOCATOR)
