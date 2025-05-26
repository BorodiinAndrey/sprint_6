from page.base_page import BasePage

class QuestionsPage(BasePage):

    def scroll_to_element(self, locator, position='end'):
        super().scroll_to_element(locator, position)