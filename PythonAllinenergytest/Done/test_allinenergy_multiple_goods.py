import self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("start-maximized")


class TestMultipleGoods:
    driver = ''

    def setup_method(self):

        self.driver = webdriver
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('C:\Python_Selenium\pythonProject\chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.get('https://allinenergy.com.ua/')

    def test_allinenergy_ss(self): #Go to "sockets,switches" menu from header--SelectDropdown
        sock_menu = self.driver.find_element(By.XPATH, "//span[@class='table-nav__link-image']/img[contains(@src,'/uploads/icons/icon3.png')]")
        shn_submenu = self.driver.find_element(By.XPATH, "//a[@class='tree-nav__link' and @href = 'https://allinenergy.com.ua/vimikachi-rozetki-schneider-electric']")
        shn_as_submenu= self.driver.find_element(By.XPATH,"//a[@class='tree-nav__link' and @href= 'https://allinenergy.com.ua/rozetki-vimikachi-schneider-electric-asfora']")

        actions = ActionChains(self.driver)
        actions.move_to_element(sock_menu)
        actions.move_to_element(shn_submenu)
        actions.move_to_element(shn_as_submenu)
        actions.click(shn_as_submenu)
        actions.perform()

        self.driver.execute_script("window.scrollBy(0,500)")

        goods = self.driver.find_element(By.XPATH, "//img[@title = 'Schneider ASFORA РАМКА 2-ПОСТОВА, ГОРИЗОНТАЛЬНА, КРЕМОВИЙ EPH5800223']")
        actions = ActionChains(self.driver).move_to_element(goods)
        button = self.driver.find_element(By.XPATH, "//button[@class='product-buy__btn product-buy__btn--buy']/span[1]")
        actions.click(button)
        actions.perform()
        time.sleep(2)
        # Assuming you want to click the "+" button 3 times
        num_clicks = 3

        for _ in range(num_clicks):
            PlusButton = self.driver.find_element(By.XPATH, "//button[@data-form-quantity-control = 'plus']")
            actions.click(PlusButton)
            actions.perform()
            time.sleep(1)  # Add a short delay betwe en clicks to avoid overwhelming the application

        proceed = self.driver.find_element(By.XPATH,"//button[@class = 'btn btn-default']")
        actions.click(proceed)
        actions.perform()
        time.sleep(2)


        goods1 = self.driver.find_element(By.XPATH, "//img[@title = 'Schneider ASFORA РАМКА 2-ПОСТОВА, ГОРИЗОНТАЛЬНА, БІЛА EPH5800221']")
        ActionChains(self.driver).move_to_element(goods1).perform()
        button = self.driver.find_element(By.XPATH, "(//button[@class='product-buy__btn product-buy__btn--buy'])[2]/span[1]")
        actions.click(button)
        actions.perform()
        time.sleep(2)

        num_clicks = 3

        for _ in range(num_clicks):
            PlusButton1 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/form/div/div/div[2]/button")
            actions.click(PlusButton1)
            actions.perform()
            time.sleep(1)  # Add a short delay between clicks to avoid overwhelming the application

        proceed = self.driver.find_element(By.XPATH,"//button[@class = 'btn btn-default']")
        actions.click(proceed)
        actions.perform()
        time.sleep(2)


# def test_allinenergy_k(self):  # Go to "cable" menu from header--SelectDropdown
        self.driver.execute_script("window.scrollBy(0,-500)")

        kabel_menu = self.driver.find_element(By.XPATH,"//span[@class='table-nav__link-image']/img[contains(@src,'/uploads/icons/icon1.png')]")
        el_kabel = self.driver.find_element(By.XPATH,"//a[@class='tree-nav__link' and @href = 'https://allinenergy.com.ua/elektrichnii-kabel']")
        el_kabel_submenu = self.driver.find_element(By.XPATH,"//a[@class='tree-nav__link' and @href= 'https://allinenergy.com.ua/kabel-vvg-kruglii-silovii-midnii']")

        actions = ActionChains(self.driver)
        actions.move_to_element(kabel_menu)
        actions.move_to_element(el_kabel)
        actions.move_to_element(el_kabel_submenu)
        actions.click(el_kabel_submenu)
        actions.perform()

        self.driver.execute_script("window.scrollBy(0,500)")

        goods3 = self.driver.find_element(By.XPATH,  "//img[@title = 'ЗЗЦМ Кабель ВВГнгд 3х1,5 705343']")
        actions = ActionChains(self.driver).move_to_element(goods3)
        button_buy = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[2]/div[4]/div[1]/div/div/div/div[2]/article/div/div[5]/div[1]/div[1]/div/div/form/div[1]/button/span[1]")
        actions.click(button_buy)
        actions.perform()
        time.sleep(2)

        # proceed = self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-default']")
        # actions.click(proceed)
        # actions.perform()
        # time.sleep(2)

        complete_order = self.driver.find_element(By.XPATH, "//div[@class = 'modal__footer-btn']").click()
        time.sleep(2)


        #Final Order Menu
        InputName = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[fullName]']").send_keys("Taras Prystaiko")
        InputEmail = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[email]']").send_keys("tarasprystaiko@gmail.com")
        InputPhone = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[phone]']").send_keys("+380686725269")
        InputAddress = self.driver.find_element(By.XPATH, "//input[@name = 'userInfo[deliverTo]']").send_keys("Skorupska 25/23")
        # #FinalOrderL= self.driver.find_element(By.XPATH, "//input[@value = 'Підтвердити заказ']").click()

    def teardown_method(self):
        self.driver.quit()