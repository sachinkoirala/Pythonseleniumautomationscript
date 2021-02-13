from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path="/root/Desktop/QA all/QA with selenium /geckodriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


#working with the radio button

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

#driver.find_element_by_id("RESULT_RadioButton-7_0").click()

#status=driver.find_elements_by_id("RESULT_RadioButton-7_0").is_selected()
#print(status)

#working with check boxes

driver.find_element_by_id("RESULT_CheckBox-8_0").click()
driver.find_element_by_id("RESULT_CheckBox-8_6").click()


