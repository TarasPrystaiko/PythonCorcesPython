import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

class TestAmazon:
    search_words = ("Schneider", "Legrand", "Lemanso", "Lezard")

    driver = ''

    def setup_method(self):

        self.driver = webdriver
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('C:\Python_Selenium\pythonProject\chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.get('https://allinenergy.com.ua/')


    @pytest.mark.parametrize('search_query', search_words)
    def test_amazon_search(self, search_query):
      search = self.driver.find_elements(By.NAME, "text")
      search[0].send_keys(search_query,Keys.ENTER)

      expected_text = f'\'{search_query}\''
      actual_text = self.driver.find_element(By.XPATH, "//q[@class='content__quote']").text
      # assert expected_text == actual_text, f'error Expected text: {expected_text}, but actual text: {actual_text}'


    def teardown_method(self):
     self.driver.quit()