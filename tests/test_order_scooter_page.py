import pytest
import allure
from data.data_order_scooter import FirstDataSet, SecondDataSet
from locators.order_scooter_page_locators import HeaderOrderButton, CenterOrderButton


@pytest.mark.parametrize("data_set", [FirstDataSet, SecondDataSet])
def test_order_scooter_from_header(pages, data_set):
    pages.order_scooter.get_order_scooter(
        locators_class=HeaderOrderButton,
        name=data_set.name,
        last_name=data_set.last_name,
        address=data_set.address,
        phone=data_set.phone
    )


@pytest.mark.parametrize("data_set", [FirstDataSet, SecondDataSet])
def test_order_scooter_from_center(pages, data_set):
    pages.order_scooter.scroll_to_element(CenterOrderButton.ORDER_BUTTON)
    pages.order_scooter.get_order_scooter(
        locators_class=CenterOrderButton,
        name=data_set.name,
        last_name=data_set.last_name,
        address=data_set.address,
        phone=data_set.phone
    )
