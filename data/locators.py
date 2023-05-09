from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='search_form_input_homepage']")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search_button_homepage']")
    RESULTS = (By.XPATH, "//*[@id='links']//*[@data-testid='result']")
    LOGIN_INPUT = (By.XPATH, "//*[@id='form3-username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='form3-password']")
    ENTER_BUTTON = (By.XPATH, "//*[@id='main-wrap']//*[@type='submit']")
    USER_TAG = (By.XPATH, "//*[@id='top']//*[@id='user_tag']")
    

