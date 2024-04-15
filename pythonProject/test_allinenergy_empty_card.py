import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

class TestAmazonCard:
    driver = ''

    def setup_method(self):

        self.driver = webdriver
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('C:\Python_Selenium\pythonProject\chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.get('https://allinenergy.com.ua/')

    def test_allinenergy_empty_card(self):
        self.driver.find_element(By.XPATH, "//a[@class='table-nav__link' and @href='https://allinenergy.com.ua/rozprodazh']").click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@class ='content__header']//h1").text
        expected_text = 'Розпродаж'
        assert actual_text == expected_text, f"error Expected text: '{expected_text}', but actual text: '{actual_text}'"


    def teardown_method(self):
        self.driver.quit()