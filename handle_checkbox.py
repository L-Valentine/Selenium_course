import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://itera-qa.azurewebsites.net/home/automation')
driver.maximize_window()
time.sleep(1)

# select specific checkbox
driver.find_element(By.XPATH, '//input[@id="monday"]').click()

# select all the checkboxes
weekdays = driver.find_elements(By.XPATH, '//input[@type="checkbox" and contains(@id, "day")]')
print(len(weekdays))

# select all the checkboxes, approach 1:
for i in range(len(weekdays)):
    weekdays[i].click()

# select all the checkboxes, approach 2:
for day in weekdays:
    day.click()

# select multiple checkboxes by choice
for day in weekdays:
    weekname = day.get_attribute('id')
    if weekname == 'monday' or weekname == 'sunday':
        day.click()

for day in weekdays:
    weekname = day.get_attribute('id')
    if weekname in ('monday', 'friday', 'sunday'):
        day.click()

# select last 2 checkboxes
for i in range(len(weekdays) - 2, len(weekdays)):  # range(5, 7)
    weekdays[i].click()

# select first 2 checkboxes
for i in range(len(weekdays)):
    if i < 2:
        weekdays[i].click()

# clear all the checkboxes
for day in weekdays:
    if day.is_selected():
        day.click()

time.sleep(5)
driver.close()
driver.quit()
