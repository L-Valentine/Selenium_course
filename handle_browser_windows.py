import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(1)

window_id = driver.current_window_handle
print(window_id)

driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
window_ids = driver.window_handles
time.sleep(1)

# Approach 1
parent_window_id = window_ids[0]
child_window_id = window_ids[1]
print(parent_window_id, child_window_id)
print('-' * 30)

driver.switch_to.window(child_window_id)
print('Title of the child window: ', driver.title)
time.sleep(1)

driver.switch_to.window(parent_window_id)
print('Title of the parent window: ', driver.title)
print('-' * 30)

# Approach 2
for wind_id in window_ids:
    driver.switch_to.window(wind_id)
    print(driver.title)

# close specific browser window:
for wind_id in window_ids:
    driver.switch_to.window(wind_id)
    if driver.title == 'OrangeHRM':
        driver.close()

for wind_id in window_ids:
    driver.switch_to.window(wind_id)
    if driver.title == 'OrangeHRM' or driver.title == 'OrangeHRM HR Software | Free & Open Source HR Software | HRMS ' \
                                                      '| HRIS | OrangeHRM':
        driver.close()

driver.quit()
