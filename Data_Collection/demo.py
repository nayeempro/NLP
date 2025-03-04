from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

import re

# Set Chrome options
chrome_option = Options()
chrome_option.add_argument('--no-sandbox')          
chrome_option.add_argument('--disable-dev-shm-usage') 
chrome_option.add_argument('--incognito')
chrome_option.add_argument('--disable-cache')

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://duckduckgo.com/?t=h_&q=property+manager+at+Phoenix+%2B+%22child+care%22&ia=web&iaxm=maps&bbox=-112.22012176408694%2C33.68482944010742%2C-111.84404273591306%2C33.44828676010741')
driver.maximize_window()
time.sleep(5)

height = driver.execute_script('return document.body.scrollHeight;')
print("Height is --->", height)
num = []
name = []
for prod in range(1, 21):
    try:
        head = driver.find_element(By.XPATH,f'//*[@id="react-layout"]/div/div[2]/main/aside/section[2]/ol/li[{prod}]/article/div[1]/h2').text
        link = driver.find_element(By.XPATH, f'//*[@id="react-layout"]/div/div[2]/main/aside/section[2]/ol/li[{prod}]/article/div[1]/p[2]').text
        
        pattern = r"\+1\s\d{3}\s\d{3}\s\d{4}"
        match = re.search(pattern, link)

        # Append both name and phone number together to maintain equal length
        if match:
            num.append(match.group())
        else:
            num.append("N/A")

        name.append(head)  # Append name inside try block, ensuring equal length

    except Exception as e:
        print(f"Error retrieving element {prod}: {e}")
        # If there's an error retrieving the name, append placeholders to keep lengths equal
        name.append("N/A")  
        num.append("N/A")  

# Now, both lists have the same length, and the DataFrame will work correctly
data = pd.DataFrame({'Name': name, 'Number': num})
print(data)
data.to_excel("PhoneBook.xlsx", index=False)
driver.quit()
