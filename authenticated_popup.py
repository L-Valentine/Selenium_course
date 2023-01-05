import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# injecting username and password into url to bypass the authentication popup
driver.get(url='https://admin:admin@the-internet.herokuapp.com/basic_auth')
driver.maximize_window()
time.sleep(2)

driver.close()
driver.quit()
