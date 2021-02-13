from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="/root/Desktop/QA all/QA with selenium /geckodriver")

driver.get("http://advantageonlineshopping.com/#/")

#how many links, capture links ,click on links

links = driver.find_elements(By.TAG_NAME,"a")

print("Number of links present:",len(links)) #howmanylinks

for link in links:
    print(link.text)
