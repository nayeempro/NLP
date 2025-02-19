from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
print("hello start")
driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/routers/?page=1')
driver.maximize_window()


# find how many page available of a specific product
get_prod_num = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text
total_prod = int(get_prod_num.split()[0])
total_page = round(total_prod/40)
print("Page no",total_prod, type(total_prod),total_page)
link_dict = {}

for i in range(1,total_page):
    driver.get(f'https://www.daraz.com.bd/routers/?page={i}')
    print(f'page no {i} opening')
    driver.maximize_window()
    key = f"page_{i}"
    link_dict[key] = []
    for product in range(1,41):
        str_prod = str(product)
        link = driver.find_element(By.CSS_SELECTOR,f'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child('+str_prod+') > div > div > div.buTCk > div.RfADt > a').get_attribute('href')
        driver.maximize_window()
        link_dict[key].append(link)
        print("link is --->",link)
    print(link_dict[key])

print("all dict is ---->",link_dict)

# ------This part is just for my own interest Just ignore it -------

# Flatten the data into a list of tuples [(page, link), (page, link), ...]
flattened_data = [(page, link) for page, links in link_dict.items() for link in links]
# Convert to DataFrame
df = pd.DataFrame(flattened_data, columns=["Page Number", "Link"])
# Save to Excel
df.to_excel("output.xlsx", index=False)


time.sleep(10)
driver.quit()