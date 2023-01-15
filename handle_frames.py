import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
driver.maximize_window()
time.sleep(1)

# frame / iframe / form
# switch_to.frame(0) - if there is only one frame on the page
# switch_to.frame(name_of_the_frame)
# switch_to.frame(id_of_the_trame)
# switch_to.frame(web-element)

driver.switch_to.frame('packageListFrame')  # switching to the first frame
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium').click()
driver.switch_to.default_content()  # go back to the main page
time.sleep(1)

driver.switch_to.frame('packageFrame')  # switching to the second frame
driver.find_element(By.LINK_TEXT, 'WebDriver').click()
driver.switch_to.default_content()  # go back to the main page
time.sleep(1)

driver.switch_to.frame('classFrame')  # switching to the third frame
driver.find_element(By.XPATH, '/html/body/header/nav/div[1]/div[1]/ul/li[8]/a').click()
time.sleep(1)

driver.close()
driver.quit()
