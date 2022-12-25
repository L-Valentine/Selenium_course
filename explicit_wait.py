# explicit wait (works based on condition)
# Advantages:
# - more effective
# - built-in exception handler
# Disadvantages:
# - must be added in multiple places in script

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driverwait = WebDriverWait(driver, 10)  # explicit wait declaration, basic syntax
# driverwait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException,
#                                                            ElementNotVisibleException,
#                                                            ElementNotSelectableException])
driverwait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])

driver.get(url='https://www.google.com')
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys('Selenium')
searchbox.submit()

searchlink = driverwait.until(EC.presence_of_element_located((By.XPATH, '//h3[text()="Selenium"]')))
searchlink.click()

driver.close()
driver.quit()
