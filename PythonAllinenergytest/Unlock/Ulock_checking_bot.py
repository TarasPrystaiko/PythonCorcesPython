from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service: Service = Service(executable_path="../chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.pl/")

time.sleep(10)

