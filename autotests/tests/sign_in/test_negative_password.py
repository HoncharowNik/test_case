
import pytest
from autotests.src.pages.HomePage import HomePage
from autotests.src.pages.SignInPage import SignInPage

@pytest.mark.usefixtures('init_driver')
class TestNegative:

    @pytest.mark.id3
    def test_negative_name(self):

        home_page = HomePage(self.driver)
        home_page.homepage()
        home_page.click_sign_in_btn()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.input_email('hijilo4322@hhmel.com')
        sign_in_page.click_cuntinue_btn()
        sign_in_page.input_password('впыhhdfhsfgчапd')
        sign_in_page.click_sign_in_btn()
        expected_err = "The email and password combination you entered doesn't match"
        sign_in_page.password_error_is_displayed(expected_err)