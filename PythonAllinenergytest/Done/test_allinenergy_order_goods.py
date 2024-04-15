from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("start-maximized")



class TestOrder:
    driver = ''

    def setup_method(self): #Prerequisities

        self.driver = webdriver
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('C:\Python_Selenium\pythonProject\chromedriver.exe')
        self.driver.implicitly_wait(5)
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

        actual_text = self.driver.find_element(By.XPATH, "//div[@class ='content__header']/h1").text
        expected_text = 'Розетки, Вимикачі Schneider Electric Asfora'
        assert actual_text == expected_text, f"error Expected text: '{expected_text}', but actual text: '{actual_text}'"

        self.driver.back()
        self.driver.forward()


        good1 = self.driver.find_element(By.XPATH, "//div[@class = 'product-photo']//img[@title = 'Schneider ASFORA РАМКА 1- ПОСТОВА СТАЛЬ EPH5800162']").click()

        actual_text = self.driver.find_element(By.XPATH, "//div[@class = 'content__header content__header--xs']/h1").text
        expected_text = 'Schneider ASFORA РАМКА 1- ПОСТОВА СТАЛЬ EPH5800162'
        assert actual_text == expected_text, f"error Expected text: '{expected_text}', but actual text: '{actual_text}'"

        #GoodsMenu
        PlusButton = self.driver.find_element(By.XPATH,"//button[@data-form-quantity-control = 'plus']").click()
        MinusButton = self.driver.find_element(By.XPATH,"//button[@data-form-quantity-control = 'minus']").click()
        BuyButton = self.driver.find_element(By.XPATH,"//button[@class = 'product-buy__btn product-buy__btn--buy']").click()
        ConfirmOrder = self.driver.find_element(By.XPATH, "//a[@class = 'btn btn--va-m btn-primary']").click()

        #Final Order Menu
        InputName = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[fullName]']").send_keys("Taras Prystaiko")
        InputEmail = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[email]']").send_keys("tarasprystaiko@gmail.co")
        InputPhone = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[phone]']").send_keys("+380686725269")
        InputAddress = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[deliverTo]']").send_keys("Skorupska 25/23")

        # FinalOrderL= self.driver.find_element(By.XPATH, "//input[@value = 'Підтвердити заказ']").click()

    def teardown_method(self):
        self.driver.quit()