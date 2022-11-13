import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# open the web page
driver.get(url='https://vk.com')
time.sleep(1)

# maximize browser window
driver.maximize_window()
time.sleep(1)

# tag & id css selector
driver.find_element(By.CSS_SELECTOR, 'input#index_email').send_keys('abc@gmail.com')
driver.find_element(By.CSS_SELECTOR, '#index_email').send_keys('abc@gmail.com')

# tag & class css selector
driver.find_element(By.CSS_SELECTOR, 'input.VkIdForm__input').send_keys('abc@gmail.com')
driver.find_element(By.CSS_SELECTOR, '.VkIdForm__input').send_keys('abc@gmail.com')

# tag & attribute css selector
driver.find_element(By.CSS_SELECTOR, 'input[autocomplete=username]').send_keys('abc@gmail.com')
driver.find_element(By.CSS_SELECTOR, '[autocomplete=username]').send_keys('abc@gmail.com')

# tag & class & attribute css selector
driver.find_element(By.CSS_SELECTOR, 'input.VkIdForm__input[autocomplete=username]').send_keys('abc@gmail.com')
driver.find_element(By.CSS_SELECTOR, '.VkIdForm__input[autocomplete=username]').send_keys('abc@gmail.com')

driver.get(url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(1)
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(1)
driver.find_element(By.NAME, 'password').send_keys('admin123')
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button').click()
time.sleep(1)
driver.get('https://www.orangehrm.com')

# Absolute / Full XPath
driver.find_element(By.XPATH, '/html/body/nav/div/div/div[2]/ul/li[2]/a').click()

# Relative / Partial XPath
driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a').click()

driver.get(url='https://demo.nopcommerce.com')
driver.maximize_window()
time.sleep(1)

# Absolute / Full XPath
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()

# Relative / Partial XPath
driver.find_element(By.XPATH, '//input[@id="small-searchterms"]').send_keys('Lenovo Thinkpad X1 Carbon Laptop')
driver.find_element(By.XPATH, '//*[@id="small-searchterms"]').send_keys('Lenovo Thinkpad X1 Carbon Laptop')

driver.get(url='http://automationpractice.com/index.php')
time.sleep(1)

# Absolute / Full XPath
driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]').send_keys('T-shirts')
driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button').click()

# Relative / Partial XPath
driver.find_element(By.XPATH, '//*[@id="search_query_top"]').send_keys('T-shirts')
driver.find_element(By.XPATH, '//*[@id="searchbox"]/button').click()

# Relative / Partial XPath with or / and operator
driver.find_element(By.XPATH, '//input[@id="search_query_top" or @name="search_query"]').send_keys('T-shirts')
driver.find_element(By.XPATH, '//button[@name="submit_search" and @class="btn btn-default button-search"]').click()

# contains() / starts-with()
driver.find_element(By.XPATH, '//input[contains(@id, "search"]').send_keys('T-shirts')
driver.find_element(By.XPATH, '//button[starts-with(@name, "submit_"]').click()

# text()
driver.find_element(By.XPATH, '//a[text()="Women"]').click()

driver.close()
driver.quit()