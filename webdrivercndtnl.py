from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox(executable_path="/root/Desktop/QA with selenium /python/pycharmselenium/geckodriver")

driver.get("http://emo.com/")

user_ele=driver.find_element_by_name("username")

print(ele.is_displayed()) #returns true or false based of element status

print(ele.is_enabled())   #return t/f


pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed()) #returns true or false based of element status
print(pwd_ele.is_enabled())

user_ele.send_keys("asdfgh")
pwd_ele.send_keys("1234567")

driver.find_element_by_name("Submit").click()




