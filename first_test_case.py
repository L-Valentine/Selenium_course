import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# old method (Selenium 3):
# driver = webdriver.Chrome(executable_path=r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")

# new method (Selenium 4)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open the web page
driver.get(url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(1)

# find login input
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(1)

# find password input
driver.find_element(By.NAME, 'password').send_keys('admin123')
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button').click()
time.sleep(1)

# compare titles / print test result
act_title = driver.title
exp_title = 'OrangeHRM'

if act_title == exp_title:
    print('Login Test Passed')
else:
    print('Login Test Failed')
time.sleep(1)
