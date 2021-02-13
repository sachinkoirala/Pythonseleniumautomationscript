from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/root/Desktop/QA all/QA with selenium /geckodriver")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()

time.sleep(5)

#driver.switch_to_alert().accept()  #closeswindowusing okbutton

driver.switch_to_alert().dismiss()