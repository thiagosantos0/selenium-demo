# coding=utf-8
import time
import pytest
from pages.search_page import SearchPage
from tests.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC


class TestSearch(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = SearchPage(self.driver, self.wait, "https://duckduckgo.com/")
        time.sleep(2)
        self.page.go_to_search_page()
        time.sleep(2)

    def test_title(self, load_pages):
        time.sleep(2)
        self.page.check_title("DuckDuckGo — Privacidade simplificada.")
        time.sleep(2)

    def test_search(self, load_pages):
        time.sleep(2)
        self.page.make_a_search("Selenium")
        time.sleep(2)

    def test_login(self, load_pages):

        f=open("./account.txt","r")
        lines=f.readlines()
        login=lines[0]
        password=lines[1]
        f.close()

        
        self.page = SearchPage(self.driver, self.wait, "https://lichess.org/login")
        time.sleep(2)
        self.page.go_to_search_page()
        time.sleep(2)

        

        time.sleep(2)
        self.driver.find_element(*self.page.locator.LOGIN_INPUT).send_keys(login)
        self.driver.find_element(*self.page.locator.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.page.locator.ENTER_BUTTON).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.page.locator.USER_TAG))


        
