
from autotests.src.pages.locators.AttractionLocatoors import AttractionLocators
from autotests.src.SeleniumExtended import SeleniumExtended

class AttractionPage(AttractionLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_search_request(self, text):
        text = text if text else 'travel'

        self.sl.wait_and_input_text(self.SEARCH_FIELD, text)

    def click_search_btn(self):
        self.sl.wait_and_click_timeout(self.SEARCH_BTN)

    def click_to_museums_btn(self):
        self.sl.wait_and_click_timeout(self.MUSEUMS_BTN)

    def click_to_first_link(self):
        self.sl.wait_and_click(self.FIRST_LINK)

    def verify_title_text(self, expexted_err):
        self.sl.wait_until_element_contains_text(self.TITLE_HEADER, expexted_err)