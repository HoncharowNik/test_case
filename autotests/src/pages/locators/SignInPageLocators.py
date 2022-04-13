
from selenium.webdriver.common.by import By


class SignInLocators:

    EMAIL = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')

    NAME_ERROR_MSG = (By.ID, 'username-note')
    PASSWORD_ERROR_MSG = (By.ID, 'password-note')

    PRESS_AND_HOLD_BTN = (By.ID, 'AsvOYtROEvnFRBE')

