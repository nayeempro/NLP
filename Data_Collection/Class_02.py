from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/routers/')
driver.maximize_window()

link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/a')


print(link.get_attribute('href'))

driver.get(link.get_attribute('href'))
time.sleep(100)
driver.quit()
