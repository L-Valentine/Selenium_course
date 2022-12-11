import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# get() - opening the application URL
driver.get(url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(1)

# title - to capture the title of the current webpage
print(driver.title) # OrangeHRM

# current_url - to capture the URL of the current webpage
print(driver.current_url) # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

# page_source - to capture source code of the page
print(driver.page_source)

driver.close()
driver.quit()
