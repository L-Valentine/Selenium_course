import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://www.google.com')
driver.maximize_window()
time.sleep(1)
driver.get(url='https://www.amazon.com')
time.sleep(1)

# return to the previous page
driver.back()
time.sleep(1)

# go to the next page
driver.forward()
time.sleep(1)

# to refresh the page
driver.refresh()
time.sleep(1)

driver.close()
driver.quit()
