from selenium import webdriver


driver=webdriver.Firefox(executable_path="/root/Desktop/QA with selenium /python/pycharmselenium/geckodriver")

driver.implicitly_wait(5)

driver.maximize_window()
0
driver.get("http://www.expedia.com")

# driver.implicitly_wait(10) it is for implicit wait
 #assert "My joomla" in driver.title
 #driver.find_element_by_name("username")

driver.find_element(By.ID,"tab-flight-tab-hp").click() #clickonflightsbutton



driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO") #clickonflightsbutton

time.sleep(2) #from_python

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("12/02/2021")

driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("15/02/2021")






