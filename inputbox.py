from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/root/Desktop/QA all/QA with selenium /geckodriver")


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# script to find how many input boxes in a webpage

inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("koirala")

print(len(inputboxes))

status=driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("displayed or not:", status)

status=driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("enabled or not:", status)

#how to provide value into the textbox

driver.find_element(By.ID,'RESULT_TextField-1').send_keys("sachin")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("koirala")
driver.find_element_by_id('RESULT_TextField-3').send_keys("`12345678")

#how to get the status of webpage