import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://demo.nopcommerce.com')
driver.maximize_window()
time.sleep(1)

# find_element returns single web element
# 1. Locator matching with single web element
element = driver.find_element(By.XPATH, '//input[@id="small-searchterms"]')
element.send_keys('Apple MacBook Pro 13-inch')

# 2. Locator matching with multiple web elements
element = driver.find_element(By.XPATH, '//div[@class="footer"]//a')
print(element.text)  # it will return first link from the footer - "Sitemap"

# 3. Element not available then throw NoSuchElementException
login_element = driver.find_element(By.LINK_TEXT, 'Log')  # here is used incorrect locator
login_element.click()

# find_elements returns multiple web elements
# 1. Locator matching with single web element
# Even the locator matching with single web element, the "find_elements" method returns list
elements = driver.find_elements(By.XPATH, '//input[@id="small-searchterms"]')
print(len(elements))  # 1
print(elements[0])  # <selenium.webdriver.remote.webelement.WebElement (session="676699ad28a0d1961798bb8d8788024e",
# element="0927d6f8-4b32-4934-8eda-d1ed0f70612c")>
# get access to such element:
elements[0].send_keys('Apple MacBook Pro 13-inch')
time.sleep(1)

# 2. Locator matching with multiple web elements
elements = driver.find_elements(By.XPATH, '//div[@class="footer"]//a')
print(len(elements))  # 23
print(elements[0].text)  # Sitemap (first element of the list)

# to print all elements of the list:
for element in elements:
    print(element.text)

# 3. Element not available - no exceptions
elements = driver.find_elements(By.LINK_TEXT, 'Log')  # here is used incorrect locator
print('Elements returned: ', len(elements))

driver.close()
driver.quit()
