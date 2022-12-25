# driver.implicitly_wait(10)
# Advantages:
# - single statement at the beginning of the script
# - performance will not be reduced (it the element available within the time it proceed to execute further statements.
# Disadvantages:
# - if the element is not available within the time mentioned, still there is a chance to getting exception

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)  # seconds implicit wait
# (It does not make sense to indicate more than 10 seconds, because if the application does not load within 10
# seconds, then there are obvious performance problems)
# Until the process terminates, this driver's implicit wait will always be available
# This implicit wait will apply to all next statements in the script

driver.get(url='https://www.google.com')
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys('Selenium')
searchbox.submit()

driver.find_element(By.XPATH, '//h3[text()="Selenium"]').click()

driver.close()
driver.quit()
