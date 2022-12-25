import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://admin-demo.nopcommerce.com/login')
driver.maximize_window()
time.sleep(1)

emailbox = driver.find_element(By.XPATH, '//input[@id="Email"]')
emailbox.clear()
emailbox.send_keys('abc@gmail.com')
time.sleep(1)
loginbutton = driver.find_element(By.XPATH, '//button[normalize-space()="Log in"]')

# Text method returns inner text of the web element
# Get attribute method returns the value of any attribute of the web element

print('Result of text: ', emailbox.text)  # ---
print('Result of get_attribute: ', emailbox.get_attribute('value'))  # abc@gmail.com

print('-' * 30)

print('Result of text: ', loginbutton.text)  # LOG IN
print('Result of get_attribute: ', loginbutton.get_attribute('value'))  # ---
print('Result of get_attribute: ', loginbutton.get_attribute('type'))  # submit

driver.close()
driver.quit()
