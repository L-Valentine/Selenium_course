import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='http://www.deadlinkcity.com')
driver.maximize_window()
time.sleep(1)

links = driver.find_elements(By.TAG_NAME, 'a')
count = 1

for link in links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, '--> is broken link, ', 'Status code: ', res.status_code)
        count += 1
    else:
        print(url, '--> is valid link, ', 'Status code: ', res.status_code)

print('Total number of broken links: ', count)

time.sleep(5)
driver.close()
driver.quit()
