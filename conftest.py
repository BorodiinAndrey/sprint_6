import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from page.order_scooter_page import OrderScooterPage
from page.questions_page import QuestionsPage

class Pages:
    def __init__(self, driver):
        self.order_scooter = OrderScooterPage(driver)
        self.questions = QuestionsPage(driver)


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("window-size=2560, 1440")
    driver = webdriver.Firefox(options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture()
def pages(driver):
    return Pages(driver)
