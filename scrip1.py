from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="/root/Desktop/QA with selenium /python/pycharmselenium/geckodriver")

driver.get("http://newtours.demoaut.com/")

print(driver.title)



