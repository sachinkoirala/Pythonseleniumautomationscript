from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver=webdriver.Firefox(executable_path="/root/Desktop/QA all/QA with selenium /geckodriver")


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#work on
element = (driver.find_element_by_id("RESULT_RadioButton-9"))
drp = Select(element)

#selectbyvisibletext
#drp.select_by_visible_text('Morning')

#selectbyindex number
#drp.select_by_index(2) #selectafternoon

#selectbyvalue
drp.select_by_value("Radio-2")

#capturalloptionsandprint

print(len(drp.options))
all_options=drp.options

for option in all_options:
    print(option.text)









