from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path="/root/Desktop/QA all/QA with selenium /geckodriver")

driver.get("file:///root/Desktop/QA%20all/QAselenium%20/python/pycharmselenium/htmltable.html")

rows=len(driver.find_element_by_xpath("/html/body/table/tbody/tr"))
cols=len(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th"))

print(rows)
print(cols)
