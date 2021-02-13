from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox(executable_path="/root/Desktop/QA with selenium /python/pycharmselenium/geckodriver")

driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")

time.sleep(5)
print(driver.title)

driver.back()

time.sleep(5)
print(driver.title)

driver.forward()

time.sleep(5)
print(driver.title)



