
from selenium.webdriver.common.by import By

class AttractionLocators:

    SEARCH_FIELD = (By.CSS_SELECTOR, 'div.css-1yo1c9c .css-1dgyr43')
    SEARCH_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    MUSEUMS_BTN = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div[4]/label/div')
    FIRST_LINK = (By.CSS_SELECTOR, 'a[title="Admission to Madame Tussauds London"]')
    TITLE_HEADER = (By.CSS_SELECTOR, 'h2.css-1uk1gs8')