from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
import re
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#solve captcha issue
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("start-maximized")
# Initialize the undetected driver
driver = uc.Chrome(options=options)

##cash issue
# chrome_options = Options()
# chrome_options.add_argument("--disable-cache")
# chrome_options.add_argument("--incognito")
# driver = webdriver.Chrome(options=chrome_options)
# # driver = webdriver.Chrome()



driver.get('https://www.google.com/')

driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Laptop Shop Near Mirpur")

search_box.send_keys(Keys.RETURN)

time.sleep(10)

# go to map
g_map = driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a').click()
time.sleep(10)

#click for scroll
driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[2]')
# Scroll to the bottom of the page
height = driver.execute_script("return document.body.scrollHeight")
print(height)
for i in range(0, height, 30):
    driver.execute_script(f'window.scrollTo(0, {i})')
    time.sleep(5)

product_title = driver.find_element(By.XPATH, '//h1').text
print(f'Product Title: {product_title}')

time.sleep(10)
driver.quit()
