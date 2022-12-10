import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# open the web page
driver.get(url='https://money.rediff.com/gainers/bse/daily/groupa')
driver.maximize_window()
time.sleep(1)

# self
text_msg = driver.find_element(By.XPATH, '//a[contains(text(), "Brightcom Group")]/self::a').text
print(text_msg)

# parent
# text method can be used only for one element, for multiply elements use loop!
text_msg = driver.find_element(By.XPATH, '//a[contains(text(), "Brightcom Group")]/parent::td').text
print(text_msg)

# to capture child elements
children = driver.find_elements(By.XPATH, '//a[contains(text(), "Panama Petrochem")]/ancestor::tr/child::td')
print(len(children)) # 5

# ancestor
text_msg = driver.find_element(By.XPATH, '//a[contains(text(), "Panama Petrochem")]/ancestor::tr').text
print(text_msg) # Panama Petrochem A 331.30 352.90 + 6.52

# descendant
descendants = driver.find_elements(By.XPATH, '//a[contains(text(), "Panama Petrochem")]/ancestor::tr/descendant::*')
print('Number of descendant nodes: ', len(descendants)) # 7

# following
followings = driver.find_elements(By.XPATH, '//a[contains(text(), "PB Fintech")]/ancestor::tr/following::*')
print('Number of following nodes: ', len(followings)) # 3391

# following-sibling
following_siblings = driver.find_elements(By.XPATH, '//a[contains(text(), "PB '
                                                    'Fintech")]/ancestor::tr/following-sibling::tr')
print('Number of following-siblings nodes: ', len(following_siblings)) # 406

# preceding
preceding = driver.find_elements(By.XPATH, '//a[contains(text(), "PB Fintech")]/ancestor::tr/preceding::tr')
print('Number of preceding nodes: ', len(preceding)) # 13

# preceding-sibling
preceding_siblings = driver.find_elements(By.XPATH, '//a[contains(text(), "PB '
                                                    'Fintech")]/ancestor::tr/preceding-sibling::tr')
print('Number of preceding siblings nodes: ', len(preceding_siblings)) # 12

driver.close()
driver.quit()
