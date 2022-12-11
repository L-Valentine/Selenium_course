import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://demo.nopcommerce.com/register')
driver.maximize_window()
time.sleep(1)

# is_displayed() is_enabled()
searchbox = driver.find_element(By.XPATH, '//input[@id="small-searchterms"]')
print('-' * 100)
print('Displayed status: ', searchbox.is_displayed()) # True
print('Enabled status: ', searchbox.is_enabled()) # True

# is_selected() - for radio buttons and checkboxes
rd_male = driver.find_element(By.XPATH, '//input[@id="gender-male"]')
rd_female = driver.find_element(By.XPATH, '//input[@id="gender-female"]')

print('-' * 100)
print('Default radio buttons statuses')
print('First radio button selected status: ', rd_male.is_selected()) # False
print('Second radio button selected status: ', rd_female.is_selected()) # False

rd_male.click() # select male radio button

print('-' * 100)
print('Radio buttons statuses after selecting male button')
print('First radio button selected status: ', rd_male.is_selected()) # True
print('Second radio button selected status: ', rd_female.is_selected()) # False

rd_female.click() # select female radio button
print('-' * 100)
print('Radio buttons statuses after selecting female button')
print('First radio button selected status: ', rd_male.is_selected()) # False
print('Second radio button selected status: ', rd_female.is_selected()) # True

driver.close()
driver.quit()
