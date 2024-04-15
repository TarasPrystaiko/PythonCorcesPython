import pytest
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

    def test_allinenergy_left_menu(self):
        defend_menu= self.driver.find_element(By.XPATH,"//span[@class='table-nav__link-image']/img[contains(@src,'/uploads/icons/icon2.png')]")
        def_aut_menu = self.driver.find_element(By.XPATH,"//a[@class='tree-nav__link' and @href = 'https://allinenergy.com.ua/nizkovoltne-obladnannia']")
        aut_as_menu = self.driver.find_element(By.XPATH,"//a[@class='tree-nav__link' and @href= 'https://allinenergy.com.ua/avtomatichni-vimikachi']")
        aut_as_submenu = self.driver.find_element(By.XPATH,"//a[@class='tree-nav__link' and @href= 'https://allinenergy.com.ua/avtomatichni-vimikachi-modulni']")

        actions = ActionChains(self.driver)
        actions.move_to_element(defend_menu)
        actions.move_to_element(def_aut_menu)
        actions.move_to_element(aut_as_menu)
        actions.move_to_element(aut_as_submenu)
        actions.click(aut_as_submenu)
        actions.perform()

#Select brend

        typeofnebwork = self.driver.find_element(By.ID, "brand-schneider-electric").click() #select
        actual_text = self.driver.find_element(By.XPATH,"//span[@class='active-filters__btn-link' and contains(text(), 'Schneider Electric')]").text
        expected_text = 'Schneider Electric'
        assert actual_text == expected_text, f"Error: Expected text: '{expected_text}', but actual text: '{actual_text}'"
        typeofnebwork = self.driver.find_element(By.ID, "brand-schneider-electric").click() #unselect
        time.sleep(2)

        lemanso_brend = self.driver.find_element(By.ID, "brand-lemanso").click() #select
        actual_text = self.driver.find_element(By.XPATH,"//span[@class='active-filters__btn-link' and contains(text(), 'LEMANSO')]").text
        expected_text = 'LEMANSO'
        assert actual_text == expected_text, f"Error: Expected text: '{expected_text}', but actual text: '{actual_text}'"
        lemanso_brend = self.driver.find_element(By.ID, "brand-lemanso").click() #unselect
        time.sleep(2)


        hager_brend = self.driver.find_element(By.ID, "brand-hager").click()  # select
        actual_text = self.driver.find_element(By.XPATH,"//span[@class='active-filters__btn-link' and contains(text(), 'Hager')]").text
        expected_text = 'Hager'
        assert actual_text == expected_text, f"Error: Expected text: '{expected_text}', but actual text: '{actual_text}'"
        hager_brend = self.driver.find_element(By.ID, "brand-hager").click()  # unselect
        time.sleep(2)

        eti_brend = self.driver.find_element(By.ID, "brand-eti").click()  # select
        actual_text = self.driver.find_element(By.XPATH,"//span[@class='active-filters__btn-link' and contains(text(), 'ETI')]").text
        expected_text = 'ETI'
        assert actual_text == expected_text, f"Error: Expected text: '{expected_text}', but actual text: '{actual_text}'"
        eti_brend = self.driver.find_element(By.ID, "brand-eti").click()  # unselect


#Select TypeofNetwork

        typeofnebwork = self.driver.find_element(By.XPATH,"//div[@class='filter__title' and contains(text(), 'Тип мережі')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,"//div[@class='filter__title' and contains(text(), 'Тип мережі')]").click()

        self.driver.execute_script("window.scrollBy(0,500)")

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Кількість полюсів')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Кількість полюсів')]").click()

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Країна виробник')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Країна виробник')]").click()

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Застосування')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Застосування')]").click()

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Робоча температура повітря')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Робоча температура повітря')]").click()

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Тип управління')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Тип управління')]").click()

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Спосіб кріплення')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Спосіб кріплення')]").click()

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Тип товару')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Тип товару')]").click()

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Вага')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Вага')]").click()

        typeofnebwork = self.driver.find_element(By.XPATH,
                                                 "//div[@class='filter__title' and contains(text(), 'Колір')]").click()
        time.sleep(2)
        typeofnebwork = self.driver.find_element(By.XPATH,

                                                 "//div[@class='filter__title' and contains(text(), 'Колір')]").click()

    # def teardown_method(self):
        self.driver.quit()