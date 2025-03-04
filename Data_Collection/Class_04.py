from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set Chrome options
chrome_option = Options()
chrome_option.add_argument('--headless')           # Run in headless mode
chrome_option.add_argument('--no-sandbox')          # Bypass OS security model
chrome_option.add_argument('--disable-dev-shm-usage') # Overcome limited resource problems
chrome_option.add_argument('--incognito')
chrome_option.add_argument('--disable-cache')

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.daraz.com.bd/products/adjustable-hand-grip-5-60kg-strengthen-your-grip-with-precision-and-comfort-using-this-adjustable-hand-grip-i223264230-s1169372473.html?pvid=2ed698c7-4fb8-491d-a406-3ee18e1db142&search=jfy&scm=1007.51705.413671.0&spm=a2a0e.tm80335411.just4u.d_223264230")
driver.maximize_window()
time.sleep(1)

height = driver.execute_script('return document.body.scrollHeight;')

print("height is --->",height)

for i in range(0,height+1300,100):
    driver.execute_script(f'window.scrollTo(0,{i})')
    time.sleep(0.2)
all_comments = driver.find_elements(By.CLASS_NAME,"content")

print(len(all_comments))
comments = []
dates = []
for comment in all_comments:
    # print(all_comments[i])
    comments.append(comment.text)
    


time.sleep(1)
# convert data frame
df = pd.DataFrame(comments,columns=['comment'])

# save excel
df.to_excel('comment.xlsx',index=False)
# print("save excel file successfully")
driver.quit()