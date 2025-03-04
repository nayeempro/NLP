from selenium import webdriver
from selenium.webdriver.common.by import By
# import option for chrome option
from selenium.webdriver.chrome.options import Options
# import keys for google enter
from selenium.webdriver.common.keys import Keys
# import actionchain
from selenium.webdriver.common.action_chains import ActionChains
import time
chrome_option = Options()
chrome_option.add_argument('--incognito')
chrome_option.add_argument('--disable-cache')

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://www.google.com/')
driver.maximize_window()
search_box = driver.find_element(By.NAME,"q")
time.sleep(10)
search_box.send_keys("Dhanmondi Computer Shop")
search_box.send_keys(Keys.RETURN)
# find the recaptcha class
recaptcha_checkbox = driver.find_element(By.CLASS_NAME, "g-recaptcha")
time.sleep(10)
action = ActionChains(driver)
action.move_to_element(recaptcha_checkbox).click().perform()






time.sleep(100)
driver.quit()
