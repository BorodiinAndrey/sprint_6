import pytest
from selenium.webdriver.support import expected_conditions as EC
import allure
from data.data_order_scooter import FirstDataSet, SecondDataSet, Text
from locators.order_scooter_page_locators import HeaderOrderButton, CenterOrderButton, BaseOrderLocators


@allure.feature("Тесты на заказ скутера")
class TestOrderScooterPage:

    @allure.title("Проверка заказа по кнопке 'Заказать' в хедере")
    @pytest.mark.parametrize("data_set", [FirstDataSet, SecondDataSet])
    def test_order_scooter_from_header(self, pages, data_set):
        with allure.step("Осуществление заказа"):
            pages.order_scooter.get_order_scooter(
                locators_class=HeaderOrderButton,
                name=data_set.name,
                last_name=data_set.last_name,
                address=data_set.address,
                phone=data_set.phone,
                data=data_set.data
            )

        with allure.step("Проверка получения текста 'Заказ оформлен'"):
            assert Text.order_text in pages.order_scooter.get_text(BaseOrderLocators.GET_ORDER_TEXT_LOCATOR)

        with allure.step("Тап на кнопку 'Посмотреть заказ'"):
            pages.order_scooter.click_to_element(BaseOrderLocators.LOOK_ORDER_LOCATOR)
        with allure.step("Тап на лого самоката"):
            pages.order_scooter.click_to_element(BaseOrderLocators.SCOOTER_LOGO_LOCATOR)

        with allure.step("Проверка что произошел переход на главную страницу"):
            assert Text.main_page_text in pages.order_scooter.get_text(BaseOrderLocators.MAIN_TEXT_LOCATOR)

        with allure.step("Тап по логотипу 'Яндекс'"):
            pages.order_scooter.click_to_element(BaseOrderLocators.YANDEX_LOGO_LOCATOR)
        with allure.step("Переключение на следующую вкладку браузера"):
            pages.order_scooter.switch_to_second_tab()

        with allure.step("Проверка, что произошел редирект на страницу Яндекс"):
            pages.order_scooter.wait.until(EC.url_contains(Text.yandex_link))
            assert Text.yandex_link in pages.order_scooter.get_current_link()

    @allure.title("Проверка заказа по кнопке 'Заказать' по центру экрана")
    @pytest.mark.parametrize("data_set", [FirstDataSet, SecondDataSet])
    def test_order_scooter_from_center(self, pages, data_set):
        with allure.step("Скрол к кнопке 'Заказать'"):
            pages.order_scooter.scroll_to_element(CenterOrderButton.ORDER_BUTTON)
        with allure.step("Осуществление заказа"):
            pages.order_scooter.get_order_scooter(
                locators_class=CenterOrderButton,
                name=data_set.name,
                last_name=data_set.last_name,
                address=data_set.address,
                phone=data_set.phone,
                data=data_set.data
            )

        with allure.step("Проверка получения текста 'Заказ оформлен'"):
            assert Text.order_text in pages.order_scooter.get_text(BaseOrderLocators.GET_ORDER_TEXT_LOCATOR)

        with allure.step("Тап на кнопку 'Посмотреть заказ'"):
            pages.order_scooter.click_to_element(BaseOrderLocators.LOOK_ORDER_LOCATOR)
        with allure.step("Тап на лого самоката"):
            pages.order_scooter.click_to_element(BaseOrderLocators.SCOOTER_LOGO_LOCATOR)

        with allure.step("Проверка что произошел переход на главную страницу"):
            assert Text.main_page_text in pages.order_scooter.get_text(BaseOrderLocators.MAIN_TEXT_LOCATOR)

        with allure.step("Тап по логотипу 'Яндекс'"):
            pages.order_scooter.click_to_element(BaseOrderLocators.YANDEX_LOGO_LOCATOR)
        with allure.step("Переключение на следующую вкладку браузера"):
            pages.order_scooter.switch_to_second_tab()

        with allure.step("Проверка, что произошел редирект на страницу Яндекс"):
            pages.order_scooter.wait.until(EC.url_contains(Text.yandex_link))
            assert Text.yandex_link in pages.order_scooter.get_current_link()
