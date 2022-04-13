
import pytest
from autotests.src.pages.HomePage import HomePage
from autotests.src.pages.SignInPage import SignInPage

@pytest.mark.usefixtures('init_driver')
class TestNegative:

    @pytest.mark.id2
    def test_negative_name(self):

        home_page = HomePage(self.driver)
        home_page.homepage()
        home_page.click_sign_in_btn()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.input_email('rasfasvvssafasfasfas')
        sign_in_page.click_cuntinue_btn()
        expected_err = "Please check if the email address you've entered is correct."
        sign_in_page.name_error_is_displayed(expected_err)