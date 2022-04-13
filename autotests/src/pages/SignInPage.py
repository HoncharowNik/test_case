import time

from autotests.src.pages.locators.SignInPageLocators import SignInLocators
from autotests.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.action_chains import ActionChains


class SignInPage(SignInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)



    def input_email(self,email):
        email = email if email else 'hijilo4322@hhmel.com'

        self.sl.wait_and_input_text(self.EMAIL, email)

    def click_cuntinue_btn(self):
        self.sl.wait_and_click(self.CONTINUE_BTN)

    def input_password(self, password):
        password = password if password else 'Qwerty1234'

        self.sl.wait_and_input_text(self.PASSWORD, password)

    def click_sign_in_btn(self):
        self.sl.wait_and_click(self.CONTINUE_BTN)


    def name_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.NAME_ERROR_MSG, exp_err)

    def password_error_is_displayed(self, expected_err):
        self.sl.wait_until_element_contains_text(self.PASSWORD_ERROR_MSG, expected_err)

    def sign_in(self, email=None, password=None):
        self.input_email(email=email)
        self.click_cuntinue_btn()
        self.input_password(password=password)
        self.click_sign_in_btn()



