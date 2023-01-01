import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()
time.sleep(1)

drpcountry_ele = driver.find_element(By.XPATH, '//select[@id="input-country"]')
drpcountry = Select(drpcountry_ele)
drpcountry = Select(driver.find_element(By.XPATH, '//select[@id="input-country"]'))

# select option from the dropdown
drpcountry.select_by_visible_text('India')
time.sleep(1)
drpcountry.select_by_value('10')  # Argentina
time.sleep(1)
drpcountry.select_by_index(13)  # Australia

# capture all the options from the dropdown and print them
drpcountry_opt = drpcountry.options
print('Total number of options: ', len(drpcountry_opt))

for opt in drpcountry_opt:
    print(opt.text)

# select an option from the dropdown list without using built-in methods
for opt in drpcountry_opt:
    if opt.text == 'India':
        opt.click()
        break

drpoptions = driver.find_elements(By.XPATH, '//*[@id="input-country"]/option')
print(len(drpoptions))

time.sleep(5)
driver.close()
driver.quit()
