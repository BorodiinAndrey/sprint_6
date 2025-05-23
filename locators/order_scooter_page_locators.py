from selenium.webdriver.common.by import By

class HeaderOrderButton:
    ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Header_Nav__AGCXC")]//button[contains(@class, "Button_Button__ra12g")]']
    NAME_LOCATOR = [By.XPATH, '//*[@placeholder="* Имя"]']
    LAST_NAME_LOCATOR = [By.XPATH, '//*[@placeholder="* Фамилия"]']
    ADDRESS_LOCATOR = [By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]']
    SUBWAY_STATION_LOCATOR = [By.XPATH, '//*[@placeholder="* Станция метро"]']
    CHOOSE_STATION_LOCATOR = [By.XPATH, "//*[@class='select-search__row' and @data-index='0']"]
    PHONE_LOCATOR = [By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, "//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Далее']"]

class CenterOrderButton:
    ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]"]
    NAME_LOCATOR = [By.XPATH, '//*[@placeholder="* Имя"]']
    LAST_NAME_LOCATOR = [By.XPATH, '//*[@placeholder="* Фамилия"]']
    ADDRESS_LOCATOR = [By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]']
    SUBWAY_STATION_LOCATOR = [By.XPATH, '//*[@placeholder="* Станция метро"]']
    CHOOSE_STATION_LOCATOR = [By.XPATH, "//*[@class='select-search__row' and @data-index='1']"]
    PHONE_LOCATOR = [By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, "//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Далее']"]