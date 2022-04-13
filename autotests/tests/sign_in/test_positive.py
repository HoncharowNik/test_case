
import pytest
from autotests.src.pages.HomePage import HomePage
from autotests.src.pages.SignInPage import SignInPage


@pytest.mark.usefixtures('init_driver')
class TestPositiveSingIn:

    @pytest.mark.id1
    def test_positive_sign_in(self):

        home_page = HomePage(self.driver)
        home_page.homepage()
        home_page.click_sign_in_btn()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.sign_in()

        home_page.verify()
