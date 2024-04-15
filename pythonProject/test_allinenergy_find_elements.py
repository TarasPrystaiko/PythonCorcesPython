from selenium import webdriver
from selenium.webdriver.common.by import By

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


    def test_allinenergy_find_elements(self):
        self.driver.find_element(By.XPATH, "//span[@class='table-nav__link-image']/img[contains(@src,'/uploads/icons/icon3.png')]").click()
        actual_links = self.driver.find_elements(By.XPATH, "//div[@class='row row--ib row--ib row--vindent-m']/div[@class='col-xs-6 col-sm-4 col-md-4 col-lg-3']")
        assert len(actual_links) == 9, f'Expected to see 9 links, got {len(actual_links)}'

    def teardown_method(self):
        self.driver.quit()