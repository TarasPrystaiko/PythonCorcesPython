from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

class TestAmazonHover:
    driver = ''

    def setup_method(self):

        self.driver = webdriver
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('C:\Python_Selenium\pythonProject\chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.get('https://allinenergy.com.ua/')

    def test_allinenergy_hover(self):
        menu = self.driver.find_element(By.XPATH, "//span[@class='table-nav__link-image']/img[contains(@src,'/uploads/icons/icon3.png')]")
        submenu = self.driver.find_element(By.XPATH, "//a[@class='tree-nav__link' and @href = 'https://allinenergy.com.ua/vimikachi-rozetki-schneider-electric']")
        submenu1 = self.driver.find_element(By.XPATH,"//a[@class='tree-nav__link' and @href= 'https://allinenergy.com.ua/rozetki-vimikachi-schneider-electric-asfora']")


        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.move_to_element(submenu)
        actions.move_to_element(submenu1)
        actions.click(submenu1)
        actions.perform()
        actual_text = self.driver.find_element(By.XPATH, "//div[@class ='content__header']/h1").text
        expected_text = 'Розетки, Вимикачі Schneider Electric Asfora'
        assert actual_text == expected_text, f"error Expected text: '{expected_text}', but actual text: '{actual_text}'"

    def teardown_method(self):
        self.driver.quit()