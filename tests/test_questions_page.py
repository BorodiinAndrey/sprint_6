import pytest
import allure
from data import data_questions
from locators.questions_page_locators import (
    FirstImportantQuestion, SecondImportantQuestion, ThirdImportantQuestion,
    FourthImportantQuestion, FifthImportantQuestion, SixthImportantQuestion,
    SeventhImportantQuestion, EighthImportantQuestion, Cookies
)


questions_data = [
    pytest.param(
        FirstImportantQuestion.HOW_MUCH_QUESTION,
        FirstImportantQuestion.HOW_MUCH_TEXT,
        data_questions.HOW_MUCH_QUESTION_TEXT,
        'Сколько это стоит? И как оплатить?'
    ),
    pytest.param(
        SecondImportantQuestion.WANT_COUPLE_SCOOTER_QUESTION,
        SecondImportantQuestion.WANT_COUPLE_SCOOTER_TEXT,
        data_questions.WANT_COUPLE_SCOOTER_TEXT,
        'Хочу сразу несколько самокатов! Так можно?'
    ),
    pytest.param(
        ThirdImportantQuestion.RENTAL_TIME_CALCULATED_QUESTION,
        ThirdImportantQuestion.RENTAL_TIME_CALCULATED_TEXT,
        data_questions.RENTAL_TIME_CALCULATED_TEXT,
        'Как рассчитывается время аренды?'
    ),
    pytest.param(
        FourthImportantQuestion.ORDER_SCOOTER_TODAY_QUESTION,
        FourthImportantQuestion.ORDER_SCOOTER_TODAY_TEXT,
        data_questions.ORDER_SCOOTER_TODAY_TEXT,
        'Можно ли заказать самокат прямо на сегодня?'
    ),
    pytest.param(
        FifthImportantQuestion.EXTEND_ORDER_QUESTION,
        FifthImportantQuestion.EXTEND_ORDER_TEXT,
        data_questions.EXTEND_ORDER_TEXT,
        'Можно ли продлить заказ или вернуть самокат раньше?'
    ),
    pytest.param(
        SixthImportantQuestion.BRING_CHARGER_QUESTION,
        SixthImportantQuestion.BRING_CHARGER_TEXT,
        data_questions.BRING_CHARGER_TEXT,
        'Вы привозите зарядку вместе с самокатом?'
    ),
    pytest.param(
        SeventhImportantQuestion.CANCEL_ORDER_QUESTION,
        SeventhImportantQuestion.CANCEL_ORDER_TEXT,
        data_questions.CANCEL_ORDER_TEXT,
        'Можно ли отменить заказ?'
    ),
    pytest.param(
        EighthImportantQuestion.MKAD_QUESTION,
        EighthImportantQuestion.MKAD_TEXT,
        data_questions.MKAD_TEXT,
        'Я жизу за МКАДом, привезёте?'
    ),
]


@allure.feature('Тесты на блок с важными вопросами')
class TestQuestionsPage:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_text, title", questions_data)
    def test_questions(self, pages, question_locator, answer_locator, expected_text, title):
        allure.dynamic.title(f'Проверка важного вопроса: "{title}"')

        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)

        with allure.step('Скролл к вопросу'):
            pages.questions.scroll_to_element(question_locator)

        with allure.step('Раскрытие вопроса'):
            pages.questions.click_to_element(question_locator)

        with allure.step('Сравнение текста ответа'):
            actual_text = pages.questions.get_text(answer_locator)
            assert actual_text == expected_text
