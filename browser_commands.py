import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(1)

driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
time.sleep(1)

# close() - this command used to close the browser. By this command, if more than one browser window has been opened,
# only one of them ('parent' browser window, where driver is focused) will be closed.
driver.close()

# quit() - this command is used to terminate a process. By this command, if more than one browser window has been
# opened, each of them will be closed.
driver.quit()
