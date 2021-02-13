from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path="/root/Desktop/QA all/QA with selenium /geckodriver")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/io/package-summary.html")

driver.switch_to_frame("packageListFrame")  #firstframe
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to_default_content()

driver.switch_to_frame("packageFrame") #secondframe
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)


driver.switch_to_default_content()

time.sleep(3)


driver.switch_to_frame("classFrame") #thirdframe
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()





