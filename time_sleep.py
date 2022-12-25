# time.sleep(time in seconds)
# Advantages:
# - simple to use
# Disadvantages:
# - performance of the script is very poor
# - if the element is not available within the time mentioned, still there is a chance to getting exception

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://www.google.com')
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys('Selenium')
searchbox.submit()

time.sleep(5)
driver.find_element(By.XPATH, '//h3[text()="Selenium"]').click()

driver.close()
driver.quit()
