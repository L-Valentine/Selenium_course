import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://demo.nopcommerce.com')
driver.maximize_window()
time.sleep(1)

# click on link
driver.find_element(By.LINK_TEXT, 'Digital downloads').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Digital').click()

# find the total number of links on a page
links = driver.find_elements(By.TAG_NAME, 'a')
links = driver.find_elements(By.XPATH, '//a')
print('Total number of links: ', len(links))

# print list of links
for link in links:
    print(link.text)

time.sleep(5)
driver.close()
driver.quit()
