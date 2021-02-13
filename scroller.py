from selenium import webdriver
import time

driver=webdriver.Firefox(executable_path="/root/Desktop/QA all/QA with selenium /geckodriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#there are three ways of scrolling the pages


#3.scroll to end of page

driver.maximize_window() #maximize window size
#1.scroll down the pagwe by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

#2.scroll down the page till element found
nepal=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[2]/tbody/tr[23]/td[1]/img")
driver.execute_script("arguements[0].scrollIntoView() ;",nepal)

