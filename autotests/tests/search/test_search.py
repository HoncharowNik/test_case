
import pytest
from autotests.src.pages.HomePage import HomePage
from autotests.src.pages.AppractionPage import AttractionPage
import time

@pytest.mark.usefixtures('init_driver')
class TestSearch:

    @pytest.mark.id4
    def test_search(self):

        home_page = HomePage(self.driver)
        home_page.homepage()
        home_page.click_on_attractions_btn()

        search_p = AttractionPage(self.driver)
        search_p.input_search_request('travel')
        time.sleep(2)
        search_p.click_search_btn()
        search_p.click_to_museums_btn()
        search_p.click_to_first_link()
        header_text = 'Admission to Madame Tussauds London'
        search_p.verify_title_text(header_text)