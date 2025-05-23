from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class OrderScooterPage:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.wait_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
