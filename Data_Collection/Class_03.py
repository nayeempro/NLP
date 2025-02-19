from selenium import webdriver
import time
from selenium.webdriver.common.by import By
print("hello start")
driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/routers/?page=1')
driver.maximize_window()
# find how many page available of a specific product
get_prod_num = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text
total_prod = int(get_prod_num.split()[0])
total_page = round(total_prod/40)
print("Page no",total_prod, type(total_prod),total_page)
link_list = []
# here i get product link from 1-5 no product for 1-2 page (5*2 = 10 )
for page in range(1,3):
    driver.get(f'https://www.daraz.com.bd/routers/?page={page}')
    print(f'page no {page} opening')
    driver.maximize_window()
    for prod in range(1,6):
        str_prod = str(prod)
        link = driver.find_element(By.XPATH,f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+str_prod+']/div/div/div[2]/div[2]/a').get_attribute('href')
        print(f' from --->{page} product no {prod}')
        link_list.append(link)





print(link_list,len(link_list))


time.sleep(10)
driver.quit()