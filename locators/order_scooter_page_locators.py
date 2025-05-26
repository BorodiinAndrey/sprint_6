from selenium.webdriver.common.by import By


class BaseOrderLocators:
    NAME_LOCATOR = [By.XPATH, '//*[@placeholder="* Имя"]']
    LAST_NAME_LOCATOR = [By.XPATH, '//*[@placeholder="* Фамилия"]']
    ADDRESS_LOCATOR = [By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]']
    SUBWAY_STATION_LOCATOR = [By.XPATH, '//*[@placeholder="* Станция метро"]']
    PHONE_LOCATOR = [By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, "//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Далее']"]
    DATA_LOCATOR = [By.XPATH, '//*[@placeholder="* Когда привезти самокат"]']
    CLICK_LOCATOR = [By.CLASS_NAME, 'Order_Header__BZXOb']
    RENTAL_PERIOD_LOCATOR = [By.CLASS_NAME, 'Dropdown-placeholder']
    FINAL_ORDER_BUTTON_LOCATOR = [By.XPATH, "//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and normalize-space(text())='Заказать']"]
    YES_BUTTON_LOCATOR = [By.XPATH, "//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and normalize-space(text())='Да']"]
    GET_ORDER_TEXT_LOCATOR = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
    LOOK_ORDER_LOCATOR = [By.XPATH, "//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and normalize-space(text())='Посмотреть статус']"]
    SCOOTER_LOGO_LOCATOR = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    MAIN_TEXT_LOCATOR = [By.CLASS_NAME, "Home_Header__iJKdX"]
    YANDEX_LOGO_LOCATOR = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    YANDEX_ELEMENT_LOCATOR = [By.XPATH, "//*[contains(@class, 'arrow__button') and normalize-space(text())='Найти']"]


class HeaderOrderButton(BaseOrderLocators):
    ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Header_Nav__AGCXC")]//button[contains(@class, "Button_Button__ra12g")]']
    CHOOSE_STATION_LOCATOR = [By.XPATH, "//*[@class='select-search__row' and @data-index='0']"]
    TIME_LOCATOR = [By.XPATH, "//*[@class='Dropdown-option' and @aria-selected='false' and normalize-space(text())='сутки']"]


class CenterOrderButton(BaseOrderLocators):
    ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]"]
    CHOOSE_STATION_LOCATOR = [By.XPATH, "//*[@class='select-search__row' and @data-index='1']"]
    TIME_LOCATOR = [By.XPATH, "//*[@class='Dropdown-option' and @aria-selected='false' and normalize-space(text())='двое суток']"]
