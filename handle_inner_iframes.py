import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Надежда\Desktop\Учеба\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url='https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
time.sleep(1)

# frame / iframe / form
# switch_to.frame(0) - if there is only one frame on the page
# switch_to.frame(name_of_the_frame)
# switch_to.frame(id_of_the_trame)
# switch_to.frame(web-element)

driver.find_element(By.XPATH, '//a[normalize-space()="Iframe with in an Iframe"]').click()

outer_frame = driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(outer_frame)
time.sleep(1)

inner_frame = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_frame)
time.sleep(1)

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('welcome')
time.sleep(1)

driver.switch_to.parent_frame()  # switching back to outer_frame

driver.close()
driver.quit()
