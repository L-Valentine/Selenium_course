import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# open the web page
driver.get(url='https://demo.nopcommerce.com')
time.sleep(1)

# maximize browser window
driver.maximize_window()
time.sleep(1)

# find search line / enter value to find
# 1. find by ID
driver.find_element(By.ID, 'small-searchterms').send_keys('Lenovo Thinkpad X1 Carbon Laptop')

# 2. find by NAME
driver.find_element(By.NAME, 'q').send_keys('Lenovo Thinkpad X1 Carbon Laptop')
time.sleep(1)

# find element using link text
driver.find_element(By.LINK_TEXT, 'Register').click()

# find element using partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, 'Reg').click()
time.sleep(1)

driver.close()
driver.quit()
