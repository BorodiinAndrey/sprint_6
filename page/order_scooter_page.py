from page.base_page import BasePage

class OrderScooterPage(BasePage):

    def switch_to_second_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_link(self):
        return self.driver.current_url

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
        self.click_to_element(locators_class.FINAL_ORDER_BUTTON_LOCATOR)
        self.click_to_element(locators_class.YES_BUTTON_LOCATOR)
