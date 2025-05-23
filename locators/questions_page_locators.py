from selenium.webdriver.common.by import By


class FirstImportantQuestion:
    HOW_MUCH_QUESTION = [By.ID, 'accordion__heading-0']
    HOW_MUCH_TEXT = [By.ID, 'accordion__panel-0']


class SecondImportantQuestion:
    WANT_COUPLE_SCOOTER_QUESTION = [By.ID, 'accordion__heading-1']
    WANT_COUPLE_SCOOTER_TEXT = [By.ID, 'accordion__panel-1']


class ThirdImportantQuestion:
    RENTAL_TIME_CALCULATED_QUESTION = [By.ID, 'accordion__heading-2']
    RENTAL_TIME_CALCULATED_TEXT = [By.ID, 'accordion__panel-2']


class FourthImportantQuestion:
    ORDER_SCOOTER_TODAY_QUESTION = [By.ID, 'accordion__heading-3']
    ORDER_SCOOTER_TODAY_TEXT = [By.ID, 'accordion__panel-3']


class FifthImportantQuestion:
    EXTEND_ORDER_QUESTION = [By.ID, 'accordion__heading-4']
    EXTEND_ORDER_TEXT = [By.ID, 'accordion__panel-4']


class SixthImportantQuestion:
    BRING_CHARGER_QUESTION = [By.ID, 'accordion__heading-5']
    BRING_CHARGER_TEXT = [By.ID, 'accordion__panel-5']


class SeventhImportantQuestion:
    CANCEL_ORDER_QUESTION = [By.ID, 'accordion__heading-6']
    CANCEL_ORDER_TEXT = [By.ID, 'accordion__panel-6']


class EighthImportantQuestion:
    MKAD_QUESTION = [By.ID, 'accordion__heading-7']
    MKAD_TEXT = [By.ID, 'accordion__panel-7']

class Cookies:
    cookies_button = [By.CLASS_NAME, 'App_CookieButton__3cvqF']
