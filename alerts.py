import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
time.sleep(1)

# to open alert window
driver.find_element(By.XPATH, '//button[normalize-space()="Click for JS Prompt"]').click()

alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys('Welcome!')

# closing alert window by using OK button
alert_window.accept()

# closing alert window by using CANCEL button
alert_window.dismiss()

driver.get(url='https://mypage.rediff.com/login/dologin')
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH, '//input[@value="Login"]').click()  # login button
time.sleep(2)
driver.switch_to.alert.accept()

time.sleep(5)
driver.close()
driver.quit()
