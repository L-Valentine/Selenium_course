import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# open the web page
driver.get(url='http://automationpractice.com/index.php')
time.sleep(1)

# maximize browser window
driver.maximize_window()
time.sleep(1)

# find multiply elements using CLASS_NAME selector
sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
print(len(sliders))

# find multiply links using TAG_NAME selector
links = driver.find_elements(By.TAG_NAME, 'a')
time.sleep(1)
print(len(links))

driver.close()
driver.quit()
