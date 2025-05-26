from data import data_questions
import allure
from locators.questions_page_locators import (
    FirstImportantQuestion, SecondImportantQuestion, ThirdImportantQuestion,
    FourthImportantQuestion, FifthImportantQuestion, SixthImportantQuestion,
    SeventhImportantQuestion, EighthImportantQuestion, Cookies)

@allure.feature('Тесты на блок с важными вопросами')
class TestQuestionsPage:

    @allure.title('Проверка вопроса "Сколько это стоит? И как оплатить?"')
    def test_how_much_question(self, pages):
        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)
        with allure.step('Скрол к первому важному вопросу'):
            pages.questions.scroll_to_element(FirstImportantQuestion.HOW_MUCH_QUESTION)
        with allure.step('Раскрытие первого вопроса'):
            pages.questions.click_to_element(FirstImportantQuestion.HOW_MUCH_QUESTION)

        with allure.step('Сравнение текста первого вопроса'):
            assert data_questions.HOW_MUCH_QUESTION_TEXT == pages.questions.get_text(FirstImportantQuestion.HOW_MUCH_TEXT)

    @allure.title('Проверка вопроса "Хочу сразу несколько самокатов! Так можно?"')
    def test_want_couple_scooter_question(self, pages):
        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)
        with allure.step('Скрол ко второму важному вопросу'):
            pages.questions.scroll_to_element(SecondImportantQuestion.WANT_COUPLE_SCOOTER_QUESTION)
        with allure.step('Раскрытие второго вопроса'):
            pages.questions.click_to_element(SecondImportantQuestion.WANT_COUPLE_SCOOTER_QUESTION)

        with allure.step('Сравнение текста второго вопроса'):
            assert data_questions.WANT_COUPLE_SCOOTER_TEXT == pages.questions.get_text(SecondImportantQuestion.WANT_COUPLE_SCOOTER_TEXT)

    @allure.title('Проверка вопроса "Как рассчитывается время аренды?"')
    def test_rental_time_calculated_question(self, pages):
        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)
        with allure.step('Скрол к третьему важному вопросу'):
            pages.questions.scroll_to_element(ThirdImportantQuestion.RENTAL_TIME_CALCULATED_QUESTION)
        with allure.step('Раскрытие третьего вопроса'):
            pages.questions.click_to_element(ThirdImportantQuestion.RENTAL_TIME_CALCULATED_QUESTION)

        with allure.step('Сравнение текста третьего вопроса'):
            assert data_questions.RENTAL_TIME_CALCULATED_TEXT == pages.questions.get_text(ThirdImportantQuestion.RENTAL_TIME_CALCULATED_TEXT)

    @allure.title('Проверка вопроса "Можно ли заказать самокат прямо на сегодня?"')
    def test_order_scooter_today_question(self, pages):
        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)
        with allure.step('Скрол к четвертому важному вопросу'):
            pages.questions.scroll_to_element(FourthImportantQuestion.ORDER_SCOOTER_TODAY_QUESTION)
        with allure.step('Раскрытие четвертого вопроса'):
            pages.questions.click_to_element(FourthImportantQuestion.ORDER_SCOOTER_TODAY_QUESTION)

        with allure.step('Сравнение текста четвертого вопроса'):
            assert data_questions.ORDER_SCOOTER_TODAY_TEXT == pages.questions.get_text(FourthImportantQuestion.ORDER_SCOOTER_TODAY_TEXT)

    @allure.title('Проверка вопроса "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_extend_order_question(self, pages):
        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)
        with allure.step('Скрол к пятому важному вопросу'):
            pages.questions.scroll_to_element(FifthImportantQuestion.EXTEND_ORDER_QUESTION)
        with allure.step('Раскрытие пятого вопроса'):
            pages.questions.click_to_element(FifthImportantQuestion.EXTEND_ORDER_QUESTION)

        with allure.step('Сравнение текста пятого вопроса'):
            assert data_questions.EXTEND_ORDER_TEXT == pages.questions.get_text(FifthImportantQuestion.EXTEND_ORDER_TEXT)

    @allure.title('Проверка вопроса "Вы привозите зарядку вместе с самокатом?"')
    def test_bring_charger_question(self, pages):
        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)
        with allure.step('Скрол к шестому важному вопросу'):
            pages.questions.scroll_to_element(SixthImportantQuestion.BRING_CHARGER_QUESTION)
        with allure.step('Раскрытие шестого вопроса'):
            pages.questions.click_to_element(SixthImportantQuestion.BRING_CHARGER_QUESTION)

        with allure.step('Сравнение текста шестого вопроса'):
            assert data_questions.BRING_CHARGER_TEXT == pages.questions.get_text(SixthImportantQuestion.BRING_CHARGER_TEXT)

    @allure.title('Проверка вопроса "Можно ли отменить заказ?"')
    def test_cancel_order_question(self, pages):
        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)
        with allure.step('Скрол к седьмому важному вопросу'):
            pages.questions.scroll_to_element(SeventhImportantQuestion.CANCEL_ORDER_QUESTION)
        with allure.step('Раскрытие седьмого вопроса'):
            pages.questions.click_to_element(SeventhImportantQuestion.CANCEL_ORDER_QUESTION)

        with allure.step('Сравнение текста седьмого вопроса'):
            assert data_questions.CANCEL_ORDER_TEXT == pages.questions.get_text(SeventhImportantQuestion.CANCEL_ORDER_TEXT)

    @allure.title('Проверка вопроса "Я жизу за МКАДом, привезёте?"')
    def test_mkad_question(self, pages):
        with allure.step('Тап на кнопку принятия cookie'):
            pages.questions.click_to_element(Cookies.cookies_button)
        with allure.step('Скрол к восьмому важному вопросу'):
            pages.questions.scroll_to_element(EighthImportantQuestion.MKAD_QUESTION)
        with allure.step('Раскрытие восьмого вопроса'):
            pages.questions.click_to_element(EighthImportantQuestion.MKAD_QUESTION)

        with allure.step('Сравнение текста восьмого вопроса'):
            assert data_questions.MKAD_TEXT == pages.questions.get_text(EighthImportantQuestion.MKAD_TEXT)
