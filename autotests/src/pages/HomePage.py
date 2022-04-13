
from autotests.src.pages.locators.HomePageLocators import HomePageLocators
from autotests.src.helpers.config_helpers import get_base_url
from autotests.src.SeleniumExtended import SeleniumExtended

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def homepage(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_sign_in_btn(self):
        self.sl.wait_and_click(self.SIGN_IN_BTN)

    def click_on_attractions_btn(self):
        self.sl.wait_and_click(self.ATTRACTIONS_BTN)

    def verify(self):
        self.sl.wait_until_element_is_visible(self.VERIFY_IS_SIGNED_IN)