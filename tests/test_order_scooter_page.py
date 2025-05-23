import pytest
import allure
from data.data_order_scooter import FirstDataSet, SecondDataSet
from locators.order_scooter_page_locators import HeaderOrderButton, CenterOrderButton


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
