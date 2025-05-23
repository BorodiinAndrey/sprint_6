import data
from locators.questions_page_locators import (
    FirstImportantQuestion, SecondImportantQuestion, ThirdImportantQuestion,
    FourthImportantQuestion, FifthImportantQuestion, SixthImportantQuestion,
    SeventhImportantQuestion, EighthImportantQuestion, Cookies)


class TestQuestionsPage:

    def test_how_much_question(self, pages):
        pages.questions.click_to_element(Cookies.cookies_button)
        pages.questions.scroll_to_element(FirstImportantQuestion.HOW_MUCH_QUESTION)
        pages.questions.click_to_element(FirstImportantQuestion.HOW_MUCH_QUESTION)

        assert data.how_much_question_text == pages.questions.get_text(FirstImportantQuestion.HOW_MUCH_TEXT)

    def test_want_couple_scooter_question(self, pages):
        pages.questions.click_to_element(Cookies.cookies_button)
        pages.questions.scroll_to_element(SecondImportantQuestion.WANT_COUPLE_SCOOTER_QUESTION)
        pages.questions.click_to_element(SecondImportantQuestion.WANT_COUPLE_SCOOTER_QUESTION)

        assert data.want_couple_scooter_text == pages.questions.get_text(SecondImportantQuestion.WANT_COUPLE_SCOOTER_TEXT)

    def test_rental_time_calculated_question(self, pages):
        pages.questions.click_to_element(Cookies.cookies_button)
        pages.questions.scroll_to_element(ThirdImportantQuestion.RENTAL_TIME_CALCULATED_QUESTION)
        pages.questions.click_to_element(ThirdImportantQuestion.RENTAL_TIME_CALCULATED_QUESTION)

        assert data.rental_time_calculated_text == pages.questions.get_text(ThirdImportantQuestion.RENTAL_TIME_CALCULATED_TEXT)

    def test_order_scooter_today_question(self, pages):
        pages.questions.click_to_element(Cookies.cookies_button)
        pages.questions.scroll_to_element(FourthImportantQuestion.ORDER_SCOOTER_TODAY_QUESTION)
        pages.questions.click_to_element(FourthImportantQuestion.ORDER_SCOOTER_TODAY_QUESTION)

        assert data.order_scooter_today_text == pages.questions.get_text(FourthImportantQuestion.ORDER_SCOOTER_TODAY_TEXT)

    def test_extend_order_question(self, pages):
        pages.questions.click_to_element(Cookies.cookies_button)
        pages.questions.scroll_to_element(FifthImportantQuestion.EXTEND_ORDER_QUESTION)
        pages.questions.click_to_element(FifthImportantQuestion.EXTEND_ORDER_QUESTION)

        assert data.extend_order_text == pages.questions.get_text(FifthImportantQuestion.EXTEND_ORDER_TEXT)

    def test_bring_charger_question(self, pages):
        pages.questions.click_to_element(Cookies.cookies_button)
        pages.questions.scroll_to_element(SixthImportantQuestion.BRING_CHARGER_QUESTION)
        pages.questions.click_to_element(SixthImportantQuestion.BRING_CHARGER_QUESTION)

        assert data.bring_charger_text == pages.questions.get_text(SixthImportantQuestion.BRING_CHARGER_TEXT)

    def test_cancel_order_question(self, pages):
        pages.questions.click_to_element(Cookies.cookies_button)
        pages.questions.scroll_to_element(SeventhImportantQuestion.CANCEL_ORDER_QUESTION)
        pages.questions.click_to_element(SeventhImportantQuestion.CANCEL_ORDER_QUESTION)

        assert data.cancel_order_text == pages.questions.get_text(SeventhImportantQuestion.CANCEL_ORDER_TEXT)

    def test_mkad_question(self, pages):
        pages.questions.click_to_element(Cookies.cookies_button)
        pages.questions.scroll_to_element(EighthImportantQuestion.MKAD_QUESTION)
        pages.questions.click_to_element(EighthImportantQuestion.MKAD_QUESTION)

        assert data.mkad_text == pages.questions.get_text(EighthImportantQuestion.MKAD_TEXT)
