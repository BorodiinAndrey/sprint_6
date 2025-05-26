import pytest
from typing import Type
from selenium.webdriver.support import expected_conditions as EC
import allure
from data.data_order_scooter import FirstDataSet, SecondDataSet, Text
from locators.order_scooter_page_locators import HeaderOrderButton, CenterOrderButton, BaseOrderLocators


@allure.feature("Тесты на заказ скутера")
class TestOrderScooterPage:

    @allure.title("Проверка заказа самоката через разные кнопки и данные")
    @pytest.mark.parametrize(
        "locators_class, data_set, scroll",
        [
            pytest.param(HeaderOrderButton, FirstDataSet, False, id="header_first"),
            pytest.param(CenterOrderButton, SecondDataSet, True, id="center_second"),
        ]
    )
    def test_order_scooter(self, pages, locators_class: Type[BaseOrderLocators], data_set: Type[FirstDataSet], scroll):
        if scroll:
            with allure.step("Скрол к кнопке 'Заказать'"):
                pages.order_scooter.scroll_to_element(locators_class.ORDER_BUTTON)

        with allure.step("Осуществление заказа"):
            pages.order_scooter.get_order_scooter(
                locators_class=locators_class,
                name=data_set.NAME,
                last_name=data_set.LAST_NAME,
                address=data_set.ADDRESS,
                phone=data_set.PHONE,
                data=data_set.DATA
            )

        with allure.step("Проверка получения текста 'Заказ оформлен'"):
            assert Text.ORDER_TEXT in pages.order_scooter.get_text(locators_class.GET_ORDER_TEXT_LOCATOR)

        with allure.step("Тап на кнопку 'Посмотреть заказ'"):
            pages.order_scooter.click_to_element(locators_class.LOOK_ORDER_LOCATOR)

        with allure.step("Тап на лого самоката"):
            pages.order_scooter.click_to_element(locators_class.SCOOTER_LOGO_LOCATOR)

        with allure.step("Проверка что произошел переход на главную страницу"):
            assert Text.MAIN_PAGE_TEXT in pages.order_scooter.get_text(locators_class.MAIN_TEXT_LOCATOR)

        with allure.step("Тап по логотипу 'Яндекс'"):
            pages.order_scooter.click_to_element(locators_class.YANDEX_LOGO_LOCATOR)

        with allure.step("Переключение на следующую вкладку браузера"):
            pages.order_scooter.switch_to_second_tab()

        with allure.step("Проверка, что произошел редирект на страницу Яндекс"):
            pages.order_scooter.wait.until(EC.url_contains(Text.YANDEX_LINK))
            assert Text.YANDEX_LINK in pages.order_scooter.get_current_link()
