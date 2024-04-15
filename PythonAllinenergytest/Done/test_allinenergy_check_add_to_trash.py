from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("start-maximized")



class TestOrder:
    driver = ''

    def setup_method(self): #Prerequisities

        self.driver = webdriver
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('C:\Python_Selenium\pythonProject\chromedriver.exe')
        self.driver.implicitly_wait(20)
        self.driver.get('https://allinenergy.com.ua/')

    def test_allinenergy(self): #SelectDropdown
        menu = self.driver.find_element(By.XPATH, "//span[@class='table-nav__link-image']/img[contains(@src,'/uploads/icons/icon3.png')]")
        submenu = self.driver.find_element(By.XPATH, "//a[@class='tree-nav__link' and @href = 'https://allinenergy.com.ua/vimikachi-rozetki-schneider-electric']")
        submenu1 = self.driver.find_element(By.XPATH,"//a[@class='tree-nav__link' and @href= 'https://allinenergy.com.ua/rozetki-vimikachi-schneider-electric-asfora']")

        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.move_to_element(submenu)
        actions.move_to_element(submenu1)
        actions.click(submenu1)
        actions.perform()

        self.driver.execute_script("window.scrollBy(0,500)")

        goods = self.driver.find_element(By.XPATH, "//img[@title = 'Schneider ASFORA РАМКА 2-ПОСТОВА, ГОРИЗОНТАЛЬНА, КРЕМОВИЙ EPH5800223']")
        actions = ActionChains(self.driver).move_to_element(goods)
        button = self.driver.find_element(By.XPATH, "//button[@class = 'product-buy__btn product-buy__btn--buy']")
        actions.click(button)
        actions.perform()
        time.sleep(2)
        proceed = self.driver.find_element(By.XPATH,"//button[@class = 'btn btn-default']")
        actions.click(proceed)
        actions.perform()
        time.sleep(2)
        # self.driver.back()

        self.driver.execute_script("window.scrollBy(0,-500)")
        time.sleep(2)

        actual_text = self.driver.find_element(By.XPATH,"//div[@class = 'cart-header__desc']").text
        expected_text = '1 - ₴49,56'
        assert actual_text == expected_text, f"error Expected text: '{expected_text}', but actual text: '{actual_text}'"


        trash = self.driver.find_element(By.XPATH, "//a[@href = 'https://allinenergy.com.ua/shop/cart']").click()
        PlusButton = self.driver.find_element(By.XPATH, "//button[@data-form-quantity-control = 'plus']").click()
        time.sleep(2)
        MinusButton = self.driver.find_element(By.XPATH, "//button[@data-form-quantity-control = 'minus']").click()
        time.sleep(2)

        ConfirmOrder = self.driver.find_element(By.XPATH, "//a[@class = 'btn btn--va-m btn-primary']").click()
        time.sleep(2)

        # Final Order Menu
        InputName = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[fullName]']").send_keys("Taras Prystaiko")
        InputEmail = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[email]']").send_keys("tarasprystaiko@gmail.com")
        InputPhone = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[phone]']").send_keys("+380686725269")
        InputAddress = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[deliverTo]']").send_keys("Skorupska 25/23")
        # #FinalOrderL= self.driver.find_element(By.XPATH, "//input[@value = 'Підтвердити заказ']").click()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()