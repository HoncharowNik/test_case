import pytest
from selenium import webdriver




@pytest.fixture(scope="class")
def init_driver(request):


    driver = webdriver.Chrome()

    # driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()

