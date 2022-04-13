
from selenium.webdriver.common.by import By


class HomePageLocators:

    SIGN_IN_BTN = (By.XPATH, '//*[@id="b2indexPage"]/header/nav[1]/div[2]/div[6]/a')
    VERIFY_IS_SIGNED_IN = (By.CSS_SELECTOR, 'svg.-streamline-bell_normal')
    ATTRACTIONS_BTN = (By.XPATH, '//*[@id="b2indexPage"]/header/nav[2]/ul/li[4]/a')