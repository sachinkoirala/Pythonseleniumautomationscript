from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#firefox
driver=webdriver.Firefox(executable_path="/root/Desktop/QA with selenium /python/pycharmselenium/geckodriver")

driver.get ("http://demo.automationtesting.in/Register.html")

print(driver.title)      #return the tile og page
print(driver.current_Url)  #return the URL of the page

driver.find_element_by_xpath ("//*[@id='submitbtn']").click()

time.sleep(5)
driver.close()